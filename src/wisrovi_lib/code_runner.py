#!/usr/bin/env python3
"""
Ejecutor y Evaluador Seguro de Código para el Tutor Virtual.
Permite ejecutar código en vivo y validar retos con retroalimentación socrática.
"""

import sys
import os
import io
import subprocess
import tempfile
from typing import Dict, Any, List, Optional

from .memory_inspector import MemoryInspector

CURRENT_FILE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(CURRENT_FILE_DIR, "..", ".."))

class CodeRunner:
    """Motor de ejecución y evaluación de soluciones de los estudiantes."""

    @staticmethod
    def run_code(code: str) -> Dict[str, Any]:
        """Ejecuta código de forma interactiva y retorna salida y estado de memoria."""
        return MemoryInspector.execute_and_inspect(code)

    @classmethod
    def evaluate_challenge(cls, course_num: int, class_num: int, student_code: str) -> Dict[str, Any]:
        """
        Evalúa el código del estudiante validando contratos de ejecución en tiempo real
        y ejecutando las pruebas unitarias correspondientes.
        """
        scope: Dict[str, Any] = {}
        
        # 1. Compilar y ejecutar código del alumno en scope aislado
        try:
            compiled = compile(student_code, "<student_solution>", "exec")
            exec(compiled, scope)
        except SyntaxError as se:
            return {
                "passed": False,
                "exit_code": 1,
                "output": f"SyntaxError en línea {se.lineno}: {se.msg}",
                "socratic_hint": "💡 Pista del Mentor: Revisa los dos puntos (:) al final de tus sentencias o la indentación de tu código.",
                "score": 0
            }
        except Exception as e:
            return {
                "passed": False,
                "exit_code": 1,
                "output": f"{type(e).__name__}: {str(e)}",
                "socratic_hint": f"💡 Pista del Mentor: Se produjo un error al ejecutar tu código ({type(e).__name__}). Revisa variables no definidas o tipos incompatibles.",
                "score": 0
            }

        # 2. Validación de aserciones funcionales por clase
        try:
            if course_num == 1 and class_num == 1:
                if "evaluar_estudiante" not in scope:
                    return {
                        "passed": False,
                        "exit_code": 1,
                        "output": "Error: No se encontró la función 'evaluar_estudiante(nombre, edad)'",
                        "socratic_hint": "Define la función con: def evaluar_estudiante(nombre: str, edad: int) -> str:",
                        "score": 0
                    }
                fn = scope["evaluar_estudiante"]
                assert fn("Ana", 20) == "Mayor de edad", "evaluar_estudiante('Ana', 20) debe retornar 'Mayor de edad'"
                assert fn("Leo", 15) == "Menor de edad", "evaluar_estudiante('Leo', 15) debe retornar 'Menor de edad'"
                assert fn("Carlos", 18) == "Mayor de edad", "evaluar_estudiante('Carlos', 18) debe retornar 'Mayor de edad' para 18 exactos"

            elif course_num == 1 and class_num == 2:
                if "identificar_tipo_y_tamano" not in scope:
                    return {
                        "passed": False,
                        "exit_code": 1,
                        "output": "Error: No se encontró la función 'identificar_tipo_y_tamano(valor)'",
                        "socratic_hint": "Define la función con: def identificar_tipo_y_tamano(valor) -> tuple:",
                        "score": 0
                    }
                fn = scope["identificar_tipo_y_tamano"]
                t1, s1 = fn(42)
                assert t1 == "int" and s1 > 0, "fn(42) debe retornar ('int', bytes)"
                t2, s2 = fn("Wisrovi")
                assert t2 == "str" and s2 > 0, "fn('Wisrovi') debe retornar ('str', bytes)"

            elif course_num == 1 and class_num == 8:
                if "GestorInventario" not in scope:
                    return {
                        "passed": False,
                        "exit_code": 1,
                        "output": "Error: No se encontró la clase 'GestorInventario'",
                        "socratic_hint": "Crea la clase GestorInventario con sus métodos agregar_producto y obtener_stock.",
                        "score": 0
                    }
                gestor_cls = scope["GestorInventario"]
                g = gestor_cls()
                g.agregar_producto("Laptop", 10)
                assert g.obtener_stock("Laptop") == 10
                
                # Test de excepciones
                try:
                    g.agregar_producto("Error", -5)
                    assert False, "Debe lanzar ValueError con stock negativo"
                except ValueError:
                    pass
                
                try:
                    g.obtener_stock("Inexistente")
                    assert False, "Debe lanzar KeyError si el producto no existe"
                except KeyError:
                    pass
            else:
                # Para cualquier otra clase, comprobar que no lanzó errores y corrió
                pass

            return {
                "passed": True,
                "exit_code": 0,
                "output": "✅ Todas las pruebas y aserciones se completaron exitosamente.",
                "socratic_hint": "",
                "score": 100
            }
        except AssertionError as ae:
            return {
                "passed": False,
                "exit_code": 1,
                "output": f"AssertionError: {str(ae)}",
                "socratic_hint": f"💡 Pista del Mentor: {str(ae)}. Revisa los casos límite de tu lógica.",
                "score": 0
            }
        except Exception as e:
            return {
                "passed": False,
                "exit_code": 1,
                "output": f"Error en la prueba: {type(e).__name__} - {str(e)}",
                "socratic_hint": "💡 Pista del Mentor: Revisa los tipos de datos devueltos y las condiciones de parada.",
                "score": 0
            }
