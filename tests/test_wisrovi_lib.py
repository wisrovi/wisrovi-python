#!/usr/bin/env python3
"""
Tests automatizados exhaustivos para wisrovi_lib:
- Gamificación y Perfil RPG
- Inspector de Memoria Dual (Stack vs Heap)
- Evaluador de Código y Contratos de las 32 Clases de los 4 Cursos
- Generador de Certificados y Diplomas Oficiales
- Motor de Currículo y Metáforas Pedagógicas
- Interfaz Embebida HTML
"""

import os
import sys
import tempfile
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from wisrovi_lib import (
    GamificationEngine,
    StudentProfile,
    MemoryInspector,
    CodeRunner,
    CertificateGenerator,
    TutorEngine,
)
from wisrovi_lib.embedded_ui import get_embedded_html

def test_gamification_engine():
    temp_dir = tempfile.mkdtemp()
    profile_path = os.path.join(temp_dir, "test_profile.json")
    
    engine = GamificationEngine(profile_path=profile_path)
    assert engine.profile.xp == 0
    assert engine.profile.level == 1
    
    # Añadir XP
    res = engine.add_xp(600, "Superó reto 1")
    assert res["level"] == 2
    assert "Explorador" in res["level_title"]
    
    # Desbloquear Insignia
    badge = engine.unlock_badge("first_code")
    assert badge is not None
    assert "first_code" in engine.profile.unlocked_badges
    
    # Completar clase
    c_res = engine.complete_class(1, 1)
    assert c_res["success"] is True
    assert "1-1" in engine.profile.completed_classes

def test_memory_inspector():
    code = """
x = 42
nombre = 'Wisrovi'
lista = [1, 2, 3]
"""
    res = MemoryInspector.execute_and_inspect(code)
    assert res["success"] is True
    assert res["total_variables"] == 3
    
    var_names = [v["name"] for v in res["memory_variables"]]
    assert "x" in var_names
    assert "nombre" in var_names
    assert "lista" in var_names
    
    # Verificar mutabilidad
    list_var = next(v for v in res["memory_variables"] if v["name"] == "lista")
    assert list_var["is_mutable"] is True
    
    str_var = next(v for v in res["memory_variables"] if v["name"] == "nombre")
    assert str_var["is_mutable"] is False

def test_certificate_generator():
    html = CertificateGenerator.generate_html(
        student_name="Alejandro Martinez",
        course_title="Curso 1: Fundamentos Basicos de Python",
        hours=40
    )
    assert "Alejandro Martinez" in html
    assert "Curso 1: Fundamentos Basicos de Python" in html
    assert "WISROVI ACADEMY" in html
    assert "ID Hash:" in html

def test_tutor_engine_all_32_classes():
    summary = TutorEngine.get_all_classes_summary()
    assert len(summary) == 32, f"Se esperaban 32 clases, obtenido {len(summary)}"
    
    # Validar 8 clases por cada curso
    for course_id in range(1, 5):
        course_classes = [c for c in summary if c["course_num"] == course_id]
        assert len(course_classes) == 8, f"Curso {course_id} debe tener 8 clases"
        
        for class_id in range(1, 9):
            content = TutorEngine.get_class_content(course_id, class_id)
            assert content is not None, f"Contenido de Clase {course_id}-{class_id} no debe ser None"
            assert content["course_num"] == course_id
            assert content["class_num"] == class_id
            assert len(content["title"]) > 0
            assert len(content["metaphor"]) > 0
            assert len(content["theory"]) > 0
            assert len(content["mermaid"]) > 0
            assert len(content["demo_code"]) > 0
            assert len(content["playground_code"]) > 0
            assert len(content["challenge_prompt"]) > 0
            assert len(content["challenge_starter"]) > 0
            assert len(content["socratic_hints"]) >= 2
            if class_id == 8:
                assert content["boss_battle"] is True

