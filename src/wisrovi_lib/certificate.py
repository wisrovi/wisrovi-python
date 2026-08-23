#!/usr/bin/env python3
"""
Generador de Certificados de Acreditación Profesional en PDF.
Emite diplomas oficiales en alta resolución con sellos vectoriales dorados,
tipografía académica LaTeX, código de verificación hash y firma del mentor.
"""

import os
import hashlib
import tempfile
import subprocess
from datetime import datetime
from typing import Dict, Any, Optional

CERTIFICATE_TEMPLATE_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Certificado de Acreditación Oficial - Wisrovi Academy</title>
<style>
  @page {
    size: A4 landscape;
    margin: 0;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    font-family: 'Latin Modern Roman', 'Georgia', 'Times New Roman', serif;
    background: #0f172a;
    color: #1e293b;
    width: 297mm;
    height: 210mm;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 10mm;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  .cert-outer {
    background: #ffffff;
    width: 100%;
    height: 100%;
    border: 8px solid #0f172a;
    outline: 2px solid #d97706;
    outline-offset: -12px;
    padding: 12mm 15mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-align: center;
    position: relative;
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
  }
  .cert-header {
    margin-bottom: 2mm;
  }
  .cert-logo {
    font-size: 16pt;
    font-weight: 800;
    letter-spacing: 2px;
    color: #0f172a;
    text-transform: uppercase;
  }
  .cert-sublogo {
    font-size: 8pt;
    color: #d97706;
    letter-spacing: 3px;
    text-transform: uppercase;
    font-weight: 700;
    margin-top: 1mm;
  }
  .cert-title-block {
    margin: 2mm 0;
  }
  .cert-title {
    font-size: 24pt;
    font-weight: 900;
    color: #0f172a;
    letter-spacing: 1px;
    text-transform: uppercase;
  }
  .cert-preamble {
    font-size: 11pt;
    color: #64748b;
    font-style: italic;
    margin-top: 1mm;
  }
  .cert-student-name {
    font-size: 26pt;
    font-weight: 900;
    color: #0284c7;
    text-decoration: none;
    border-bottom: 2px solid #0284c7;
    display: inline-block;
    padding: 0 10mm 1mm 10mm;
    margin: 2mm 0;
    letter-spacing: 1px;
  }
  .cert-body {
    font-size: 11pt;
    line-height: 1.4;
    color: #334155;
    max-width: 220mm;
    margin: 0 auto;
  }
  .cert-course-name {
    font-weight: 800;
    color: #0f172a;
    font-size: 13pt;
    display: block;
    margin: 1.5mm 0;
  }
  .cert-details {
    display: flex;
    justify-content: center;
    gap: 12mm;
    font-size: 9.5pt;
    color: #475569;
    margin: 2mm 0;
  }
  .cert-details span strong {
    color: #0f172a;
  }
  .cert-footer {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 1px solid #e2e8f0;
    padding-top: 4mm;
    margin-top: 2mm;
  }
  .cert-seal-box {
    text-align: left;
    font-size: 8pt;
    color: #64748b;
  }
  .cert-seal-badge {
    background: #0f172a;
    color: #fbbf24;
    padding: 2mm 4mm;
    font-size: 7.5pt;
    font-weight: 800;
    letter-spacing: 1px;
    display: inline-block;
    border-radius: 4px;
    margin-bottom: 1mm;
  }
  .cert-hash {
    font-family: monospace;
    font-size: 7pt;
    color: #94a3b8;
  }
  .cert-signature-box {
    text-align: right;
  }
  .cert-signature-line {
    font-family: 'Brush Script MT', 'Dancing Script', cursive, serif;
    font-size: 20pt;
    color: #0f172a;
    margin-bottom: -1mm;
  }
  .cert-signer-name {
    font-size: 10.5pt;
    font-weight: 800;
    color: #0f172a;
    border-top: 1.5px solid #0f172a;
    padding-top: 1mm;
    display: inline-block;
  }
  .cert-signer-title {
    font-size: 8pt;
    color: #64748b;
  }
</style>
</head>
<body>
<div class="cert-outer">
  <div class="cert-header">
    <div class="cert-logo">WISROVI ACADEMY OF ADVANCED SOFTWARE & AI</div>
    <div class="cert-sublogo">Centro Internacional de Excelencia en Ingeniería de Software & Inteligencia Artificial</div>
  </div>

  <div class="cert-title-block">
    <div class="cert-title">Certificado de Acreditación Profesional</div>
    <div class="cert-preamble">Por cuanto se certifica y hace constar formalmente que:</div>
  </div>

  <div>
    <div class="cert-student-name">{student_name}</div>
  </div>

  <div class="cert-body">
    Ha cursado y superado con distinción académica todas las exigencias formativas, prácticas de laboratorio y suites de pruebas unitarias automatizadas del programa de alta especialización:
    <span class="cert-course-name">«{course_title}»</span>
  </div>

  <div class="cert-details">
    <span>• Carga Formativa: <strong>{hours} Horas de Práctica Activa</strong></span>
    <span>• Metodología: <strong>Aprendizaje en Espiral & La Regla de la Bicicleta</strong></span>
    <span>• Fecha de Graduación: <strong>{issue_date}</strong></span>
  </div>

  <div class="cert-footer">
    <div class="cert-seal-box">
      <div class="cert-seal-badge">🛡️ CERTIFICACIÓN VERIFICADA &bull; WISROVI SUITE</div>
      <div>Verificación oficial en: <strong style="color: #0284c7;">academy_python.wisrovi.dev/verify</strong></div>
      <div class="cert-hash">ID Hash: {cert_hash}</div>
    </div>

    <div class="cert-signature-box">
      <div class="cert-signature-line">William Rodriguez</div>
      <div class="cert-signer-name">William Rodríguez (Wisrovi)</div>
      <div class="cert-signer-title">Principal Software Engineer & AI Solutions Architect &bull; Badajoz, España</div>
    </div>
  </div>
</div>
</body>
</html>
"""

CLASS_CERTIFICATES: Dict[str, Dict[str, str]] = {
    # =========================================================================
    # CURSO 1: FUNDAMENTOS BÁSICOS DE PYTHON
    # =========================================================================
    "1-1": {
        "title": "Acreditación en Fundamentos de Programación & Flujo de Control",
        "skill": "Sintaxis Fundamental, Variables y Decisiones Básicas",
        "concept": "Ha demostrado dominio técnico al estructurar programas en Python utilizando variables en memoria RAM, bifurcaciones condicionales lógicas y bucles de iteración fundamentales.",
        "badge": "🌱 Primer Pedaleo",
        "linkedin_text": "🚀 ¡Acabo de superar la Clase 01 del Programa Integral de Python con William Rodríguez (Wisrovi)! He aprendido a dominar la sintaxis fundamental, el modelo de memoria y el flujo de control en Python. 🎓 Certificado oficial verificado por Wisrovi Academy: https://wisrovi.github.io/wisrovi-python/ #Python #SoftwareEngineering #CleanCode #Wisrovi"
    },
    "1-2": {
        "title": "Acreditación en Tipado Estático y Type Hints (PEP 484)",
        "skill": "Desarrollo Tipado y Contratos Estrictos en Python",
        "concept": "Ha demostrado maestría técnica al diseñar funciones con contratos de tipado estricto (Type Hints - PEP 484), previniendo errores de diseño e inspeccionando la memoria RAM.",
        "badge": "🏷️ Type Master",
        "linkedin_text": "🚀 ¡Acabo de obtener mi Diploma en «Tipado Estático y Type Hints (PEP 484)» en Python! He aprendido a escribir código robusto con contratos estrictos de parámetros y retornos. Mentoría por William Rodríguez (Wisrovi). 🎓 https://wisrovi.github.io/wisrovi-python/ #Python #TypeHints #PEP484 #Wisrovi"
    },
    "1-3": {
        "title": "Acreditación en Bifurcaciones Lógicas y Toma de Decisiones",
        "skill": "Control de Flujo con Condicionales Complejas",
        "concept": "Ha demostrado solvencia al resolver árboles de decisión complejos con operadores lógicos, evaluación en cortocircuito y sentencias if/elif/else optimizadas.",
        "badge": "🚦 Control Flow Expert",
        "linkedin_text": "🚀 ¡Superada la Clase 03 de Python con William Rodríguez (Wisrovi)! Dominando bifurcaciones lógicas, álgebra booleana y control de flujo empresarial en Python. 🎓 https://wisrovi.github.io/wisrovi-python/ #Python #Programming #CleanCode"
    },
    "1-4": {
        "title": "Acreditación en Bucles y Procesamiento Iterativo Eficiente",
        "skill": "Iteración con for/while y Control de Bucles",
        "concept": "Ha demostrado habilidad práctica en la automatización de procesos repetitivos mediante bucles for y while, manipulando secuencias y controlando la ejecución con break y continue.",
        "badge": "⚙️ Loop Automator",
        "linkedin_text": "🚀 ¡Acabo de certificarme en «Bucles e Iteración Avanzada» en Python con William Rodríguez (Wisrovi)! Automatizando flujos de datos y procesamiento en memoria. 🎓 https://wisrovi.github.io/wisrovi-python/ #Python #Automation #Algorithms"
    },
    "1-5": {
        "title": "Acreditación en Manipulación de Secuencias y Colecciones",
        "skill": "Listas Mutables, Tuplas Inmutables y Slicing",
        "concept": "Ha demostrado capacidad analítica al seleccionar y transformar estructuras de datos secuenciales, optimizando la mutabilidad e indexación avanzada en memoria.",
        "badge": "📦 Sequence Architect",
        "linkedin_text": "🚀 ¡Nuevo diploma obtenido! Acreditado en «Listas, Tuplas y Slicing Avanzado» en Python con William Rodríguez (Wisrovi). Dominando la memoria y la mutabilidad. 🎓 https://wisrovi.github.io/wisrovi-python/ #Python #DataStructures"
    },
    "1-6": {
        "title": "Acreditación en Diccionarios Hash y Teoría de Conjuntos",
        "skill": "Mapeo Clave-Valor O(1) y Conjuntos Sets",
        "concept": "Ha demostrado excelencia técnica al estructurar datos con tablas hash clave-valor en diccionarios y aplicar operaciones de conjuntos para eliminar duplicados en tiempo récord.",
        "badge": "🔑 Key-Value Wizard",
        "linkedin_text": "🚀 ¡Certificado en «Diccionarios y Sets Hash» en Python con William Rodríguez (Wisrovi)! Optimizando accesos a datos O(1) y álgebra de conjuntos. 🎓 https://wisrovi.github.io/wisrovi-python/ #Python #DataStructures #HashTables"
    },
    "1-7": {
        "title": "Acreditación en Arquitectura Funcional, Ámbitos y Scope",
        "skill": "Funciones de Primer Nivel, Args/Kwargs y Modularidad",
        "concept": "Ha demostrado dominio en el diseño de código modular, limpio y mantenible mediante funciones puras, argumentos posicionales/nombrados (*args, **kwargs) y gestión precisa del Scope.",
        "badge": "🧩 Function Master",
        "linkedin_text": "🚀 ¡Acabo de superar la Clase 07 de Python con William Rodríguez (Wisrovi)! Acreditado en «Funciones de Primer Nivel, Scope y Modularidad Limpia». 🎓 https://wisrovi.github.io/wisrovi-python/ #Python #FunctionalProgramming #SoftwareEngineering"
    },
    "1-8": {
        "title": "Acreditación en Desarrollo de Aplicaciones CLI Completas",
        "skill": "Arquitectura de Software y Proyecto Integrador CLI",
        "concept": "Ha demostrado capacidad de ingeniería al integrar todos los fundamentos de Python en una aplicación de consola funcional, testeada y lista para producción.",
        "badge": "🏆 CLI Master Builder",
        "linkedin_text": "🚀 ¡He completado el Curso 1 de Python y graduado mi primer Proyecto Integrador CLI con William Rodríguez (Wisrovi)! Preparado para la ingeniería de algoritmos y estructuras avanzadas. 🎓 https://wisrovi.github.io/wisrovi-python/ #Python #Portfolio #DevProject"
    },

    # =========================================================================
    # CURSO 2: ALGORITMOS AVANZADOS Y ESTRUCTURAS DE DATOS
    # =========================================================================
    "2-1": {
        "title": "Acreditación en Análisis de Complejidad y Notación Big-O",
        "skill": "Eficiencia Asintótica de Tiempo y Espacio",
        "concept": "Ha demostrado rigor de ingeniería al evaluar la eficiencia temporal y espacial de algoritmos, reduciendo cuellos de botella de O(N²) a O(N) y O(1).",
        "badge": "⚡ Big-O Optimizer",
        "linkedin_text": "🚀 ¡Nuevo diploma en «Análisis de Complejidad y Notación Big-O» con William Rodríguez (Wisrovi)! Optimizando el rendimiento computacional de algoritmos en Python. 🎓 https://wisrovi.github.io/wisrovi-python/ #BigO #Algorithms #Performance"
    },
    "2-2": {
        "title": "Acreditación en Estructuras LIFO y FIFO de Alta Velocidad",
        "skill": "Pilas, Colas y Optimización con collections.deque",
        "concept": "Ha demostrado destreza en la implementación de buffers de tareas FIFO y validadores sintácticos LIFO con operaciones O(1) en los extremos de la memoria.",
        "badge": "🥞 Stack & Queue Master",
        "linkedin_text": "🚀 ¡Certificado en «Pilas LIFO y Colas FIFO con deque» en Python con William Rodríguez (Wisrovi)! Rendimiento O(1) para arquitecturas de alta concurrencia. 🎓 https://wisrovi.github.io/wisrovi-python/ #DataStructures #Algorithms"
    },
    "2-3": {
        "title": "Acreditación en Tablas Hash y Búsqueda en Tiempo Constante",
        "skill": "Estructuras de Búsqueda O(1) y Resolución de Colisiones",
        "concept": "Ha demostrado dominio en el aprovechamiento de funciones hash para indexación y búsqueda instantánea en tiempo constante O(1).",
        "badge": "⚡ O(1) Hash Expert",
        "linkedin_text": "🚀 ¡Superada la Clase 03 del Curso de Algoritmos con William Rodríguez (Wisrovi)! Acreditado en «Tablas Hash y Búsqueda O(1)». 🎓 https://wisrovi.github.io/wisrovi-python/ #HashTables #DataStructures"
    },
    "2-4": {
        "title": "Acreditación en Algoritmos de Búsqueda Binaria",
        "skill": "Búsqueda por Bisección con Complejidad O(log n)",
        "concept": "Ha demostrado maestría al implementar algoritmos de búsqueda logarítmica O(log N) sobre colecciones ordenadas masivas.",
        "badge": "🎯 Binary Search Pro",
        "linkedin_text": "🚀 ¡Acreditado en «Búsqueda Binaria O(log n)» en Python con William Rodríguez (Wisrovi)! Reduciendo millones de operaciones a microsegundos. 🎓 https://wisrovi.github.io/wisrovi-python/ #BinarySearch #Algorithms"
    },
    "2-5": {
        "title": "Acreditación en Ordenamiento con Divide y Vencerás",
        "skill": "QuickSort, MergeSort y Algoritmos O(n log n)",
        "concept": "Ha demostrado solvencia algorítmica al implementar estrategias de partición y mezcla recursiva para ordenar estructuras de datos a escala.",
        "badge": "📊 Sorting Champion",
        "linkedin_text": "🚀 ¡He obtenido mi diploma en «QuickSort y MergeSort» con William Rodríguez (Wisrovi)! Dominando el paradigma Divide y Vencerás en Python. 🎓 https://wisrovi.github.io/wisrovi-python/ #Sorting #Algorithms"
    },
    "2-6": {
        "title": "Acreditación en Árboles Binarios de Búsqueda (BST)",
        "skill": "Estructuras Jerárquicas y Recorridos de Árbol",
        "concept": "Ha demostrado capacidad técnica al construir árboles binarios balanceados, gestionando nodos, inserciones y recorridos in-order, pre-order y post-order.",
        "badge": "🌳 Tree Architect",
        "linkedin_text": "🚀 ¡Certificado en «Árboles Binarios de Búsqueda (BST)» con William Rodríguez (Wisrovi)! Estructurando datos jerárquicos eficientes en memoria. 🎓 https://wisrovi.github.io/wisrovi-python/ #Trees #DataStructures"
    },
    "2-7": {
        "title": "Acreditación en Modelado de Grafos y Recorridos BFS / DFS",
        "skill": "Grafos, Matrices de Adyacencia y Rutas Óptimas",
        "concept": "Ha demostrado maestría en la representación de redes mediante grafos y el cálculo de caminos más cortos y exploración con Breadth-First y Depth-First Search.",
        "badge": "🕸️ Graph Master",
        "linkedin_text": "🚀 ¡Nuevo hito alcanzado! Acreditado en «Grafos y Recorridos BFS/DFS» en Python con William Rodríguez (Wisrovi). Resolviendo redes y rutas óptimas. 🎓 https://wisrovi.github.io/wisrovi-python/ #GraphAlgorithms #BFS #DFS"
    },
    "2-8": {
        "title": "Acreditación en Programación Dinámica y Memoización",
        "skill": "Optimización Recursiva y Tabulación de Estados",
        "concept": "Ha demostrado excelencia matemática y computacional al transformar algoritmos exponenciales O(2^N) en soluciones polinómicas O(N) con memoización.",
        "badge": "🧠 Dynamic Programming Guru",
        "linkedin_text": "🚀 ¡Graduado del Curso 2 de Algoritmos con William Rodríguez (Wisrovi)! Acreditado en «Recursividad y Programación Dinámica». ¡Listo para Agentes de IA! 🎓 https://wisrovi.github.io/wisrovi-python/ #DynamicProgramming #Memoization"
    },

    # =========================================================================
    # CURSO 3: CREACIÓN Y DESARROLLO DE AGENTES DE INTELIGENCIA ARTIFICIAL
    # =========================================================================
    "3-1": {
        "title": "Acreditación en Fundamentos de LLMs y Tokenización",
        "skill": "Arquitectura Transformer, Context Windows y Tokens",
        "concept": "Ha demostrado comprensión rigurosa de los modelos de lenguaje autorregresivos, cálculo de costes de contexto y codificación de tokens.",
        "badge": "🤖 LLM Pioneer",
        "linkedin_text": "🚀 ¡Iniciando el Curso de Agentes de IA con William Rodríguez (Wisrovi)! Acreditado en «Fundamentos de LLMs y Tokenización». 🎓 https://wisrovi.github.io/wisrovi-python/ #LLM #ArtificialIntelligence #GenerativeAI"
    },
    "3-2": {
        "title": "Acreditación en Prompt Engineering Avanzado y Few-Shot",
        "skill": "Instrucciones de Sistema, Delimitadores y Few-Shot",
        "concept": "Ha demostrado dominio en el diseño de directrices deterministas, mitigación de alucinaciones y técnicas de razonamiento guiado para modelos de lenguaje.",
        "badge": "✍️ Prompt Engineer",
        "linkedin_text": "🚀 ¡Diploma obtenido en «Prompt Engineering Avanzado & Few-Shot» con William Rodríguez (Wisrovi)! Diseñando especificaciones de alta precisión para IA. 🎓 https://wisrovi.github.io/wisrovi-python/ #PromptEngineering #AI"
    },
    "3-3": {
        "title": "Acreditación en Salidas Estructuradas con Pydantic V2",
        "skill": "Validación de Esquemas JSON y Tipado Estricto para IA",
        "concept": "Ha demostrado excelencia en el control de interfaces de IA mediante modelos Pydantic, garantizando respuestas JSON parseables y tipadas.",
        "badge": "🛡️ Structured Output Specialist",
        "linkedin_text": "🚀 ¡Certificado en «Salidas Estructuradas con Pydantic V2 para IA» con William Rodríguez (Wisrovi)! Blindando la comunicación entre LLMs y backend. 🎓 https://wisrovi.github.io/wisrovi-python/ #Pydantic #StructuredOutputs #AI"
    },
    "3-4": {
        "title": "Acreditación en Tool Calling y Function Execution Engine",
        "skill": "Despacho Dinámico de Herramientas en Python para LLMs",
        "concept": "Ha demostrado maestría al dotar a modelos LLM de herramientas reales en Python, implementando esquemas de herramientas y despacho seguro de llamadas a funciones.",
        "badge": "🛠️ Tool Calling Engineer",
        "linkedin_text": "🚀 ¡He obtenido mi Acreditación en «Tool Calling y Function Calling en Python» con William Rodríguez (Wisrovi)! Conectando LLMs con ejecución de código en el mundo real. 🎓 https://wisrovi.github.io/wisrovi-python/ #ToolCalling #FunctionCalling #AIAgents"
    },
    "3-5": {
        "title": "Acreditación en Embeddings y Representación Semántica",
        "skill": "Vectores Semánticos y Similitud Coseno",
        "concept": "Ha demostrado habilidad en la transformación de texto a espacios vectoriales de alta dimensión y cálculo de distancias semánticas en memoria.",
        "badge": "📐 Vector Space Master",
        "linkedin_text": "🚀 ¡Superada la Clase 05 de Agentes de IA con William Rodríguez (Wisrovi)! Acreditado en «Embeddings y Similitud Coseno». 🎓 https://wisrovi.github.io/wisrovi-python/ #Embeddings #VectorSearch #AI"
    },
    "3-6": {
        "title": "Acreditación en Arquitecturas RAG (Retrieval-Augmented Generation)",
        "skill": "Recuperación Vectorial e Inyección de Contexto en Tiempo Real",
        "concept": "Ha demostrado capacidad de arquitectura al construir pipelines RAG que aumentan el conocimiento de los LLMs con fuentes documentales privadas.",
        "badge": "📚 RAG Architect",
        "linkedin_text": "🚀 ¡Diploma en «Arquitecturas RAG (Retrieval-Augmented Generation)» con William Rodríguez (Wisrovi)! Creando sistemas de IA basados en conocimiento real. 🎓 https://wisrovi.github.io/wisrovi-python/ #RAG #VectorDatabase #AIAgents"
    },
    "3-7": {
        "title": "Acreditación en Agentes Autónomos y Ciclo ReAct",
        "skill": "Razonamiento ReAct (Thought -> Action -> Observation)",
        "concept": "Ha demostrado solvencia técnica al diseñar agentes autónomos capaces de razonar iterativamente, seleccionar herramientas y resolver objetivos complejos.",
        "badge": "🕵️ ReAct Agent Creator",
        "linkedin_text": "🚀 ¡Acabo de construir mi primer Agente Autónomo ReAct en Python con William Rodríguez (Wisrovi)! Acreditado en «Ciclos Cognitivos de IA». 🎓 https://wisrovi.github.io/wisrovi-python/ #ReAct #AIAgents #AutonomousAI"
    },
    "3-8": {
        "title": "Acreditación en Sistemas Multi-Agente y Guardrails",
        "skill": "Orquestación de Equipos de Agentes y Políticas de Seguridad",
        "concept": "Ha demostrado liderazgo técnico al coordinar sistemas multi-agente distribuidos con supervisión jerárquica y validación de seguridad contra ataques de inyección.",
        "badge": "🌐 Multi-Agent Orchestrator",
        "linkedin_text": "🚀 ¡Graduado del Curso 3 de Agentes de Inteligencia Artificial con William Rodríguez (Wisrovi)! Acreditado en «Sistemas Multi-Agente & Guardrails». 🎓 https://wisrovi.github.io/wisrovi-python/ #MultiAgent #Guardrails #AIArchitecture"
    },

    # =========================================================================
    # CURSO 4: TALLER PRÁCTICO & PROYECTO FINAL INTEGRADOR FULL-STACK
    # =========================================================================
    "4-1": {
        "title": "Acreditación en Arquitectura de Software y Planificación",
        "skill": "Diseño Modular, Diagramas C4 y Contratos de Dominio",
        "concept": "Ha demostrado visión de ingeniería al planificar sistemas desacoplados, modelos de dominio limpios y flujos de integración punta a punta.",
        "badge": "📐 Lead Architect",
        "linkedin_text": "🚀 ¡Iniciando el Proyecto Final con William Rodríguez (Wisrovi)! Acreditado en «Arquitectura de Software y Planificación de Sistemas Full-Stack de IA». 🎓 https://wisrovi.github.io/wisrovi-python/ #SoftwareArchitecture #SystemDesign"
    },
    "4-2": {
        "title": "Acreditación en Desarrollo de Backend con FastAPI",
        "skill": "APIs REST Asíncronas, Rutas y Validación de Entrada",
        "concept": "Ha demostrado dominio en el desarrollo de microservicios HTTP de alto rendimiento con FastAPI, inyección de dependencias y OpenAPI.",
        "badge": "⚡ FastAPI Backend Specialist",
        "linkedin_text": "🚀 ¡Diploma en «Backend APIs con FastAPI» obtenido con William Rodríguez (Wisrovi)! Creando servicios asíncronos de nivel de producción. 🎓 https://wisrovi.github.io/wisrovi-python/ #FastAPI #Python #APIDesign"
    },
    "4-3": {
        "title": "Acreditación en Persistencia Relacional y Transacciones ACID",
        "skill": "Modelado de Bases de Datos SQL y Transaccionalidad",
        "concept": "Ha demostrado rigor en el diseño de esquemas de datos, consultas optimizadas y control de integridad transaccional ACID.",
        "badge": "🗄️ Database Engineer",
        "linkedin_text": "🚀 ¡Certificado en «Persistencia SQL y Transacciones ACID» con William Rodríguez (Wisrovi)! Garantizando integridad de datos en Python. 🎓 https://wisrovi.github.io/wisrovi-python/ #SQL #Databases #ACID"
    },
    "4-4": {
        "title": "Acreditación en Frontend Interactivo con Streamlit",
        "skill": "Dashboards de Control e Interfaces Reactivas",
        "concept": "Ha demostrado destreza al construir interfaces de usuario elegantes y reactivas para interactuar con modelos de IA y bases de datos.",
        "badge": "🖥️ Streamlit Frontend Pro",
        "linkedin_text": "🚀 ¡Superada la Clase 04 de Proyecto Final con William Rodríguez (Wisrovi)! Acreditado en «Interfaces Interactivas con Streamlit». 🎓 https://wisrovi.github.io/wisrovi-python/ #Streamlit #DataApp #Python"
    },
    "4-5": {
        "title": "Acreditación en Integración de Motores de IA en Aplicaciones",
        "skill": "Conexión de Agentes de IA a Pipelines de Producción",
        "concept": "Ha demostrado solvencia al integrar pipelines de razonamiento artificial y procesamiento de lenguaje natural en el flujo operativo del software.",
        "badge": "🔌 AI Integration Engineer",
        "linkedin_text": "🚀 ¡Diploma obtenido en «Integración de Motores de IA en Producción» con William Rodríguez (Wisrovi)! Software inteligente en acción. 🎓 https://wisrovi.github.io/wisrovi-python/ #AI #ProductionAI #Python"
    },
    "4-6": {
        "title": "Acreditación en Testing Riguroso con Pytest, Mocks y CI",
        "skill": "Pruebas Unitarias, Fixtures y Cobertura de Código",
        "concept": "Ha demostrado calidad de ingeniería al diseñar suites de pruebas automatizadas con pytest, fixtures y mocks para aislar dependencias críticas.",
        "badge": "🧪 QA & Test Master",
        "linkedin_text": "🚀 ¡Acreditado en «Testing con Pytest, Fixtures y Mocks» con William Rodríguez (Wisrovi)! Calidad y fiabilidad de software comprobada. 🎓 https://wisrovi.github.io/wisrovi-python/ #Pytest #QualityAssurance #Python"
    },
    "4-7": {
        "title": "Acreditación en Containerización Profesional con Docker",
        "skill": "Dockerfiles Multi-Stage y Docker Compose Multi-Servicio",
        "concept": "Ha demostrado solvencia DevOps al empaquetar aplicaciones completas en contenedores reproducibles y orquestar servicios con Docker Compose.",
        "badge": "🐳 Docker & Container Expert",
        "linkedin_text": "🚀 ¡Certificado en «Containerización con Docker & Compose» en Python con William Rodríguez (Wisrovi)! Despliegue estandarizado y reproducible. 🎓 https://wisrovi.github.io/wisrovi-python/ #Docker #DevOps #Microservices"
    },
    "4-8": {
        "title": "Acreditación en Despliegue Continuo CI/CD y Portafolio de Élite",
        "skill": "Pipelines de Despliegue en la Nube y Portafolio Profesional",
        "concept": "Ha demostrado excelencia profesional al culminar con éxito el Programa Integral de Formación en Python: De Cero a Agentes de Inteligencia Artificial, desplegando su solución en producción.",
        "badge": "👑 Python & AI Master Engineer",
        "linkedin_text": "🏆 ¡HE COMPLETADO EL PROGRAMA INTEGRAL DE PYTHON (32 SEMANAS)! Desde fundamentos y algoritmos hasta Agentes de IA y Arquitectura Full-Stack en producción. Agradecido con William Rodríguez (Wisrovi) por esta mentoría de excelencia. 🎓 https://wisrovi.github.io/wisrovi-python/ #Python #AI #CloudDeployment #Portfolio"
    }
}

CLASS_CERTIFICATE_TEMPLATE_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Diploma de Acreditación de Competencia - Wisrovi Academy</title>
<style>
  @page {
    size: A4 landscape;
    margin: 0;
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    font-family: 'Latin Modern Roman', 'Georgia', 'Times New Roman', serif;
    background: #0f172a;
    color: #1e293b;
    width: 297mm;
    height: 210mm;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 8mm;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
  }
  .cert-outer {
    background: #ffffff;
    width: 100%;
    height: 100%;
    border: 8px solid #0f172a;
    outline: 2px solid #d97706;
    outline-offset: -12px;
    padding: 10mm 14mm;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-align: center;
    position: relative;
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
  }
  .cert-header {
    margin-bottom: 1.5mm;
  }
  .cert-logo {
    font-size: 15pt;
    font-weight: 800;
    letter-spacing: 2px;
    color: #0f172a;
    text-transform: uppercase;
  }
  .cert-sublogo {
    font-size: 8pt;
    color: #d97706;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    font-weight: 700;
    margin-top: 1mm;
  }
  .cert-title-block {
    margin: 1.5mm 0;
  }
  .cert-badge-tag {
    background: #0284c7;
    color: #ffffff;
    font-size: 8pt;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 1.5mm 4mm;
    border-radius: 4px;
    display: inline-block;
    margin-bottom: 2mm;
  }
  .cert-title {
    font-size: 21pt;
    font-weight: 900;
    color: #0f172a;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }
  .cert-preamble {
    font-size: 10.5pt;
    color: #64748b;
    font-style: italic;
    margin-top: 1mm;
  }
  .cert-student-name {
    font-size: 24pt;
    font-weight: 900;
    color: #0284c7;
    border-bottom: 2px solid #0284c7;
    display: inline-block;
    padding: 0 8mm 1mm 8mm;
    margin: 1.5mm 0;
  }
  .cert-body {
    font-size: 10.5pt;
    line-height: 1.35;
    color: #334155;
    max-width: 230mm;
    margin: 0 auto;
  }
  .cert-skill-name {
    font-weight: 800;
    color: #0f172a;
    font-size: 12pt;
    display: block;
    margin: 1.5mm 0 1mm 0;
  }
  .cert-concept-box {
    background: #f8fafc;
    border-left: 3px solid #d97706;
    padding: 2mm 4mm;
    margin: 1.5mm auto;
    font-size: 9.5pt;
    color: #475569;
    text-align: justify;
    max-width: 220mm;
    line-height: 1.3;
  }
  .cert-details {
    display: flex;
    justify-content: center;
    gap: 8mm;
    font-size: 9pt;
    color: #475569;
    margin: 1.5mm 0;
  }
  .cert-details span strong {
    color: #0f172a;
  }
  .cert-footer {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 1px solid #e2e8f0;
    padding-top: 3mm;
    margin-top: 1.5mm;
  }
  .cert-seal-box {
    text-align: left;
    font-size: 7.5pt;
    color: #64748b;
  }
  .cert-seal-badge {
    background: #0f172a;
    color: #fbbf24;
    padding: 1.5mm 3.5mm;
    font-size: 7pt;
    font-weight: 800;
    letter-spacing: 1px;
    display: inline-block;
    border-radius: 4px;
    margin-bottom: 1mm;
  }
  .cert-hash {
    font-family: monospace;
    font-size: 6.5pt;
    color: #94a3b8;
  }
  .cert-signature-box {
    text-align: right;
  }
  .cert-signature-line {
    font-family: 'Brush Script MT', 'Dancing Script', cursive, serif;
    font-size: 18pt;
    color: #0f172a;
    margin-bottom: -1mm;
  }
  .cert-signer-name {
    font-size: 9.5pt;
    font-weight: 800;
    color: #0f172a;
    border-top: 1.5px solid #0f172a;
    padding-top: 1mm;
    display: inline-block;
  }
  .cert-signer-title {
    font-size: 7.5pt;
    color: #64748b;
  }
</style>
</head>
<body>
<div class="cert-outer">
  <div class="cert-header">
    <div class="cert-logo">WISROVI ACADEMY OF ADVANCED SOFTWARE & AI</div>
    <div class="cert-sublogo">Centro Internacional de Excelencia en Ingeniería de Software & Inteligencia Artificial</div>
  </div>

  <div class="cert-title-block">
    <div class="cert-badge-tag">{badge_tag}</div>
    <div class="cert-title">{cert_title}</div>
    <div class="cert-preamble">Por cuanto se certifica y hace constar formalmente que:</div>
  </div>

  <div>
    <div class="cert-student-name">{student_name}</div>
  </div>

  <div class="cert-body">
    Ha completado satisfactoriamente el laboratorio práctico y superado el 100% de las pruebas unitarias automatizadas correspondientes a la competencia técnica:
    <span class="cert-skill-name">«{skill_title}»</span>
    <div class="cert-concept-box">
      <strong>Evidencia de Aprendizaje:</strong> {concept_learned}
    </div>
  </div>

  <div class="cert-details">
    <span>• Curso: <strong>{course_name} (Clase 0{class_num})</strong></span>
    <span>• Metodología: <strong>La Regla de la Bicicleta & Práctica Activa</strong></span>
    <span>• Fecha: <strong>{issue_date}</strong></span>
  </div>

  <div class="cert-footer">
    <div class="cert-seal-box">
      <div class="cert-seal-badge">🛡️ MICRO-ACREDITACIÓN VERIFICADA &bull; WISROVI ACADEMY</div>
      <div>Verificación oficial: <strong style="color: #0284c7;">wisrovi.github.io/wisrovi-python/</strong></div>
      <div class="cert-hash">ID Hash: {cert_hash}</div>
    </div>

    <div class="cert-signature-box">
      <div class="cert-signature-line">William Rodriguez</div>
      <div class="cert-signer-name">William Rodríguez (Wisrovi)</div>
      <div class="cert-signer-title">Principal Software Engineer & AI Solutions Architect &bull; Badajoz, España</div>
    </div>
  </div>
</div>
</body>
</html>
"""

class CertificateGenerator:
    """Generador de diplomas PDF y PNG de certificación de cursos y micro-acreditaciones de clase."""

    @classmethod
    def get_class_info(cls, course_num: int, class_num: int) -> Dict[str, str]:
        """Obtiene los metadatos de acreditación para una clase específica."""
        key = f"{course_num}-{class_num}"
        if key in CLASS_CERTIFICATES:
            return CLASS_CERTIFICATES[key]
        return {
            "title": f"Acreditación en Clase {class_num:02d} del Curso {course_num}",
            "skill": f"Competencias Clave de la Sesión {class_num:02d}",
            "concept": "Ha superado satisfactoriamente las pruebas automatizadas y retos de ingeniería de esta sesión.",
            "badge": f"🎯 Clase {class_num:02d}",
            "linkedin_text": f"🚀 ¡Acabo de superar la Clase {class_num:02d} del Curso {course_num} de Python con @Wisrovi! 🎓 Certificado por Wisrovi Academy: https://wisrovi.github.io/wisrovi-python/ #Python"
        }

    @classmethod
    def generate_html(
        cls,
        student_name: str,
        course_title: str = "Programa Integral de Formación en Python: De Cero a Agentes de IA",
        hours: int = 160
    ) -> str:
        """Renderiza el documento HTML del certificado de curso o programa completo."""
        issue_date = datetime.now().strftime("%d de %B de %Y")
        
        # Generar hash de verificación único
        hash_seed = f"{student_name}-{course_title}-{issue_date}-wisrovi-academy-2026"
        cert_hash = hashlib.sha256(hash_seed.encode("utf-8")).hexdigest()[:24].upper()
        
        html = (
            CERTIFICATE_TEMPLATE_HTML
            .replace("{student_name}", student_name.strip() or "Estudiante Wisrovi")
            .replace("{course_title}", course_title)
            .replace("{hours}", str(hours))
            .replace("{issue_date}", issue_date)
            .replace("{cert_hash}", cert_hash)
        )
        return html

    @classmethod
    def generate_class_certificate_html(
        cls,
        student_name: str,
        course_num: int,
        class_num: int
    ) -> str:
        """Renderiza el documento HTML del diploma oficial específico de una clase."""
        info = cls.get_class_info(course_num, class_num)
        issue_date = datetime.now().strftime("%d de %B de %Y")
        
        course_names = {
            1: "Curso 1: Fundamentos Básicos de Python",
            2: "Curso 2: Algoritmos Avanzados y Estructuras de Datos",
            3: "Curso 3: Desarrollo de Agentes de Inteligencia Artificial",
            4: "Curso 4: Taller Práctico & Proyecto Integrador Full-Stack"
        }
        course_name = course_names.get(course_num, f"Curso {course_num}")
        
        hash_seed = f"{student_name}-c{course_num}-s{class_num}-{issue_date}-wisrovi-class-cert"
        cert_hash = hashlib.sha256(hash_seed.encode("utf-8")).hexdigest()[:24].upper()
        
        html = (
            CLASS_CERTIFICATE_TEMPLATE_HTML
            .replace("{student_name}", student_name.strip() or "Estudiante Wisrovi")
            .replace("{badge_tag}", info.get("badge", "🎓 Micro-Certificación"))
            .replace("{cert_title}", info.get("title", f"Acreditación en Clase 0{class_num}"))
            .replace("{skill_title}", info.get("skill", "Competencias Técnicas"))
            .replace("{concept_learned}", info.get("concept", "Superación de retos técnicos."))
            .replace("{course_name}", course_name)
            .replace("{class_num}", str(class_num))
            .replace("{issue_date}", issue_date)
            .replace("{cert_hash}", cert_hash)
        )
        return html

    @classmethod
    def generate_pdf(
        cls,
        student_name: str,
        output_pdf_path: str,
        course_title: str = "Programa Integral de Formación en Python: De Cero a Agentes de IA",
        hours: int = 160
    ) -> str:
        """Compila el certificado de curso completo en PDF usando Google Chrome Headless."""
        html_content = cls.generate_html(student_name, course_title, hours)
        return cls._compile_with_chrome(html_content, output_pdf_path, is_pdf=True)

    @classmethod
    def generate_class_certificate_pdf(
        cls,
        student_name: str,
        course_num: int,
        class_num: int,
        output_pdf_path: str
    ) -> str:
        """Compila el diploma específico de una clase en PDF usando Google Chrome Headless."""
        html_content = cls.generate_class_certificate_html(student_name, course_num, class_num)
        return cls._compile_with_chrome(html_content, output_pdf_path, is_pdf=True)

    @classmethod
    def generate_class_certificate_png(
        cls,
        student_name: str,
        course_num: int,
        class_num: int,
        output_png_path: str
    ) -> str:
        """Renderiza el diploma específico de una clase en PNG usando Google Chrome Headless."""
        html_content = cls.generate_class_certificate_html(student_name, course_num, class_num)
        return cls._compile_with_chrome(html_content, output_png_path, is_pdf=False)

    @classmethod
    def get_class_share_payload(
        cls,
        student_name: str,
        course_num: int,
        class_num: int
    ) -> Dict[str, Any]:
        """Retorna el paquete completo de datos y enlaces para compartir en LinkedIn."""
        info = cls.get_class_info(course_num, class_num)
        s_name = student_name.strip() or "Estudiante Wisrovi"
        
        issue_date = datetime.now().strftime("%d de %B de %Y")
        hash_seed = f"{s_name}-c{course_num}-s{class_num}-{issue_date}-wisrovi-class-cert"
        cert_hash = hashlib.sha256(hash_seed.encode("utf-8")).hexdigest()[:24].upper()
        
        linkedin_text = info.get("linkedin_text", "")
        # URL oficial para compartir
        share_url = f"https://wisrovi.github.io/wisrovi-python/curso-0{course_num}/clase-0{class_num}/"
        linkedin_intent_url = f"https://www.linkedin.com/sharing/share-offsite/?url={share_url}"
        
        return {
            "course_num": course_num,
            "class_num": class_num,
            "student_name": s_name,
            "title": info.get("title"),
            "skill": info.get("skill"),
            "concept": info.get("concept"),
            "badge": info.get("badge"),
            "cert_hash": cert_hash,
            "issue_date": issue_date,
            "linkedin_text": linkedin_text,
            "share_url": share_url,
            "linkedin_intent_url": linkedin_intent_url,
            "html": cls.generate_class_certificate_html(s_name, course_num, class_num)
        }

    @classmethod
    def _compile_with_chrome(cls, html_content: str, output_path: str, is_pdf: bool = True) -> str:
        """Helper privado para compilar HTML a PDF o capturar PNG con Chrome Headless."""
        temp_dir = tempfile.mkdtemp()
        temp_html = os.path.join(temp_dir, "cert_render.html")
        
        try:
            with open(temp_html, "w", encoding="utf-8") as f:
                f.write(html_content)
                
            os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
            
            if is_pdf:
                cmd = [
                    "google-chrome",
                    "--headless",
                    "--disable-gpu",
                    "--no-sandbox",
                    f"--print-to-pdf={output_path}",
                    temp_html
                ]
            else:
                cmd = [
                    "google-chrome",
                    "--headless",
                    "--disable-gpu",
                    "--no-sandbox",
                    f"--screenshot={output_path}",
                    "--window-size=1200,850",
                    temp_html
                ]
            
            subprocess.run(cmd, check=True)
            return output_path
        finally:
            if os.path.exists(temp_html):
                try:
                    os.remove(temp_html)
                    os.rmdir(temp_dir)
                except Exception:
                    pass
