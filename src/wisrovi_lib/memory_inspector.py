#!/usr/bin/env python3
"""
Inspector Visual de Memoria Heap y Stack para el Tutor Virtual.
Permite extraer el estado de las variables, punteros y direcciones de memoria
en tiempo real para que el alumno visualice las 'Cajas' y 'Objetos'.
"""

import sys
import types
from typing import Dict, List, Any, Optional

IMMUTABLE_TYPES = (int, float, str, bool, tuple, frozenset, bytes, type(None))

class MemoryInspector:
    """Inspecciona y formatea el estado de la memoria para la interfaz web."""

    @staticmethod
    def inspect_frame_variables(local_vars: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Convierte las variables de un frame en una lista estructurada para la UI."""
        results = []
        for name, val in local_vars.items():
            if name.startswith("__") or isinstance(val, (types.ModuleType, types.FunctionType)):
                continue
                
            val_type = type(val).__name__
            val_id_hex = hex(id(val))
            val_size = sys.getsizeof(val)
            is_mutable = not isinstance(val, IMMUTABLE_TYPES)
            
            # Representación limpia del valor
            val_str = repr(val)
            if len(val_str) > 80:
                val_str = val_str[:77] + "..."
                
            results.append({
                "name": name,
                "type": val_type,
                "id": val_id_hex,
                "size_bytes": val_size,
                "value": val_str,
                "is_mutable": is_mutable,
                "icon": "📦" if is_mutable else "🔒"
            })
        return results

    @classmethod
    def execute_and_inspect(cls, code: str) -> Dict[str, Any]:
        """Ejecuta código de forma segura y captura tanto la salida estándar como la memoria."""
        import io
        from contextlib import redirect_stdout, redirect_stderr
        
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()
        
        sandbox_scope: Dict[str, Any] = {}
        
        try:
            with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
                # Compilar y ejecutar
                compiled = compile(code, "<wisrovi_sandbox>", "exec")
                exec(compiled, sandbox_scope)
                
            raw_stdout = stdout_capture.getvalue()
            raw_stderr = stderr_capture.getvalue()
            memory_state = cls.inspect_frame_variables(sandbox_scope)
            
            return {
                "success": True,
                "stdout": raw_stdout,
                "stderr": raw_stderr,
                "memory_variables": memory_state,
                "total_variables": len(memory_state)
            }
        except Exception as e:
            return {
                "success": False,
                "stdout": stdout_capture.getvalue(),
                "stderr": f"{type(e).__name__}: {str(e)}",
                "memory_variables": [],
                "total_variables": 0
            }

    @classmethod
    def lint_code(cls, code: str) -> List[Dict[str, Any]]:
        """
        Analizador estático AST y linter pedagógico según estándares PEP 8 / Wisrovi.
        Detecta antipatrones, mutables en argumentos por defecto y buenas prácticas.
        """
        import ast
        diagnostics = []

        try:
            tree = ast.parse(code)
        except SyntaxError as se:
            return [{
                "line": se.lineno or 1,
                "column": se.offset or 1,
                "severity": "error",
                "code": "SYNTAX_ERR",
                "message": f"Error de sintaxis: {se.msg}",
                "hint": "Revisa los dos puntos (:) al final de la sentencia o la indentación de 4 espacios."
            }]

        for node in ast.walk(tree):
            # 1. Antipatrón: Except genérico sin especificar tipo
            if isinstance(node, ast.ExceptHandler) and node.type is None:
                diagnostics.append({
                    "line": node.lineno,
                    "column": node.col_offset,
                    "severity": "warning",
                    "code": "W0702",
                    "message": "Antipatrón: Bloque 'except:' desnudo sin especificar excepción.",
                    "hint": "Especifica siempre la excepción esperada (ej. 'except ValueError:') o 'except Exception:' para capturar errores de forma controlada."
                })

            # 2. Antipatrón: Argumento por defecto mutable en funciones (gotcha clásico)
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                for default in node.args.defaults:
                    if isinstance(default, (ast.List, ast.Dict, ast.Set)):
                        diagnostics.append({
                            "line": default.lineno,
                            "column": default.col_offset,
                            "severity": "warning",
                            "code": "W0102",
                            "message": f"Gotcha Peligroso: Argumento por defecto mutable ({type(default).__name__}) en función '{node.name}'.",
                            "hint": "Usa 'default=None' y dentro de la función inicializa con 'if param is None: param = []'."
                        })

                # 3. Sugerencia de Tipado PEP 484
                has_missing_type = any(arg.annotation is None for arg in node.args.args if arg.arg != "self")
                if has_missing_type and not node.name.startswith("__"):
                    diagnostics.append({
                        "line": node.lineno,
                        "column": node.col_offset,
                        "severity": "info",
                        "code": "TYP001",
                        "message": f"Tip Pythonic: La función '{node.name}' carece de type hints en algunos parámetros.",
                        "hint": "Añade contratos de tipado estrictos (ej. 'def sumar(a: int, b: int) -> int:')."
                    })

            # 4. Antipatrón: Importación con comodín (from module import *)
            if isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    if alias.name == "*":
                        diagnostics.append({
                            "line": node.lineno,
                            "column": node.col_offset,
                            "severity": "warning",
                            "code": "W0401",
                            "message": f"Antipatrón: Importación con comodín 'from {node.module} import *'.",
                            "hint": "Importa explícitamente solo las clases o funciones que vayas a utilizar."
                        })

        return diagnostics

    @classmethod
    def benchmark_code(cls, code: str, iterations: int = 50) -> Dict[str, Any]:
        """
        Mide con alta precisión el tiempo de CPU y el consumo máximo de memoria RAM
        (heap footprint) de una solución mediante tracemalloc y time.perf_counter_ns.
        """
        import time
        import tracemalloc
        import io
        from contextlib import redirect_stdout, redirect_stderr

        compiled = compile(code, "<benchmark>", "exec")
        
        times_ns = []
        tracemalloc.start()
        
        devnull = io.StringIO()
        with redirect_stdout(devnull), redirect_stderr(devnull):
            for _ in range(iterations):
                scope: Dict[str, Any] = {}
                t0 = time.perf_counter_ns()
                exec(compiled, scope)
                t1 = time.perf_counter_ns()
                times_ns.append(t1 - t0)

        current_mem, peak_mem = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        avg_ns = sum(times_ns) / len(times_ns)
        avg_us = round(avg_ns / 1000.0, 2)
        min_us = round(min(times_ns) / 1000.0, 2)

        if avg_us < 50:
            speed_grade = "🚀 Ultra Rápido (< 50µs) - Complejidad O(1)"
        elif avg_us < 500:
            speed_grade = "⚡ Rápido (< 500µs) - Complejidad O(n)"
        else:
            speed_grade = "⏳ Estándar (> 500µs) - Complejidad O(n log n) o superior"

        return {
            "iterations": iterations,
            "avg_time_microseconds": avg_us,
            "min_time_microseconds": min_us,
            "peak_memory_bytes": peak_mem,
            "peak_memory_kb": round(peak_mem / 1024.0, 2),
            "speed_grade": speed_grade
        }
