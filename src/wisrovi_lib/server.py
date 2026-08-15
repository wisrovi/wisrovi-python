#!/usr/bin/env python3
"""
Servidor Web FastAPI y API REST del Tutor Virtual Interactivo (Wisrovi Academy).
Expone endpoints para ejecutar código, evaluar retos, consultar memoria y generar certificados.
"""

import os
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from typing import Dict, Any, Optional

from .gamification import GamificationEngine, StudentProfile
from .tutor_engine import TutorEngine
from .code_runner import CodeRunner
from .certificate import CertificateGenerator

app = FastAPI(
    title="Wisrovi Academy - Virtual AI Tutor",
    description="Plataforma de tutoría interactiva, gamificación y certificación.",
    version="1.0.0"
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

class UpdateProfileRequest(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

class CertificateRequest(BaseModel):
    student_name: str
    course_title: Optional[str] = "Programa Integral de Formación en Python: De Cero a Agentes de IA"
    hours: Optional[int] = 160

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

@app.get("/api/curriculum")
def get_curriculum():
    """Retorna la lista de todas las clases y su estado de compleción."""
    summary = TutorEngine.get_all_classes_summary()
    completed = set(gamification.profile.completed_classes)
    
    for item in summary:
        key = f"{item['course_num']}-{item['class_num']}"
        item["completed"] = key in completed
        
    return {
        "classes": summary,
        "total_classes": len(summary),
        "completed_count": len(completed),
        "progress_percent": int((len(completed) / max(len(summary), 1)) * 100)
    }

@app.get("/api/class/{course_num}/{class_num}")
def get_class_detail(course_num: int, class_num: int):
    """Retorna los contenidos didácticos, metáforas, código y reto de una clase."""
    content = TutorEngine.get_class_content(course_num, class_num)
    if not content:
        raise HTTPException(status_code=404, detail="Clase no encontrada")
    return content

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
    """Evalúa el reto del estudiante, corre las pruebas y otorga XP e insignias."""
    eval_res = CodeRunner.evaluate_challenge(req.course_num, req.class_num, req.code)
    
    xp_info = None
    if eval_res["passed"]:
        xp_info = gamification.complete_class(req.course_num, req.class_num)
        
    return {
        "evaluation": eval_res,
        "gamification": xp_info,
        "profile": gamification.profile.model_dump()
    }

@app.post("/api/certificate/generate")
def generate_certificate(req: CertificateRequest):
    """Genera el certificado oficial en HTML y PDF."""
    html_content = CertificateGenerator.generate_html(
        student_name=req.student_name,
        course_title=req.course_title or "Programa Integral de Formación en Python: De Cero a Agentes de IA",
        hours=req.hours or 160
    )
    
    # Ruta donde se guardará el PDF local del alumno
    output_dir = os.path.expanduser("~/.wisrovi/certificados")
    os.makedirs(output_dir, exist_ok=True)
    pdf_filename = f"certificado_{req.student_name.lower().replace(' ', '_')}.pdf"
    pdf_path = os.path.join(output_dir, pdf_filename)
    
    try:
        CertificateGenerator.generate_pdf(
            student_name=req.student_name,
            output_pdf_path=pdf_path,
            course_title=req.course_title or "Programa Integral de Formación en Python",
            hours=req.hours or 160
        )
        has_pdf = True
    except Exception:
        has_pdf = False
        
    return {
        "success": True,
        "html": html_content,
        "pdf_available": has_pdf,
        "pdf_path": pdf_path if has_pdf else None,
        "badge_markdown": f"[![Wisrovi Certified](https://img.shields.io/badge/Wisrovi%20Academy-Certified%20AI%20Engineer-gold.svg)](https://academy_python.wisrovi.dev)"
    }

# ------------------------------------------------------------------------------
# SERVIR FRONTEND SPA ESTÁTICO
# ------------------------------------------------------------------------------
@app.get("/")
def serve_index():
    index_file = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return {"status": "Wisrovi Virtual Tutor Server Running"}

if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

def start_server(host: str = "127.0.0.1", port: int = 8501):
    """Inicia el servidor web uvicorn."""
    uvicorn.run(app, host=host, port=port, log_level="info")

if __name__ == "__main__":
    start_server()
