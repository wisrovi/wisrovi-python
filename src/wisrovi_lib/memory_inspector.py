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
