#!/usr/bin/env python3
"""
Servidor Web FastAPI y API REST del Tutor Virtual Interactivo (Wisrovi Academy v12.0 Master Edition).
Expone endpoints para ejecutar código, evaluar retos, consultar memoria, micro-quizzes, auto-formateo y generar certificados.
"""

import os
import ast
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from pydantic import BaseModel
from typing import Dict, Any, Optional, List

from .gamification import GamificationEngine, StudentProfile
from .tutor_engine import TutorEngine
from .code_runner import CodeRunner
from .certificate import CertificateGenerator
from .embedded_ui import get_embedded_html

app = FastAPI(
    title="Wisrovi Python Academy - Local Server",
    description="Servidor local interactivo con tutor pedagógico y compilador seguro",
    version="2.6.0"
)

# Habilitar CORS para integración híbrida con GitHub Pages (academy_python.wisrovi.dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar motor de gamificación
gamification = GamificationEngine()

STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
os.makedirs(STATIC_DIR, exist_ok=True)

# ------------------------------------------------------------------------------
# MODELOS PYDANTIC PARA PETICIONES
# ------------------------------------------------------------------------------
class RunCodeRequest(BaseModel):
    code: str

class EvaluateChallengeRequest(BaseModel):
    course_num: int
    class_num: int
    code: str
    elapsed_seconds: Optional[int] = None

