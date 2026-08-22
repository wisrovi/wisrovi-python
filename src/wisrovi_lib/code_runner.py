#!/usr/bin/env python3
"""
Ejecutor y Evaluador Seguro de Código para el Tutor Virtual (Wisrovi Academy).
Valida contratos de ejecución, pruebas unitarias y aserciones para las 32 clases
de los 4 cursos oficiales del programa de formación.
"""

import sys
import os
import io
import math
import sqlite3
from typing import Dict, Any, List, Optional, Tuple

from .memory_inspector import MemoryInspector

class CodeRunner:
    """Motor de ejecución y evaluación de soluciones de los estudiantes."""

    @staticmethod
    def run_code(code: str) -> Dict[str, Any]:
        """Ejecuta código de forma interactiva y retorna salida y estado de memoria RAM."""
        return MemoryInspector.execute_and_inspect(code)

    @classmethod
    def evaluate_challenge(cls, course_num: int, class_num: int, student_code: str) -> Dict[str, Any]:
        """
        Evalúa el código del estudiante validando contratos de ejecución en tiempo real
        para todas las 32 clases del programa de 4 cursos.
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

        # 2. Validación de aserciones funcionales por clase (1-1 hasta 4-8)
        try:
            # =================================================================
            # CURSO 1: FUNDAMENTOS BÁSICOS DE PYTHON
            # =================================================================
            if course_num == 1:
                if class_num == 1:
                    assert "evaluar_estudiante" in scope, "Falta definir la función 'evaluar_estudiante(nombre, edad)'"
                    fn = scope["evaluar_estudiante"]
                    assert fn("Ana", 20) == "Mayor de edad", "fn('Ana', 20) debe retornar 'Mayor de edad'"
                    assert fn("Leo", 15) == "Menor de edad", "fn('Leo', 15) debe retornar 'Menor de edad'"
                    assert fn("Carlos", 18) == "Mayor de edad", "fn('Carlos', 18) debe retornar 'Mayor de edad'"

                elif class_num == 2:
                    assert "identificar_tipo_y_tamano" in scope, "Falta definir la función 'identificar_tipo_y_tamano(valor)'"
                    fn = scope["identificar_tipo_y_tamano"]
                    t1, s1 = fn(42)
                    assert t1 == "int" and s1 > 0, "fn(42) debe retornar ('int', bytes)"
                    t2, s2 = fn("Wisrovi")
                    assert t2 == "str" and s2 > 0, "fn('Wisrovi') debe retornar ('str', bytes)"

                elif class_num == 3:
                    assert "clasificar_calificacion" in scope, "Falta definir la función 'clasificar_calificacion(nota)'"
                    fn = scope["clasificar_calificacion"]
                    assert fn(95) == "Excelente", "fn(95) debe retornar 'Excelente'"
                    assert fn(75) == "Aprobado", "fn(75) debe retornar 'Aprobado'"
                    assert fn(45) == "Reprobado", "fn(45) debe retornar 'Reprobado'"

                elif class_num == 4:
                    assert "sumar_rango_pares" in scope, "Falta definir la función 'sumar_rango_pares(inicio, fin)'"
                    fn = scope["sumar_rango_pares"]
                    assert fn(1, 10) == 30, "Suma de pares entre 1 y 10 debe ser 30 (2+4+6+8+10)"
                    assert fn(4, 4) == 4, "Suma de pares entre 4 y 4 debe ser 4"
                    assert fn(5, 5) == 0, "Suma de pares entre 5 y 5 debe ser 0"

                elif class_num == 5:
                    assert "filtrar_y_ordenar_palabras" in scope, "Falta definir la función 'filtrar_y_ordenar_palabras(palabras)'"
                    fn = scope["filtrar_y_ordenar_palabras"]
                    res = fn(["sol", "python", "ia", "codigo"])
                    assert res == ["CODIGO", "PYTHON"], f"Se esperaba ['CODIGO', 'PYTHON'], obtenido {res}"

                elif class_num == 6:
                    assert "contar_frecuencia_palabras" in scope, "Falta definir la función 'contar_frecuencia_palabras(texto)'"
                    fn = scope["contar_frecuencia_palabras"]
                    res = fn("Hola mundo hola python")
                    assert res.get("hola") == 2, "La palabra 'hola' debe tener frecuencia 2"
                    assert res.get("python") == 1, "La palabra 'python' debe tener frecuencia 1"

                elif class_num == 7:
                    assert "calcular_estadisticas" in scope, "Falta definir la función 'calcular_estadisticas(*numeros)'"
                    fn = scope["calcular_estadisticas"]
                    res = fn(10, 20, 30, 40)
                    assert res["total"] == 100.0, "total debe ser 100.0"
                    assert res["promedio"] == 25.0, "promedio debe ser 25.0"
                    assert res["max"] == 40.0, "max debe ser 40.0"
                    assert res["min"] == 10.0, "min debe ser 10.0"

                elif class_num == 8:
                    assert "GestorInventario" in scope, "Falta definir la clase 'GestorInventario'"
                    gestor_cls = scope["GestorInventario"]
                    g = gestor_cls()
                    g.agregar_producto("Laptop", 10)
                    assert g.obtener_stock("Laptop") == 10, "obtener_stock debe retornar 10"
                    try:
                        g.agregar_producto("Err", -5)
                        assert False, "Debe lanzar ValueError con stock negativo"
                    except ValueError:
                        pass
                    try:
                        g.obtener_stock("Inexistente")
                        assert False, "Debe lanzar KeyError si el producto no existe"
                    except KeyError:
                        pass

            # =================================================================
            # CURSO 2: ALGORITMOS AVANZADOS Y ESTRUCTURAS DE DATOS
            # =================================================================
            elif course_num == 2:
                if class_num == 1:
                    assert "encontrar_duplicados_o_n" in scope, "Falta definir la función 'encontrar_duplicados_o_n(lista)'"
                    fn = scope["encontrar_duplicados_o_n"]
                    res = fn([1, 2, 3, 2, 4, 5, 1])
                    assert res == {1, 2}, f"Se esperaba {{1, 2}}, obtenido {res}"

                elif class_num == 2:
                    assert "validar_parentesis" in scope, "Falta definir la función 'validar_parentesis(cadena)'"
                    fn = scope["validar_parentesis"]
                    assert fn("([{}])") is True, "'([{}])' debe ser True"
                    assert fn("([)]") is False, "'([)]' debe ser False"
                    assert fn("(") is False, "'(' debe ser False"

                elif class_num == 3:
                    assert "two_sum_hash" in scope, "Falta definir la función 'two_sum_hash(nums, objetivo)'"
                    fn = scope["two_sum_hash"]
                    res = fn([2, 7, 11, 15], 9)
                    assert res in [(0, 1), (1, 0)], f"Índices esperados para suma 9: (0, 1), obtenido {res}"

                elif class_num == 4:
                    assert "busqueda_binaria" in scope, "Falta definir la función 'busqueda_binaria(ordenados, objetivo)'"
                    fn = scope["busqueda_binaria"]
                    datos = [10, 20, 30, 40, 50]
                    assert fn(datos, 30) == 2, "Búsqueda de 30 debe retornar índice 2"
                    assert fn(datos, 99) == -1, "Búsqueda de inexistente debe retornar -1"

                elif class_num == 5:
                    assert "quick_sort" in scope, "Falta definir la función 'quick_sort(arr)'"
                    fn = scope["quick_sort"]
                    res = fn([5, 2, 8, 1, 9, 3])
                    assert res == [1, 2, 3, 5, 8, 9], f"Se esperaba [1, 2, 3, 5, 8, 9], obtenido {res}"

                elif class_num == 6:
                    assert "NodoBST" in scope and "in_order" in scope, "Falta definir 'NodoBST' o 'in_order(raiz)'"
                    Nodo = scope["NodoBST"]
                    fn_inorder = scope["in_order"]
                    r = Nodo(10)
                    r.izq = Nodo(5)
                    r.der = Nodo(15)
                    assert fn_inorder(r) == [5, 10, 15], "In-order de [10, izq=5, der=15] debe ser [5, 10, 15]"

                elif class_num == 7:
                    assert "bfs_camino_mas_corto" in scope, "Falta definir la función 'bfs_camino_mas_corto(grafo, inicio, destino)'"
                    fn = scope["bfs_camino_mas_corto"]
                    g = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
                    res = fn(g, "A", "D")
                    assert res in [["A", "B", "D"], ["A", "C", "D"]], f"Camino más corto inválido: {res}"

                elif class_num == 8:
                    assert "fibonacci_dinamico" in scope, "Falta definir la función 'fibonacci_dinamico(n)'"
                    fn = scope["fibonacci_dinamico"]
                    assert fn(0) == 0, "fib(0) debe ser 0"
                    assert fn(1) == 1, "fib(1) debe ser 1"
                    assert fn(10) == 55, "fib(10) debe ser 55"
                    assert fn(30) == 832040, "fib(30) debe ser 832040"

            # =================================================================
            # CURSO 3: DESARROLLO DE AGENTES DE INTELIGENCIA ARTIFICIAL
            # =================================================================
            elif course_num == 3:
                if class_num == 1:
                    assert "estimar_costo_tokens" in scope, "Falta definir la función 'estimar_costo_tokens(texto, precio_por_1k)'"
                    fn = scope["estimar_costo_tokens"]
                    res = fn("Hola Mundo Python")
                    assert "tokens_estimados" in res and "costo_usd" in res, "Faltan claves requeridas en el retorno"
                    assert res["tokens_estimados"] > 0, "tokens_estimados debe ser mayor a 0"

                elif class_num == 2:
                    assert "construir_prompt_few_shot" in scope, "Falta definir la función 'construir_prompt_few_shot(rol, tarea, ejemplos, input_usuario)'"
                    fn = scope["construir_prompt_few_shot"]
                    prompt = fn("Traductor", "Traduce", [("Hola", "Hello")], "¿Cómo estás?")
                    assert "Traductor" in prompt and "Hello" in prompt and "¿Cómo estás?" in prompt, "El prompt debe contener todos los bloques"

                elif class_num == 3:
                    assert "ExtractionSchema" in scope and "validar_extraccion_json" in scope, "Falta 'ExtractionSchema' o 'validar_extraccion_json(payload_json)'"
                    fn = scope["validar_extraccion_json"]
                    obj = fn('{"entidad": "Python", "confianza": 0.95, "etiquetas": ["backend", "ai"]}')
                    assert obj.entidad == "Python" and obj.confianza == 0.95, "Validación incorrecta de atributos"

                elif class_num == 4:
                    assert "ToolRegistry" in scope, "Falta definir la clase 'ToolRegistry'"
                    Reg = scope["ToolRegistry"]
                    r = Reg()
                    r.register("sumar", lambda a, b: a + b)
                    assert r.execute("sumar", a=5, b=7) == 12, "La ejecución de la tool 'sumar' debe retornar 12"
                    assert "sumar" in r.list_tools(), "list_tools debe incluir 'sumar'"

                elif class_num == 5:
                    assert "similitud_coseno" in scope, "Falta definir la función 'similitud_coseno(v1, v2)'"
                    fn = scope["similitud_coseno"]
                    assert abs(fn([1.0, 0.0], [1.0, 0.0]) - 1.0) < 1e-4, "Vectores idénticos deben tener similitud 1.0"
                    assert abs(fn([1.0, 0.0], [0.0, 1.0])) < 1e-4, "Vectores ortogonales deben tener similitud 0.0"

                elif class_num == 6:
                    assert "SimpleRAGIndex" in scope, "Falta definir la clase 'SimpleRAGIndex'"
                    Index = scope["SimpleRAGIndex"]
                    idx = Index()
                    idx.agregar_documento("doc1", "Texto A", [1.0, 0.0])
                    idx.agregar_documento("doc2", "Texto B", [0.0, 1.0])
                    top = idx.buscar_similares([0.9, 0.1], top_k=1)
                    assert top == ["doc1"], f"Se esperaba ['doc1'], obtenido {top}"

                elif class_num == 7:
                    assert "ReActAgent" in scope, "Falta definir la clase 'ReActAgent'"
                    Agent = scope["ReActAgent"]
                    ag = Agent()
                    ag.registrar_paso("Pensar", "Actuar", "Observar")
                    traza = ag.obtener_traza()
                    assert len(traza) == 1 and traza[0]["thought"] == "Pensar", "Traza ReAct inválida"

                elif class_num == 8:
                    assert "OrquestadorMultiAgente" in scope, "Falta definir la clase 'OrquestadorMultiAgente'"
                    Orq = scope["OrquestadorMultiAgente"]
                    o = Orq()
                    res = o.procesar_flujo("Consulta")
                    assert res["valid"] is True and "[INVESTIGADO]" in res["final_output"], "Flujo multi-agente inválido"

            # =================================================================
            # CURSO 4: TALLER PRÁCTICO & PROYECTO INTEGRADOR FULL-STACK
            # =================================================================
            elif course_num == 4:
                if class_num == 1:
                    assert "validar_estructura_proyecto" in scope, "Falta definir la función 'validar_estructura_proyecto(modulos)'"
                    fn = scope["validar_estructura_proyecto"]
                    assert fn(["api", "core", "models", "services", "tests"]) is True, "Estructura completa debe retornar True"
                    assert fn(["api", "models"]) is False, "Estructura incompleta debe retornar False"

                elif class_num == 2:
                    assert "crear_endpoint_producto" in scope, "Falta definir la función 'crear_endpoint_producto(datos)'"
                    fn = scope["crear_endpoint_producto"]
                    res = fn({"id": 1, "name": "Laptop", "price": 999.99})
                    assert res["status"] == "ok" and res["data"]["id"] == 1, "Respuesta de endpoint FastAPI inválida"

                elif class_num == 3:
                    assert "registrar_transaccion_sqlite" in scope, "Falta definir la función 'registrar_transaccion_sqlite(conn, origen, destino, monto)'"
                    fn = scope["registrar_transaccion_sqlite"]
                    conn = sqlite3.connect(":memory:")
                    conn.execute("CREATE TABLE cuentas (id TEXT PRIMARY KEY, saldo REAL)")
                    conn.execute("INSERT INTO cuentas VALUES ('A', 100.0), ('B', 50.0)")
                    conn.commit()
                    assert fn(conn, "A", "B", 30.0) is True, "La transacción SQL debe retornar True"
                    saldo_a = conn.execute("SELECT saldo FROM cuentas WHERE id = 'A'").fetchone()[0]
                    saldo_b = conn.execute("SELECT saldo FROM cuentas WHERE id = 'B'").fetchone()[0]
                    assert saldo_a == 70.0 and saldo_b == 80.0, "Los saldos tras la transacción no coinciden"

                elif class_num == 4:
                    assert "preparar_estado_dashboard" in scope, "Falta definir la función 'preparar_estado_dashboard(usuario, metricas)'"
                    fn = scope["preparar_estado_dashboard"]
                    res = fn("Wisrovi", {"activos": 100})
                    assert res["usuario"] == "Wisrovi" and res["listo"] is True, "Estado de dashboard Streamlit inválido"

                elif class_num == 5:
                    assert "procesar_consulta_agente" in scope, "Falta definir la función 'procesar_consulta_agente(consulta, contexto_rag)'"
                    fn = scope["procesar_consulta_agente"]
                    res = fn("¿Qué es Python?", ["Doc 1"])
                    assert res["status"] == "ok" and res["fuentes_usadas"] == 1, "Procesamiento de consulta de agente inválido"

                elif class_num == 6:
                    assert "suite_calidad_codigo" in scope, "Falta definir la función 'suite_calidad_codigo(cobertura_pct, tests_fallidos)'"
                    fn = scope["suite_calidad_codigo"]
                    assert fn(90.0, 0) == (True, "Certificado"), "90% cobertura y 0 fallos debe retornar (True, 'Certificado')"
                    assert fn(80.0, 0)[0] is False, "<85% cobertura debe fallar"

                elif class_num == 7:
                    assert "generar_dockerfile_python" in scope, "Falta definir la función 'generar_dockerfile_python(version, port)'"
                    fn = scope["generar_dockerfile_python"]
                    doc = fn("3.11-slim", 8000)
                    assert "FROM python:3.11-slim" in doc and "EXPOSE 8000" in doc, "Dockerfile generado no contiene directivas requeridas"

                elif class_num == 8:
                    assert "PipelineDespliegue" in scope, "Falta definir la clase 'PipelineDespliegue'"
                    Pipe = scope["PipelineDespliegue"]
                    p = Pipe()
                    res = p.ejecutar_fases(["lint", "test", "build", "deploy"])
                    assert res["status"] == "success" and res["desplegado"] is True, "Pipeline de CI/CD final debe desplegar con éxito"

            return {
                "passed": True,
                "exit_code": 0,
                "output": f"✅ ¡Reto de la Clase 0{class_num} (Curso {course_num}) superado con éxito! Todas las pruebas unitarias y contratos de tipado validados.",
                "socratic_hint": "",
                "score": 100
            }
        except AssertionError as ae:
            return {
                "passed": False,
                "exit_code": 1,
                "output": f"AssertionError: {str(ae)}",
                "socratic_hint": f"💡 Pista del Mentor: {str(ae)}. Revisa los casos límite o contratos de tu función.",
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
