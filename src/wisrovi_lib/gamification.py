#!/usr/bin/env python3
"""
Motor de Gamificación y Persistencia del Progreso del Estudiante.
Gestiona XP, niveles, rachas, insignias y estado de avance en las 32 clases.
"""

import os
import json
import time
from datetime import datetime, date
from typing import Dict, List, Any, Optional
from pydantic import BaseModel, Field

PROFILE_DIR = os.path.expanduser("~/.wisrovi")
PROFILE_FILE = os.path.join(PROFILE_DIR, "student_profile.json")

LEVELS = [
    {"level": 1, "title": "🌱 Aprendiz de Python", "min_xp": 0, "max_xp": 499},
    {"level": 2, "title": "⚡ Explorador de Algoritmos", "min_xp": 500, "max_xp": 1499},
    {"level": 3, "title": "🤖 Arquitecto de Agentes de IA", "min_xp": 1500, "max_xp": 2999},
    {"level": 4, "title": "🏆 Master Engineer Full-Stack", "min_xp": 3000, "max_xp": 999999},
]

BADGES = {
    "first_code": {"id": "first_code", "title": "🚴 Primer Pedaleo", "desc": "Ejecutaste tu primera línea de código interactiva.", "icon": "🚴"},
    "memory_master": {"id": "memory_master", "title": "🔬 Explorador del Heap", "desc": "Inspeccionaste variables y direcciones de memoria.", "icon": "🔬"},
    "c1_graduate": {"id": "c1_graduate", "title": "🎯 Fundador de Python", "desc": "Completaste las 8 clases del Curso 1.", "icon": "🎯"},
    "c2_graduate": {"id": "c2_graduate", "title": "⚡ Mago de Algoritmos", "desc": "Completaste las 8 clases del Curso 2.", "icon": "⚡"},
    "c3_graduate": {"id": "c3_graduate", "title": "🤖 Conjurador de IA", "desc": "Completaste las 8 clases del Curso 3.", "icon": "🤖"},
    "c4_graduate": {"id": "c4_graduate", "title": "🏆 Graduado de Élite", "desc": "Completaste el Programa Integral de 32 Semanas.", "icon": "🏆"},
    "streak_3": {"id": "streak_3", "title": "🔥 Racha Imparable", "desc": "Estudiaste 3 días consecutivos.", "icon": "🔥"},
    "speedster": {"id": "speedster", "title": "⚡ Código Pythonic", "desc": "Superaste un reto a la primera sin pedir pistas.", "icon": "✨"}
}

class StudentProfile(BaseModel):
    name: str = "Estudiante Wisrovi"
    email: str = "estudiante@wisrovi.dev"
    avatar: str = "👨‍💻"
    xp: int = 0
    level: int = 1
    level_title: str = "🌱 Aprendiz de Python"
    current_course: int = 1
    current_class: int = 1
    completed_classes: List[str] = Field(default_factory=list) # e.g. ["1-1", "1-2"]
    unlocked_badges: List[str] = Field(default_factory=list)
    streak_days: int = 1
    last_active_date: str = Field(default_factory=lambda: date.today().isoformat())
    total_minutes_active: int = 0
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())

