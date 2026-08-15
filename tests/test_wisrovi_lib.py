#!/usr/bin/env python3
"""
Tests automatizados para el ecosistema wisrovi_lib (Gamificación, Memoria, Certificados y Tutor).
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

def test_code_runner_evaluation():
    # Código correcto
    good_code = """
def evaluar_estudiante(nombre: str, edad: int) -> str:
    return "Mayor de edad" if edad >= 18 else "Menor de edad"
"""
    res = CodeRunner.run_code(good_code)
    assert res["success"] is True

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

def test_tutor_engine_curriculum():
    summary = TutorEngine.get_all_classes_summary()
    assert len(summary) >= 3
    
    c1 = TutorEngine.get_class_content(1, 1)
    assert c1 is not None
    assert "Megáfono" in c1["metaphor"]
    assert "demo_code" in c1