class UpdateProfileRequest(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

class AskMentorRequest(BaseModel):
    course_num: int
    class_num: int
    question: str
    code: Optional[str] = ""

class CertificateRequest(BaseModel):
    student_name: str
    course_title: Optional[str] = "Programa Integral de Formación en Python: De Cero a Agentes de IA"
    hours: Optional[int] = 160

class ClassCertificateRequest(BaseModel):
    course_num: int
    class_num: int
    student_name: Optional[str] = "Estudiante Wisrovi"

class ResetProgressRequest(BaseModel):
    confirm: bool

class FormatCodeRequest(BaseModel):
    code: str

class LintCodeRequest(BaseModel):
    code: str

class BenchmarkRequest(BaseModel):
    code: str
    iterations: Optional[int] = 50

class QuizEvaluateRequest(BaseModel):
    course_num: int
    class_num: int
    question_idx: int
    selected_idx: int

class SaveSolutionRequest(BaseModel):
    course_num: int
    class_num: int
    code: str

# ------------------------------------------------------------------------------
# ENDPOINTS REST
# ------------------------------------------------------------------------------
@app.get("/api/progress")
def get_progress():
    """Retorna las estadísticas del estudiante, XP, nivel y clases completadas."""
    profile = gamification.load_profile()
    return profile.model_dump()

@app.post("/api/progress")
def update_profile(req: UpdateProfileRequest):
    """Actualiza los datos del alumno (nombre, email)."""
    if req.name:
        gamification.profile.name = req.name
    if req.email:
        gamification.profile.email = req.email
    gamification.save_profile()
    return gamification.profile.model_dump()

@app.post("/api/progress/reset")
def reset_progress(req: ResetProgressRequest):
    """Reinicia todo el progreso del alumno a nivel 1 con 0 XP."""
    if not req.confirm:
        raise HTTPException(status_code=400, detail="Confirmación requerida para reiniciar")
    gamification.profile.xp = 0
    gamification.profile.level = 1
    gamification.profile.completed_classes = []
    gamification.profile.unlocked_badges = []
    gamification.save_profile()
    return gamification.profile.model_dump()

@app.get("/api/stats")
def get_global_stats():
    """Retorna estadísticas avanzadas de maestría en Python para el dashboard del estudiante."""
    classes = TutorEngine.get_all_classes_summary()
    completed_set = set(gamification.profile.completed_classes)
    
    course_stats = {}
    for c_id in range(1, 5):
        c_classes = [c for c in classes if c["course_num"] == c_id]
        c_done = sum(1 for c in c_classes if c["key"] in completed_set)
        course_stats[f"c{c_id}"] = {
            "total": len(c_classes),
            "completed": c_done,
            "pct": int((c_done / len(c_classes)) * 100) if c_classes else 0
        }
        
    return {
        "profile": gamification.profile.model_dump(),
        "course_stats": course_stats,
        "total_classes": len(classes),
        "completed_classes_count": len(completed_set),
        "global_progress_percent": int((len(completed_set) / len(classes)) * 100) if classes else 0
    }

@app.post("/api/format-code")
def format_code(req: FormatCodeRequest):
    """Auto-formatea código Python usando el analizador AST de Python."""
    try:
        parsed = ast.parse(req.code)
        if hasattr(ast, "unparse"):
            formatted = ast.unparse(parsed)
            return {"success": True, "formatted_code": formatted}
    except Exception as e:
        return {"success": False, "formatted_code": req.code, "error": str(e)}
    return {"success": True, "formatted_code": req.code}

@app.post("/api/lint-code")
def lint_code_endpoint(req: LintCodeRequest):
    """Analiza código mediante AST y linter pedagógico Wisrovi."""
    from .memory_inspector import MemoryInspector
    diagnostics = MemoryInspector.lint_code(req.code)
    return {
        "success": True,
        "diagnostics": diagnostics,
        "total_issues": len(diagnostics)
    }

@app.post("/api/benchmark-code")
def benchmark_code_endpoint(req: BenchmarkRequest):
    """Mide tiempo de CPU y memoria heap de una solución Python."""
    from .memory_inspector import MemoryInspector
    try:
        results = MemoryInspector.benchmark_code(req.code, iterations=req.iterations or 50)
        return {"success": True, "benchmark": results}
    except Exception as e:
        return {"success": False, "error": f"{type(e).__name__}: {str(e)}"}

@app.post("/api/save-solution")
def save_solution_to_disk(req: SaveSolutionRequest):
    """Guarda la solución del reto directamente en el archivo reto.py del workspace local."""
    course_folders = {
        1: "01-fundamentos-python",
        2: "02-algoritmos-estructuras",
        3: "03-agentes-ia",
        4: "04-proyecto-final"
    }
    folder = course_folders.get(req.course_num)
    if not folder:
        raise HTTPException(status_code=400, detail="Curso no válido")
    
    class_prefix = f"clase-{req.class_num:02d}"
    course_path = os.path.join(os.getcwd(), folder)
    if not os.path.exists(course_path):
        return {"success": False, "message": "Directorio de curso no encontrado en el workspace actual"}
        
    target_dir = None
    for entry in os.listdir(course_path):
        if entry.startswith(class_prefix) and os.path.isdir(os.path.join(course_path, entry)):
            target_dir = os.path.join(course_path, entry)
            break
            
    if not target_dir:
        return {"success": False, "message": "Carpeta de clase no encontrada"}
        
    reto_path = os.path.join(target_dir, "ejercicios", "reto.py")
    os.makedirs(os.path.dirname(reto_path), exist_ok=True)
    with open(reto_path, "w", encoding="utf-8") as f:
        f.write(req.code)
        
    return {
        "success": True, 
        "path": reto_path, 
        "rel_path": os.path.relpath(reto_path, os.getcwd()),
        "message": f"Solución guardada exitosamente en {os.path.relpath(reto_path, os.getcwd())}"
    }

@app.post("/api/quiz/evaluate")
def evaluate_quiz(req: QuizEvaluateRequest):
    """Evalúa la respuesta a una pregunta del micro-quiz de la clase y otorga XP."""
    content = TutorEngine.get_class_content(req.course_num, req.class_num)
    if not content or "quiz" not in content:
        raise HTTPException(status_code=404, detail="Quiz no disponible para esta clase")
    quizzes = content.get("quiz", [])
    if req.question_idx < 0 or req.question_idx >= len(quizzes):
        raise HTTPException(status_code=400, detail="Índice de pregunta inválido")
        
    q_item = quizzes[req.question_idx]
    is_correct = (req.selected_idx == q_item["correct_index"])
    
    reward = {}
    if is_correct:
        reward = gamification.add_xp(25, f"Micro-Quiz C{req.course_num}-S{req.class_num:02d}")
        
    return {
        "correct": is_correct,
        "explanation": q_item.get("explanation", ""),
        "xp_awarded": 25 if is_correct else 0,
        "profile": gamification.profile.model_dump() if is_correct else None
    }

@app.post("/api/ask-mentor")
def ask_mentor(req: AskMentorRequest):
    """Procesa consultas pedagógicas socráticas y ofrece orientación contextual basada en la metáfora central."""
    q = req.question.lower().strip()
    class_info = TutorEngine.get_class_content(req.course_num, req.class_num) or {}
    metaphor = class_info.get("metaphor", "Las Cajas y Procesos")
    title = class_info.get("title", "Fundamentos")
    
    if "error" in q or "falla" in q or "no funciona" in q:
        reply = f"🔍 **Diagnóstico del Mentor:** Revisa primero los tipos de datos de entrada y retorno. En *{title}*, asegúrate de que tu lógica retorne exactamente lo especificado en el reto sin alterar el nombre de la función ni los type hints."
    elif "memoria" in q or "heap" in q or "stack" in q or "id" in q:
        reply = f"🔬 **Modelo de Memoria (Wisrovi):** Recuerda que las variables son etiquetas apuntando a posiciones en la memoria RAM (*{metaphor}*). Si reasignas una variable inmutable (como int o str), Python crea una nueva caja en otra dirección hex."
    elif "pista" in q or "ayuda" in q or "como empiezo" in q:
        hints = class_info.get("socratic_hints", [])
        hint_text = hints[0] if hints else "Divide el problema en pasos pequeños: 1) Entradas, 2) Transformación, 3) Retorno."
        reply = f"💡 **Guía Socrática:** {hint_text}"
    elif "metáfora" in q or "metafora" in q or "explicación" in q or "que es" in q:
        reply = f"🌟 **Metáfora Didáctica:** Para esta clase, visualizamos: *«{metaphor}»*. Piensa en cómo los datos fluyen a través de esta metáfora para estructurar tu algoritmo."
    else:
        reply = f"🚀 **Consejo de Arquitectura:** En *{title}*, el 70% del aprendizaje ocurre al depurar tu propio código (*La Regla de la Bicicleta*). Analiza la aserción que falla y prueba tu función con valores de prueba en el Arenero."
        
    return {
        "reply": reply,
        "metaphor": metaphor,
        "timestamp": "now"
    }

@app.get("/api/curriculum")
def get_curriculum():
    """Retorna el árbol curricular completo con las 32 clases y el estado de desbloqueo secuencial."""
    classes = TutorEngine.get_all_classes_summary()
    completed_set = set(gamification.profile.completed_classes)
    
    for c in classes:
        c["completed"] = c["key"] in completed_set
        c["available"] = gamification.is_class_unlocked(c["course_num"], c["class_num"])
        
    total_classes = len(classes)
    completed_count = sum(1 for c in classes if c["completed"])
    pct = int((completed_count / total_classes) * 100) if total_classes else 0
    
    return {
        "classes": classes,
        "total_classes": total_classes,
        "completed_count": completed_count,
        "progress_percent": pct
    }

@app.get("/api/class/{course_num}/{class_num}")
def get_class_detail(course_num: int, class_num: int):
    """Retorna los contenidos didácticos, metáforas, código, quiz, tips pythonic y reto de una clase."""
    if not gamification.is_class_unlocked(course_num, class_num):
        raise HTTPException(
            status_code=403,
            detail=f"🔒 Clase C{course_num}-S{class_num:02d} bloqueada. Para acceder a esta lección, completa primero las clases anteriores en orden secuencial."
        )
    content = TutorEngine.get_class_content(course_num, class_num)
    if not content:
        raise HTTPException(status_code=404, detail="Clase no encontrada")
        
    key = f"{course_num}-{class_num}"
    res = dict(content)
    res["is_completed"] = key in gamification.profile.completed_classes
    res["is_review_mode"] = key in gamification.profile.completed_classes
    return res

@app.get("/api/tutor/class/{course_num}/{class_num}")
def get_tutor_class_detail(course_num: int, class_num: int):
    """
    Retorna los contenidos didácticos en Modo Maestro (Instructor/Presenter).
    Acceso directo a las 32 clases sin bloqueo de gamificación estudiantil,
    incluyendo notas pedagógicas del mentor para la clase en vivo.
    """
    content = TutorEngine.get_class_content(course_num, class_num)
    if not content:
        raise HTTPException(status_code=404, detail="Clase no encontrada")
        
    res = dict(content)
    res["is_unlocked"] = True
    res["instructor_mode"] = True
    res["speaker_notes"] = {
        "metaphor_story": f"Comienza explicando: «{content['metaphor']}». Pide a los alumnos que imaginen los datos en memoria.",
        "interactive_questions": [
            f"¿Qué ocurre en el Heap cuando reasignamos una variable inmutable en {content['title']}?",
            "¿Por qué es preferible usar contratos de tipado estrictos frente a tipado implícito?",
            "¿Qué caso borde creen que rompería este algoritmo si no validamos las entradas?"
        ],
        "common_pitfalls": content.get("pythonic_tip", {}).get("antipattern", "No validar tipos de entrada.")
    }
    return res

@app.post("/api/run-code")
def run_code(req: RunCodeRequest):
    """Ejecuta código de forma interactiva y retorna salida y visualización de memoria."""
    result = CodeRunner.run_code(req.code)
    gamification.unlock_badge("first_code")
    if result.get("memory_variables"):
        gamification.unlock_badge("memory_master")
    return result

@app.post("/api/evaluate-challenge")
def evaluate_challenge(req: EvaluateChallengeRequest):
    """Evalúa el reto práctico en vivo con tests unitarios y otorga recompensas de XP y diploma de clase."""
    eval_result = CodeRunner.evaluate_challenge(req.course_num, req.class_num, req.code)
    
    reward_info = {}
    class_cert_payload = None
    if eval_result.get("passed"):
        reward_info = gamification.complete_class(req.course_num, req.class_num, elapsed_seconds=req.elapsed_seconds)
        
        # Desbloqueo de insignias de graduación
        c_done = [c for c in gamification.profile.completed_classes if c.startswith(f"{req.course_num}-")]
        if len(c_done) >= 8:
            badge_map = {1: "c1_graduate", 2: "c2_graduate", 3: "c3_graduate", 4: "c4_graduate"}
            if req.course_num in badge_map:
                gamification.unlock_badge(badge_map[req.course_num])
                
        # Generar datos y vista previa del diploma de la clase
        student_name = gamification.profile.name or "Estudiante Wisrovi"
        class_cert_payload = CertificateGenerator.get_class_share_payload(
            student_name=student_name,
            course_num=req.course_num,
            class_num=req.class_num
        )
                
    return {
        "evaluation": eval_result,
        "reward": reward_info,
        "class_certificate": class_cert_payload,
        "profile": gamification.profile.model_dump()
    }

@app.post("/api/certificate/class/preview")
def preview_class_certificate(req: ClassCertificateRequest):
    """Genera los datos y vista previa HTML del diploma de una clase."""
    payload = CertificateGenerator.get_class_share_payload(
        student_name=req.student_name or gamification.profile.name or "Estudiante Wisrovi",
        course_num=req.course_num,
        class_num=req.class_num
    )
    return {
        "success": True,
        "data": payload
    }

@app.get("/api/certificate/class/download")
def download_class_certificate(
    course_num: int,
    class_num: int,
    student_name: str = "Estudiante Wisrovi",
    export_format: str = "pdf"
):
    """Compila y descarga el diploma oficial de la clase en PDF o PNG."""
    import tempfile
    clean_name = student_name.replace(" ", "_").replace("/", "_")
    
    if export_format.lower() == "png":
        temp_png = os.path.join(tempfile.gettempdir(), f"diploma_c{course_num}_s{class_num}_{abs(hash(student_name))}.png")
        CertificateGenerator.generate_class_certificate_png(
            student_name=student_name,
            course_num=course_num,
            class_num=class_num,
            output_png_path=temp_png
        )
        if os.path.exists(temp_png):
            return FileResponse(
                temp_png,
                media_type="image/png",
                filename=f"Diploma_Wisrovi_C{course_num}_Clase{class_num:02d}_{clean_name}.png"
            )
    else:
        temp_pdf = os.path.join(tempfile.gettempdir(), f"diploma_c{course_num}_s{class_num}_{abs(hash(student_name))}.pdf")
        CertificateGenerator.generate_class_certificate_pdf(
            student_name=student_name,
            course_num=course_num,
            class_num=class_num,
            output_pdf_path=temp_pdf
        )
        if os.path.exists(temp_pdf):
            return FileResponse(
                temp_pdf,
                media_type="application/pdf",
                filename=f"Diploma_Wisrovi_C{course_num}_Clase{class_num:02d}_{clean_name}.pdf"
            )
            
    raise HTTPException(status_code=500, detail="Error al compilar el diploma de clase")

@app.post("/api/certificate/generate")
def generate_certificate(req: CertificateRequest):
    """Genera la vista previa HTML oficial del diploma de certificación de curso."""
    html_content = CertificateGenerator.generate_html(
        student_name=req.student_name,
        course_title=req.course_title,
        hours=req.hours
    )
    return {
        "success": True,
        "html": html_content
    }

@app.get("/api/certificate/download")
def download_certificate(student_name: str = "Estudiante Wisrovi", course_title: str = "Programa Integral de Formación en Python", hours: int = 160):
    """Compila y descarga el PDF oficial de certificación con Google Chrome Headless."""
    import tempfile
    temp_pdf = os.path.join(tempfile.gettempdir(), f"certificado_{abs(hash(student_name))}.pdf")
    CertificateGenerator.generate_pdf(
        student_name=student_name,
        output_pdf_path=temp_pdf,
        course_title=course_title,
        hours=hours
    )
    if os.path.exists(temp_pdf):
        return FileResponse(
            temp_pdf,
            media_type="application/pdf",
            filename=f"Certificado_Wisrovi_{student_name.replace(' ', '_')}.pdf"
        )
    raise HTTPException(status_code=500, detail="Error al compilar el certificado PDF")

# Servir Frontend UI en Modo Estudiante o Modo Presentador Tutor
@app.get("/")
def serve_ui(mode: Optional[str] = "student", course: Optional[int] = None, class_num: Optional[int] = None):
    """Servicio de la interfaz Single Page Application embebida."""
    return HTMLResponse(get_embedded_html())

@app.get("/tutor")
@app.get("/presenter")
def serve_tutor():
    """Servicio de la interfaz en Modo Presentador / Docente en Vivo."""
    return HTMLResponse(get_embedded_html())

# Montar archivos estáticos opcionales si existen
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

def start_server(host: str = "127.0.0.1", port: int = 8501):
    """Inicia el servidor web Uvicorn."""
    uvicorn.run(app, host=host, port=port, log_level="info")

if __name__ == "__main__":
    start_server()