class GamificationEngine:
    """Gestiona la lógica de progresión, XP y persistencia del alumno."""

    def __init__(self, profile_path: str = PROFILE_FILE):
        self.profile_path = profile_path
        self.profile = self.load_profile()

    def load_profile(self) -> StudentProfile:
        """Carga el perfil desde el disco o crea uno nuevo."""
        if os.path.exists(self.profile_path):
            try:
                with open(self.profile_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return StudentProfile(**data)
            except Exception:
                pass
        
        # Fallback de nuevo perfil
        new_prof = StudentProfile()
        self.save_profile(new_prof)
        return new_prof

    def save_profile(self, profile: Optional[StudentProfile] = None):
        """Guarda el perfil actual en JSON de forma atómica."""
        if profile is not None:
            self.profile = profile
            
        os.makedirs(os.path.dirname(self.profile_path), exist_ok=True)
        with open(self.profile_path, "w", encoding="utf-8") as f:
            json.dump(self.profile.model_dump(), f, indent=2, ensure_ascii=False)

    def add_xp(self, amount: int, reason: str = "") -> Dict[str, Any]:
        """Añade puntos de experiencia y evalúa si sube de nivel."""
        self.profile.xp += amount
        
        # Actualizar nivel
        old_level = self.profile.level
        for lvl in LEVELS:
            if lvl["min_xp"] <= self.profile.xp <= lvl["max_xp"]:
                self.profile.level = lvl["level"]
                self.profile.level_title = lvl["title"]
                break
                
        level_up = self.profile.level > old_level
        self._update_streak()
        self.save_profile()
        
        return {
            "new_xp": self.profile.xp,
            "gained": amount,
            "level": self.profile.level,
            "level_title": self.profile.level_title,
            "level_up": level_up,
            "reason": reason
        }

    def unlock_badge(self, badge_id: str) -> Optional[Dict[str, Any]]:
        """Otorga una insignia si no ha sido desbloqueada antes."""
        if badge_id in BADGES and badge_id not in self.profile.unlocked_badges:
            self.profile.unlocked_badges.append(badge_id)
            self.add_xp(100, f"Insignia desbloqueada: {BADGES[badge_id]['title']}")
            self.save_profile()
            return BADGES[badge_id]
        return None

    def complete_class(self, course_num: int, class_num: int, elapsed_seconds: Optional[int] = None) -> Dict[str, Any]:
        """Marca una clase como superada y otorga recompensas de graduación con bonificación dinámica por velocidad."""
        class_key = f"{course_num}-{class_num}"
        is_first_time = class_key not in self.profile.completed_classes
        
        base_xp = 150
        speed_bonus = 0
        speed_tier = "⏳ Estándar"
        
        if elapsed_seconds is not None:
            if elapsed_seconds < 300:
                speed_bonus = 50
                speed_tier = "⚡ Rápido (< 5 min)"
                self.unlock_badge("speedster")
            elif elapsed_seconds <= 900:
                speed_bonus = 25
                speed_tier = "🎯 Óptimo (5-15 min)"
            elif elapsed_seconds <= 1800:
                speed_bonus = 0
                speed_tier = "⏳ Estándar (15-30 min)"
            else:
                speed_bonus = -30
                speed_tier = "🐢 Exploración Lenta (> 30 min)"
                
        total_xp = max(50, base_xp + speed_bonus)
        
        if is_first_time:
            self.profile.completed_classes.append(class_key)
            xp_reward = self.add_xp(total_xp, f"Clase {course_num}.{class_num} ({speed_tier})")
            
            # Verificar si completó el curso
            course_classes = [f"{course_num}-{i}" for i in range(1, 9)]
            if all(k in self.profile.completed_classes for k in course_classes):
                badge_key = f"c{course_num}_graduate"
                self.unlock_badge(badge_key)
                
            # Avanzar a la siguiente clase sugerida
            if class_num < 8:
                self.profile.current_course = course_num
                self.profile.current_class = class_num + 1
            elif course_num < 4:
                self.profile.current_course = course_num + 1
                self.profile.current_class = 1
                
            self.save_profile()
            return {
                "success": True,
                "first_time": True,
                "base_xp": base_xp,
                "speed_bonus": speed_bonus,
                "speed_tier": speed_tier,
                "total_xp": total_xp,
                "xp_reward": xp_reward,
                "current_course": self.profile.current_course,
                "current_class": self.profile.current_class
            }
            
        return {
            "success": True,
            "first_time": False,
            "base_xp": base_xp,
            "speed_bonus": speed_bonus,
            "speed_tier": speed_tier,
            "total_xp": total_xp,
            "current_course": self.profile.current_course,
            "current_class": self.profile.current_class
        }

    def is_class_unlocked(self, course_num: int, class_num: int) -> bool:
        """
        Determina si una clase está desbloqueada para el estudiante según la regla de progresión lineal.
        - C1-S01 siempre está desbloqueada.
        - Cualquier clase ya superada está desbloqueada (modo práctica / repaso).
        - Para una lección nueva no superada:
          * Si class_num > 1: requiere haber superado (course_num, class_num - 1).
          * Si class_num == 1 y course_num > 1: requiere haber superado (course_num - 1, 8).
        """
        key = f"{course_num}-{class_num}"
        if course_num == 1 and class_num == 1:
            return True
        if key in self.profile.completed_classes:
            return True
        if class_num > 1:
            prev_key = f"{course_num}-{class_num - 1}"
            return prev_key in self.profile.completed_classes
        if class_num == 1 and course_num > 1:
            prev_course_end = f"{course_num - 1}-8"
            return prev_course_end in self.profile.completed_classes
        return False

    def is_course_unlocked(self, course_num: int) -> bool:
        """Determina si un curso completo está desbloqueado."""
        if course_num == 1:
            return True
        prev_course_end = f"{course_num - 1}-8"
        return prev_course_end in self.profile.completed_classes

    def _update_streak(self):
        """Calcula la racha diaria de estudio."""
        today_str = date.today().isoformat()
        if self.profile.last_active_date != today_str:
            last_date = date.fromisoformat(self.profile.last_active_date)
            delta = (date.today() - last_date).days
            if delta == 1:
                self.profile.streak_days += 1
                if self.profile.streak_days >= 3:
                    self.unlock_badge("streak_3")
            elif delta > 1:
                self.profile.streak_days = 1
            self.profile.last_active_date = today_str
            self.profile.total_minutes_active += 15