def test_all_32_challenge_evaluations():
    """Valida que los challenge_starter de las 32 clases cumplan satisfactoriamente sus evaluaciones."""
    for course_id in range(1, 5):
        for class_id in range(1, 9):
            content = TutorEngine.get_class_content(course_id, class_id)
            starter_code = content["challenge_starter"]
            
            # Evaluar con CodeRunner
            eval_res = CodeRunner.evaluate_challenge(course_id, class_id, starter_code)
            assert eval_res["passed"] is True, f"Fallo en evaluación de Clase {course_id}-{class_id}: {eval_res.get('output')} | Pista: {eval_res.get('socratic_hint')}"
            assert eval_res["score"] == 100

def test_embedded_ui_html():
    html = get_embedded_html()
    assert "<!DOCTYPE html>" in html
    assert "Wisrovi Academy" in html
    assert "midnight" in html
    assert "course-tabs-bar" in html
    assert "memory-board-dual" in html
    assert "ask-mentor-modal" in html

def test_format_code_ast():
    import ast
    bad_code = "def foo( x , y ):\n    return x + y"
    parsed = ast.parse(bad_code)
    formatted = ast.unparse(parsed)
    assert "def foo(x, y):" in formatted
    assert "return x + y" in formatted

def test_sequential_progression_and_review_mode(tmp_path):
    prof_file = tmp_path / "student_profile.json"
    engine = GamificationEngine(profile_path=str(prof_file))
    
    # 1. Al inicio, solo C1-S01 está desbloqueada
    assert engine.is_class_unlocked(1, 1) is True
    assert engine.is_class_unlocked(1, 2) is False
    assert engine.is_class_unlocked(1, 5) is False
    assert engine.is_class_unlocked(2, 1) is False
    assert engine.is_course_unlocked(1) is True
    assert engine.is_course_unlocked(2) is False
    
    # 2. El estudiante completa 1-1
    engine.complete_class(1, 1)
    # Ahora 1-1 está desbloqueada (modo repaso/práctica) y 1-2 está desbloqueada (activa)
    assert engine.is_class_unlocked(1, 1) is True
    assert engine.is_class_unlocked(1, 2) is True
    assert engine.is_class_unlocked(1, 3) is False
    
    # 3. Completa 1-2 hasta 1-7
    for c in range(2, 8):
        engine.complete_class(1, c)
    
    # 1-8 está desbloqueada, pero Curso 2 aún no
    assert engine.is_class_unlocked(1, 8) is True
    assert engine.is_class_unlocked(2, 1) is False
    assert engine.is_course_unlocked(2) is False
    
    # Puede volver a repasar la 1-1, 1-3, 1-5 libremente
    assert engine.is_class_unlocked(1, 1) is True
    assert engine.is_class_unlocked(1, 3) is True
    assert engine.is_class_unlocked(1, 5) is True
    
    # 4. Completa 1-8 (finaliza Curso 1)
    engine.complete_class(1, 8)
    # Ahora Curso 2 y 2-1 están desbloqueados
    assert engine.is_course_unlocked(2) is True
    assert engine.is_class_unlocked(2, 1) is True
    assert engine.is_class_unlocked(2, 2) is False

def test_dynamic_speed_xp_bonus(tmp_path):
    prof_file = tmp_path / "student_profile.json"
    engine = GamificationEngine(profile_path=str(prof_file))
    
    # Rápido (< 5 min / 120s): Base 150 + 50 = 200 XP
    res_fast = engine.complete_class(1, 1, elapsed_seconds=120)
    assert res_fast["total_xp"] == 200
    assert res_fast["speed_bonus"] == 50
    assert "speedster" in engine.profile.unlocked_badges
    
    # Óptimo (5 a 15 min / 600s): Base 150 + 25 = 175 XP
    res_opt = engine.complete_class(1, 2, elapsed_seconds=600)
    assert res_opt["total_xp"] == 175
    assert res_opt["speed_bonus"] == 25
    
    # Estándar (15 a 30 min / 1200s): Base 150 + 0 = 150 XP
    res_std = engine.complete_class(1, 3, elapsed_seconds=1200)
    assert res_std["total_xp"] == 150
    assert res_std["speed_bonus"] == 0
    
