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
from contextlib import redirect_stdout, redirect_stderr

from .memory_inspector import MemoryInspector

class CodeRunner:
    """Motor de ejecución y evaluación de soluciones de los estudiantes."""

    @staticmethod
    def run_code(code: str) -> Dict[str, Any]:
        """Ejecuta código de forma interactiva y retorna salida y estado de memoria."""
        return MemoryInspector.execute_and_inspect(code)

    @staticmethod
    def evaluate_challenge(course_num: int, class_num: int, student_code: str) -> Dict[str, Any]:
        """
        Evalúa el código del estudiante contra la suite de Pytest de esa clase específica.
        Genera un archivo temporal para el reto, corre el test y captura el resultado con feedback.
        """
        test_file = f"tests/curso_{course_num:02d}/test_clase_{class_num:02d}.py"
        
        # Guardar código del estudiante en un archivo temporal
        with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as temp_script:
            temp_script.write(student_code)
            temp_path = temp_script.name

        try:
            # Ejecutar pytest con el archivo de test
            cmd = [
                sys.executable,
                "-m",
                "pytest",
                "-v",
                test_file
            ]
            
            # Pasamos PYTHONPATH para que encuentre el código
            env = os.environ.copy()
            env["WISROVI_TEMP_RETO"] = temp_path
            
            res = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=15,
                env=env
            )
            
            passed = res.returncode == 0
            
            # Parsear salida
            stdout = res.stdout
            stderr = res.stderr
            
            # Feedback socrático si falla
            socratic_hint = ""
            if not passed:
                socratic_hint = CodeRunner._generate_socratic_hint(stdout, stderr)
                
            return {
                "passed": passed,
                "exit_code": res.returncode,
                "output": stdout if stdout else stderr,
                "socratic_hint": socratic_hint,
                "score": 100 if passed else 0
            }
        except subprocess.TimeoutExpired:
            return {
                "passed": False,
                "exit_code": -1,
                "output": "⏱️ Tiempo de ejecución excedido (Timeout > 15s). Posible bucle infinito.",
                "socratic_hint": "Revisa tus bucles for o while; asegúrate de que la condición de parada se alcance.",
                "score": 0
            }
        except Exception as e:
            return {
                "passed": False,
                "exit_code": -1,
                "output": f"Error del evaluador: {str(e)}",
                "socratic_hint": "Verifica la sintaxis de tu solución antes de evaluar.",
                "score": 0
            }
        finally:
            if os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except Exception:
                    pass

    @staticmethod
    def _generate_socratic_hint(stdout: str, stderr: str) -> str:
        """Extrae la causa raíz del error y la traduce a una pista socrática."""
        full_text = stdout + "\n" + stderr
        if "AssertionError" in full_text:
            return "💡 Pista del Mentor: Una de las aserciones esperaba un valor diferente. Revisa los valores de retorno de tu función y los casos límite (listas vacías, números negativos, ceros)."
        elif "TypeError" in full_text:
            return "💡 Pista del Mentor: Hay una incompatibilidad de tipos (TypeError). Recuerda revisar si estás sumando un string con un int o pasando argumentos incorrectos."
        elif "IndexError" in full_text:
            return "💡 Pista del Mentor: Has intentado acceder a una posición fuera de los límites de la colección (IndexError). Recuerda que los índices en Python empiezan en 0."
        elif "KeyError" in full_text:
            return "💡 Pista del Mentor: La clave no existe en el diccionario (KeyError). Considera usar el método '.get(clave, valor_por_defecto)'."
        elif "SyntaxError" in full_text:
            return "💡 Pista del Mentor: Hay un error de sintaxis en tu código. Revisa los dos puntos (:) al final de tus def/if/for y la indentación."
        return "💡 Pista del Mentor: Revisa la traza de error arriba para identificar la línea exacta que no cumple la prueba."