def test_tutor_mode_api_and_speaker_notes():
    """Valida los endpoints del Modo Maestro/Tutor y la entrega de Speaker Notes para el docente."""
    from wisrovi_lib.server import get_tutor_class_detail, serve_tutor
    
    # 1. Validar endpoint de clase en Modo Maestro (sin bloqueo de gamificación)
    data = get_tutor_class_detail(course_num=3, class_num=1)
    assert data["is_unlocked"] is True
    assert data["instructor_mode"] is True
    assert "speaker_notes" in data
    assert "metaphor_story" in data["speaker_notes"]
    assert len(data["speaker_notes"]["interactive_questions"]) >= 3
    assert len(data["speaker_notes"]["common_pitfalls"]) > 0
    
    # 2. Validar entrega de HTML en Modo Presentador / Docente
    res_tutor = serve_tutor()
    assert res_tutor.status_code == 200
    assert "<!DOCTYPE html>" in res_tutor.body.decode("utf-8")

def test_save_solution_to_disk():
    """Valida el guardado automático de retos en el archivo local ejercicios/reto.py."""
    from wisrovi_lib.server import save_solution_to_disk, SaveSolutionRequest
    
    req = SaveSolutionRequest(
        course_num=1,
        class_num=1,
        code="# Solución generada en Wisrovi Studio\nprint('Hola Mundo')\n"
    )
    res = save_solution_to_disk(req)
    assert res["success"] is True
    assert "reto.py" in res["path"]

def test_slide_deck_and_resizer_markup():
    """Valida que los nuevos elementos de Diapositivas, Resizer y Guardar en Disco existan en el HTML."""
    from wisrovi_lib.embedded_ui import get_embedded_html
    html = get_embedded_html()
    assert "slide-deck-modal" in html
    assert "slide-deck-btn" in html
    assert "docs-resize-handle" in html
    assert "save-reto-disk-btn" in html

def test_class_certificates_all_32_classes():
    """Valida que existan los 32 diplomas de clase con competencias, conceptos y textos de LinkedIn."""
    from wisrovi_lib.certificate import CLASS_CERTIFICATES, CertificateGenerator
    
    assert len(CLASS_CERTIFICATES) == 32
    for course_num in range(1, 5):
        for class_num in range(1, 9):
            key = f"{course_num}-{class_num}"
            assert key in CLASS_CERTIFICATES, f"Falta diploma de clase {key}"
            info = CertificateGenerator.get_class_info(course_num, class_num)
            assert len(info["title"]) > 5
            assert len(info["skill"]) > 5
            assert len(info["concept"]) > 10
            assert "linkedin_text" in info
            assert "@Wisrovi" in info["linkedin_text"]
            
            # Validar render HTML
            html = CertificateGenerator.generate_class_certificate_html(
                student_name="Alexander Fleming",
                course_num=course_num,
                class_num=class_num
            )
            assert "Alexander Fleming" in html
            assert info["title"] in html
            assert "WISROVI ACADEMY" in html
            assert "ID Hash:" in html

def test_class_certificate_share_payload():
    """Valida el paquete de metadatos de LinkedIn para compartir micro-acreditaciones."""
    payload = CertificateGenerator.get_class_share_payload(
        student_name="Elena Gomez",
        course_num=1,
        class_num=2
    )
    assert payload["student_name"] == "Elena Gomez"
    assert "Tipado Estático" in payload["title"]
    assert "linkedin.com/sharing/share-offsite" in payload["linkedin_intent_url"]
    assert "<!DOCTYPE html>" in payload["html"]

def test_class_certificate_modal_in_embedded_ui():
    """Valida que el modal de diplomas de clase y sus controles existan en la interfaz embebida."""
    html = get_embedded_html()
    assert "class-cert-modal" in html
    assert "download-class-pdf-btn" in html
    assert "download-class-png-btn" in html
    assert "share-linkedin-direct-btn" in html
    assert "class-cert-linkedin-text" in html

def test_class_certificate_server_api():
    """Valida los endpoints REST de diplomas de clase."""
    from wisrovi_lib.server import preview_class_certificate, ClassCertificateRequest
    
    req = ClassCertificateRequest(course_num=3, class_num=4, student_name="Carlos Mendez")
    res = preview_class_certificate(req)
    assert res["success"] is True
    assert "Tool Calling" in res["data"]["title"]
    assert "Carlos Mendez" in res["data"]["html"]



