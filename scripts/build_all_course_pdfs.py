#!/usr/bin/env python3
"""
Script de generación automatizada de PDFs educativos para todos los cursos y clases de wisrovi-python.
Genera PDFs de 9 páginas con estética LaTeX profesional, diagramas visuales, perfil de autor, código y referencias.
"""

import os
import shutil
import tempfile
import subprocess
from typing import Dict, Any, List

BASE_DIR = "/home/wisrovi/Documents/wisrovi-python"

AUTHOR_INFO = {
    "name": "William Rodríguez (Wisrovi)",
    "title": "AI Solutions Architect & Principal Software Engineer",
    "location": "Badajoz, España",
    "bio": (
        "Ingeniero y arquitecto de software especializado en Inteligencia Artificial Generativa, "
        "sistemas multi-agente, Visión por Computador e infraestructuras MLOps de alta disponibilidad. "
        "Creador y mantenedor de la suite de software libre <strong>wisrovi SUITE</strong> en PyPI con más de "
        "26 bibliotecas enfocadas en orquestación de pipelines, caching distribuido y optimización de bases de datos."
    ),
    "github": "https://github.com/wisrovi",
    "linkedin": "https://www.linkedin.com/in/wisrovi-rodriguez/",
    "dockerhub": "https://hub.docker.com/u/wisrovi",
    "website": "https://wisrovi.dev",
    "pypi": "https://pypi.org/user/wisrovi/",
    "philosophy": (
        "«La regla de la bicicleta: Nadie aprende a montar en bicicleta viendo tutoriales. "
        "El verdadero dominio de la programación surge cuando abres tu editor, escribes código "
        "con tus propias manos, resuelves errores y construyes proyectos reales.»"
    )
}

CSS_STYLE = """
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&family=Lora:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

@page {
    size: A4 portrait;
    margin: 0;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}

body {
    font-family: 'Lora', Georgia, serif;
    font-size: 9.8pt;
    line-height: 1.55;
    color: #1e293b;
    background: #ffffff;
}

.page {
    width: 210mm;
    height: 296.8mm;
    max-height: 296.8mm;
    padding: 16mm 20mm 18mm 20mm;
    position: relative;
    page-break-after: always;
    page-break-inside: avoid;
    overflow: hidden;
    background: #ffffff;
    display: flex;
    flex-direction: column;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1.5px solid #0f172a;
    padding-bottom: 5px;
    margin-bottom: 14px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 8pt;
    font-weight: 600;
    color: #475569;
    text-transform: uppercase;
    letter-spacing: 0.6px;
}

.footer {
    position: absolute;
    bottom: 10mm;
    left: 20mm;
    right: 20mm;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #cbd5e1;
    padding-top: 5px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 7.8pt;
    color: #64748b;
}

.content-body {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
}

h1, h2, h3, h4 {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 700;
    color: #0f172a;
}

h1 { font-size: 20pt; line-height: 1.2; margin-bottom: 10px; }
h2 { font-size: 13.5pt; line-height: 1.3; margin: 10px 0 6px 0; color: #1e3a8a; border-left: 3.5px solid #2563eb; padding-left: 8px; }
h3 { font-size: 10.5pt; line-height: 1.3; margin: 8px 0 4px 0; color: #0f172a; }
p { font-size: 9.3pt; line-height: 1.5; margin-bottom: 7px; text-align: justify; }

/* Portada */
.cover-page {
    justify-content: center;
    align-items: center;
    text-align: center;
    background: linear-gradient(135deg, #091322 0%, #172554 45%, #0f172a 100%);
    color: #ffffff;
    padding: 25mm 22mm;
}
.cover-page h1, .cover-page h2, .cover-page h3, .cover-page p {
    color: #ffffff;
    text-align: center;
}
.cover-badge {
    display: inline-block;
    background: rgba(59, 130, 246, 0.25);
    border: 1px solid #60a5fa;
    color: #93c5fd;
    padding: 5px 16px;
    border-radius: 20px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 8.5pt;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 22px;
}
.cover-course {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 12pt;
    font-weight: 600;
    color: #38bdf8 !important;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 12px;
}
.cover-title {
    font-size: 24pt;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 14px;
    color: #ffffff !important;
}
.cover-subtitle {
    font-size: 13pt;
    font-weight: 400;
    color: #cbd5e1 !important;
    max-width: 580px;
    margin: 0 auto 28px auto;
    font-style: italic;
}
.cover-divider {
    width: 90px;
    height: 3.5px;
    background: #3b82f6;
    margin: 0 auto 28px auto;
    border-radius: 2px;
}
.cover-meta {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 9.2pt;
    color: #94a3b8 !important;
    margin-top: 25px;
    line-height: 1.7;
}

/* Cajas de estilo LaTeX */
.callout {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 4px solid #3b82f6;
    padding: 8px 12px;
    border-radius: 4px;
    margin: 7px 0;
}
.callout-purple {
    border-left-color: #8b5cf6;
    background: #faf5ff;
}
.callout-emerald {
    border-left-color: #10b981;
    background: #f0fdf4;
}
.callout-amber {
    border-left-color: #f59e0b;
    background: #fffbeb;
}
.callout-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 700;
    font-size: 9pt;
    color: #1e3a8a;
    margin-bottom: 3px;
    display: flex;
    align-items: center;
    gap: 5px;
}
.callout p { font-size: 8.8pt; line-height: 1.45; margin-bottom: 0; color: #334155; }

/* Bloques de código */
.code-wrapper {
    margin: 8px 0;
    border-radius: 6px;
    overflow: hidden;
    border: 1px solid #334155;
    background: #0f172a;
}
.code-header {
    background: #1e293b;
    padding: 4px 10px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 7.5pt;
    font-weight: 600;
    color: #94a3b8;
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid #334155;
}
.code-box {
    padding: 8px 12px;
    font-family: 'Fira Code', monospace;
    font-size: 8pt;
    line-height: 1.45;
    color: #f8fafc;
    white-space: pre-wrap;
    overflow-x: auto;
}
.kw { color: #f43f5e; font-weight: 600; }
.fn { color: #38bdf8; font-weight: 500; }
.st { color: #4ade80; }
.cm { color: #94a3b8; font-style: italic; }
.nu { color: #fbbf24; }
.op { color: #cbd5e1; }
.bi { color: #c084fc; font-weight: 600; }

/* Tablas */
.styled-table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 8.2pt;
}
.styled-table th {
    background: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
    padding: 6px 8px;
    text-align: left;
    border-top: 1.5px solid #0f172a;
    border-bottom: 1.5px solid #0f172a;
}
.styled-table td {
    padding: 6px 8px;
    border-bottom: 1px solid #e2e8f0;
    color: #334155;
}
.styled-table tr:nth-child(even) {
    background: #f8fafc;
}

/* Tarjeta de autor */
.author-card {
    background: #f8fafc;
    border: 1.5px solid #e2e8f0;
    border-radius: 8px;
    padding: 14px 16px;
    margin: 8px 0;
}
.author-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 10px;
}
.author-avatar {
    width: 54px;
    height: 54px;
    border-radius: 50%;
    background: #1e293b;
    color: #38bdf8;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18pt;
    font-weight: bold;
    border: 2px solid #3b82f6;
    font-family: 'Plus Jakarta Sans', sans-serif;
}
.author-info h3 { font-size: 13pt; margin: 0; color: #0f172a; }
.author-info p { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 8.5pt; color: #64748b; margin: 0; }

.link-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-top: 10px;
}
.link-item {
    background: #ffffff;
    border: 1px solid #cbd5e1;
    padding: 7px 10px;
    border-radius: 5px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 8pt;
    color: #1e293b;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* Diagramas SVG */
.diagram-container {
    width: 100%;
    margin: 8px 0;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
}
.diagram-container svg {
    max-width: 100%;
    height: auto;
}

.two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 8px 0;
}
"""

def generate_svg_diagram(diagram_type: str, title: str, subtitle: str) -> str:
    """Genera diagramas SVG limpios y vectoriales con estética Mermaid profesional."""
    
    if diagram_type == "flow":
        return f"""
        <svg viewBox="0 0 650 180" width="100%" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#3b82f6"/>
                </marker>
            </defs>
            <!-- Nodos -->
            <rect x="15" y="65" width="120" height="50" rx="8" fill="#1e293b" stroke="#3b82f6" stroke-width="2"/>
            <text x="75" y="95" fill="#f8fafc" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600" text-anchor="middle">Inicio / Entrada</text>
            
            <line x1="135" y1="90" x2="175" y2="90" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow)"/>
            
            <polygon points="240,55 300,90 240,125 180,90" fill="#0f766e" stroke="#2dd4bf" stroke-width="2"/>
            <text x="240" y="94" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="600" text-anchor="middle">¿Condición?</text>
            
            <line x1="300" y1="90" x2="345" y2="90" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow)"/>
            <text x="322" y="82" fill="#059669" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="bold">Sí (True)</text>
            
            <rect x="350" y="65" width="130" height="50" rx="8" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2"/>
            <text x="415" y="95" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600" text-anchor="middle">Procesamiento</text>
            
            <line x1="480" y1="90" x2="520" y2="90" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrow)"/>
            
            <rect x="525" y="65" width="110" height="50" rx="8" fill="#065f46" stroke="#34d399" stroke-width="2"/>
            <text x="580" y="95" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600" text-anchor="middle">Resultado Final</text>
            
            <!-- Camino No (False) -->
            <path d="M 240 125 L 240 155 L 415 155 L 415 120" fill="none" stroke="#e11d48" stroke-width="1.8" stroke-dasharray="4,4" marker-end="url(#arrow)"/>
            <text x="325" y="150" fill="#e11d48" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" font-weight="bold">No (Bypass / Else)</text>
        </svg>
        """
    elif diagram_type == "architecture":
        return f"""
        <svg viewBox="0 0 650 180" width="100%" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <marker id="arrow2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#6366f1"/>
                </marker>
            </defs>
            <!-- Capa Cliente / Entrada -->
            <rect x="15" y="30" width="130" height="120" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.5"/>
            <text x="80" y="55" fill="#0f172a" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700" text-anchor="middle">Capa Entrada</text>
            <rect x="25" y="70" width="110" height="32" rx="4" fill="#3b82f6" />
            <text x="80" y="90" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" text-anchor="middle">Input / Prompt / UI</text>
            <rect x="25" y="110" width="110" height="28" rx="4" fill="#0284c7" />
            <text x="80" y="128" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" text-anchor="middle">Validación Datos</text>
            
            <line x1="145" y1="90" x2="195" y2="90" stroke="#6366f1" stroke-width="2" marker-end="url(#arrow2)"/>
            
            <!-- Capa Lógica / Agente / Motor -->
            <rect x="200" y="20" width="240" height="140" rx="10" fill="#ede9fe" stroke="#8b5cf6" stroke-width="2"/>
            <text x="320" y="45" fill="#5b21b6" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="700" text-anchor="middle">Núcleo de Ejecución / Lógica</text>
            <rect x="215" y="60" width="210" height="40" rx="6" fill="#6d28d9"/>
            <text x="320" y="85" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="600" text-anchor="middle">Motor / Algoritmo / LLM</text>
            <rect x="215" y="110" width="100" height="35" rx="4" fill="#7c3aed"/>
            <text x="265" y="132" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" text-anchor="middle">Memoria / Estado</text>
            <rect x="325" y="110" width="100" height="35" rx="4" fill="#7c3aed"/>
            <text x="375" y="132" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" text-anchor="middle">Herramientas / DB</text>
            
            <line x1="440" y1="90" x2="490" y2="90" stroke="#6366f1" stroke-width="2" marker-end="url(#arrow2)"/>
            
            <!-- Capa Salida / Persistencia -->
            <rect x="495" y="30" width="140" height="120" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.5"/>
            <text x="565" y="55" fill="#0f172a" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700" text-anchor="middle">Capa Persistencia</text>
            <rect x="505" y="70" width="120" height="32" rx="4" fill="#059669"/>
            <text x="565" y="90" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="9.5" text-anchor="middle">DB / Vector Store</text>
            <rect x="505" y="110" width="120" height="28" rx="4" fill="#047857"/>
            <text x="565" y="128" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" text-anchor="middle">Respuesta Formateada</text>
        </svg>
        """
    elif diagram_type == "loop":
        return f"""
        <svg viewBox="0 0 650 170" width="100%" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <marker id="arrow3" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                    <path d="M 0 1 L 10 5 L 0 9 z" fill="#0284c7"/>
                </marker>
            </defs>
            <rect x="20" y="60" width="110" height="45" rx="6" fill="#1e293b"/>
            <text x="75" y="87" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Colección / Rango</text>
            
            <line x1="130" y1="82" x2="175" y2="82" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow3)"/>
            
            <rect x="180" y="45" width="130" height="75" rx="8" fill="#0369a1" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="245" y="75" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700" text-anchor="middle">Iterador (for/while)</text>
            <text x="245" y="95" fill="#e0f2fe" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" text-anchor="middle">Extrae siguiente elemento</text>
            
            <line x1="310" y1="82" x2="355" y2="82" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow3)"/>
            
            <rect x="360" y="45" width="140" height="75" rx="8" fill="#047857" stroke="#34d399" stroke-width="1.5"/>
            <text x="430" y="75" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700" text-anchor="middle">Cuerpo del Bucle</text>
            <text x="430" y="95" fill="#d1fae5" font-family="'Plus Jakarta Sans', sans-serif" font-size="9" text-anchor="middle">Ejecuta bloque de código</text>
            
            <!-- Flecha de retorno del ciclo -->
            <path d="M 430 45 L 430 20 L 245 20 L 245 40" fill="none" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow3)"/>
            <text x="337" y="15" fill="#d97706" font-family="'Plus Jakarta Sans', sans-serif" font-size="8.5" font-weight="bold">Siguiente iteración (Loop)</text>
            
            <line x1="500" y1="82" x2="540" y2="82" stroke="#0284c7" stroke-width="2" marker-end="url(#arrow3)"/>
            
            <rect x="545" y="60" width="90" height="45" rx="6" fill="#334155"/>
            <text x="590" y="87" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="10.5" font-weight="600" text-anchor="middle">Fin del Bucle</text>
        </svg>
        """
    else:
        return f"""
        <svg viewBox="0 0 650 170" width="100%" xmlns="http://www.w3.org/2000/svg">
            <rect x="20" y="30" width="610" height="110" rx="8" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="325" y="70" fill="#1e3a8a" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="700" text-anchor="middle">{title}</text>
            <text x="325" y="100" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" text-anchor="middle">{subtitle}</text>
        </svg>
        """

def build_class_html(meta: Dict[str, Any]) -> str:
    """Construye las 9 páginas HTML completas con estilo LaTeX para una clase."""
    
    course_name = meta["course_name"]
    course_num = meta["course_num"]
    class_title = meta["class_title"]
    class_code = meta["class_code"]
    metaphor = meta["metaphor"]
    level = meta["level"]
    
    # 9 Páginas completas
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>{class_title} - {course_name}</title>
<style>
{CSS_STYLE}
</style>
</head>
<body>

<!-- ========================================== -->
<!-- PÁGINA 1: PORTADA OFICIAL                  -->
<!-- ========================================== -->
<div class="page cover-page">
    <div class="cover-badge">Programa Integral de Formación en Python</div>
    <div class="cover-course">{course_name} (Nivel {course_num})</div>
    <div class="cover-title">{class_title}</div>
    <div class="cover-subtitle">«{metaphor}»</div>
    <div class="cover-divider"></div>
    <p style="max-width: 520px; color: #cbd5e1; font-size: 10pt; font-style: italic; line-height: 1.6;">
        {meta["description"]}
    </p>
    <div class="cover-meta">
        <strong>Instructor:</strong> {AUTHOR_INFO["name"]}<br>
        <strong>Rol:</strong> {AUTHOR_INFO["title"]}<br>
        <strong>Nivel del Curso:</strong> {level} &nbsp;|&nbsp; <strong>Python:</strong> 3.10+ &nbsp;|&nbsp; <strong>Licencia:</strong> MIT
    </div>
</div>

<!-- ========================================== -->
<!-- PÁGINA 2: PRESENTACIÓN DEL AUTOR / MENTOR  -->
<!-- ========================================== -->
<div class="page">
    <div class="header">
        <span>{course_name} &bull; {class_code}</span>
        <span>Perfil del Instructor</span>
    </div>
    <div class="content-body">
        <h2>Acerca del Autor y Mentor</h2>
        <div class="author-card">
            <div class="author-header">
                <div class="author-avatar">WR</div>
                <div class="author-info">
                    <h3>{AUTHOR_INFO["name"]}</h3>
                    <p>{AUTHOR_INFO["title"]} &bull; {AUTHOR_INFO["location"]}</p>
                </div>
            </div>
            <p style="font-size: 8.8pt; line-height: 1.5; color: #334155;">
                {AUTHOR_INFO["bio"]}
            </p>
            <div class="link-grid">
                <div class="link-item">🐙 <strong>GitHub:</strong> github.com/wisrovi</div>
                <div class="link-item">💼 <strong>LinkedIn:</strong> in/wisrovi-rodriguez</div>
                <div class="link-item">🐳 <strong>DockerHub:</strong> hub.docker.com/u/wisrovi</div>
                <div class="link-item">🌐 <strong>Website:</strong> wisrovi.dev</div>
            </div>
        </div>

        <h2>Metodología de Aprendizaje: La Regla de la Bicicleta 🚲</h2>
        <p>
            En este programa no creemos en el aprendizaje pasivo. Programar no se aprende memorizando manuales o mirando videos en segundo plano mientras tomas café; se aprende <strong>escribiendo código</strong>, enfrentando errores de sintaxis, depurando variables y viendo cómo responde el intérprete en tiempo real.
        </p>

        <div class="callout callout-emerald">
            <div class="callout-title">💡 El Compromiso Activo del Estudiante</div>
            <p>
                Abre Visual Studio Code en cada sesión. Escribe cada ejemplo con tus propias manos. Cambia los números, rompe el código deliberadamente para ver el mensaje de error de Python, y luego arréglalo. Ese proceso de experimentación es el que construye sinapsis duraderas.
            </p>
        </div>

        <h2>Estructura Pedagógica de Cada Guía</h2>
        <p>
            Cada documento de esta serie está diseñado rigurosamente bajo el estándar de ingeniería de software profesional:
        </p>
        <ul style="font-size: 8.8pt; line-height: 1.5; margin-left: 20px; color: #334155;">
            <li><strong>Fundamento Conceptual y Metáfora Intuitiva:</strong> Anclaje visual del concepto abstracto a la realidad.</li>
            <li><strong>Diagrama de Flujo y Arquitectura Mental:</strong> Representación visual de cómo fluye la información.</li>
            <li><strong>Código de Nivel Profesional:</strong> Sintaxis limpia, comentarios línea a línea y tipado estático (PEP 484).</li>
            <li><strong>Patrones y Gotchas:</strong> Errores comunes que cometen los desarrolladores y cómo evitarlos.</li>
        </ul>
    </div>
    <div class="footer">
        <span>{course_name} &bull; {class_title}</span>
        <span>Página 2 de 9</span>
    </div>
</div>

<!-- ========================================== -->
<!-- PÁGINA 3: TABLA DE CONTENIDOS Y OBJETIVOS  -->
<!-- ========================================== -->
<div class="page">
    <div class="header">
        <span>{course_name} &bull; {class_code}</span>
        <span>Tabla de Contenidos & Objetivos</span>
    </div>
    <div class="content-body">
        <h2>Índice General de la Sesión</h2>
        <table class="styled-table">
            <thead>
                <tr>
                    <th style="width: 15%;">Sección</th>
                    <th style="width: 65%;">Contenido y Enfoque Temático</th>
                    <th style="width: 20%; text-align: right;">Página</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Capítulo 1</strong></td>
                    <td><strong>Fundamentos y Metáfora Conceptual:</strong> {meta["p4_title"]}</td>
                    <td style="text-align: right;">Pág. 4</td>
                </tr>
                <tr>
                    <td><strong>Capítulo 2</strong></td>
                    <td><strong>Diagrama de Flujo y Arquitectura:</strong> {meta["p5_title"]}</td>
                    <td style="text-align: right;">Pág. 5</td>
                </tr>
                <tr>
                    <td><strong>Capítulo 3</strong></td>
                    <td><strong>Implementación Práctica en Python:</strong> {meta["p6_title"]}</td>
                    <td style="text-align: right;">Pág. 6</td>
                </tr>
                <tr>
                    <td><strong>Capítulo 4</strong></td>
                    <td><strong>Patrones Avanzados, Gotchas y Debugging:</strong> {meta["p7_title"]}</td>
                    <td style="text-align: right;">Pág. 7</td>
                </tr>
                <tr>
                    <td><strong>Cierre</strong></td>
                    <td><strong>Conclusiones, Notas del Mentor y Agradecimiento</strong></td>
                    <td style="text-align: right;">Pág. 8</td>
                </tr>
                <tr>
                    <td><strong>Anexos</strong></td>
                    <td><strong>Bibliografía Oficial y Enlaces de Profundización</strong></td>
                    <td style="text-align: right;">Pág. 9</td>
                </tr>
            </tbody>
        </table>

        <h2>Objetivos de Aprendizaje (Competencias Clave)</h2>
        <div class="two-col">
            <div class="callout">
                <div class="callout-title">🎯 Competencia Conceptual</div>
                <p>{meta["obj_conceptual"]}</p>
            </div>
            <div class="callout callout-purple">
                <div class="callout-title">🛠️ Competencia Práctica</div>
                <p>{meta["obj_practical"]}</p>
            </div>
        </div>

        <h2>Requisitos Previos y Entorno Recomendado</h2>
        <p style="font-size: 8.8pt; color: #475569;">
            Para aprovechar al máximo esta sesión se recomienda tener instalado Python 3.10 o superior, Visual Studio Code con la extensión oficial de Python configurada, y haber completado las lecturas y ejercicios de las sesiones anteriores de la ruta formativa.
        </p>
    </div>
    <div class="footer">
        <span>{course_name} &bull; {class_title}</span>
        <span>Página 3 de 9</span>
    </div>
</div>

<!-- ========================================== -->
<!-- PÁGINA 4: TEORÍA Y METÁFORA CONCEPTUAL     -->
<!-- ========================================== -->
<div class="page">
    <div class="header">
        <span>{course_name} &bull; {class_code}</span>
        <span>01. Fundamento y Metáfora</span>
    </div>
    <div class="content-body">
        <h2>1. {meta["p4_title"]}</h2>
        <p>{meta["p4_intro"]}</p>

        <div class="callout callout-amber">
            <div class="callout-title">🌟 Metáfora Central: {meta["metaphor"]}</div>
            <p>{meta["p4_metaphor_desc"]}</p>
        </div>

        <h3>Principios Teóricos y Modelo Mental</h3>
        <p>{meta["p4_theory_1"]}</p>
        <p>{meta["p4_theory_2"]}</p>

        <div class="callout callout-emerald">
            <div class="callout-title">⚡ Regla de Oro en Python</div>
            <p>{meta["p4_golden_rule"]}</p>
        </div>
    </div>
    <div class="footer">
        <span>{course_name} &bull; {class_title}</span>
        <span>Página 4 de 9</span>
    </div>
</div>

<!-- ========================================== -->
<!-- PÁGINA 5: DIAGRAMA DE FLUJO Y ARQUITECTURA -->
<!-- ========================================== -->
<div class="page">
    <div class="header">
        <span>{course_name} &bull; {class_code}</span>
        <span>02. Arquitectura de Flujo</span>
    </div>
    <div class="content-body">
        <h2>2. {meta["p5_title"]}</h2>
        <p>{meta["p5_desc"]}</p>

        <div class="diagram-container">
            {generate_svg_diagram(meta.get("diagram_type", "flow"), meta["class_title"], meta["metaphor"])}
        </div>

        <h3>Desglose Paso a Paso del Diagrama</h3>
        <table class="styled-table">
            <thead>
                <tr>
                    <th style="width: 25%;">Fase del Flujo</th>
                    <th style="width: 45%;">Acción del Intérprete</th>
                    <th style="width: 30%;">Estado en Memoria</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>1. Inicialización</strong></td>
                    <td>{meta["p5_step1_action"]}</td>
                    <td>{meta["p5_step1_state"]}</td>
                </tr>
                <tr>
                    <td><strong>2. Evaluación</strong></td>
                    <td>{meta["p5_step2_action"]}</td>
                    <td>{meta["p5_step2_state"]}</td>
                </tr>
                <tr>
                    <td><strong>3. Transformación</strong></td>
                    <td>{meta["p5_step3_action"]}</td>
                    <td>{meta["p5_step3_state"]}</td>
                </tr>
                <tr>
                    <td><strong>4. Retorno / Salida</strong></td>
                    <td>{meta["p5_step4_action"]}</td>
                    <td>{meta["p5_step4_state"]}</td>
                </tr>
            </tbody>
        </table>

        <div class="callout">
            <div class="callout-title">🔍 Visualización Mental</div>
            <p>{meta["p5_mental_tip"]}</p>
        </div>
    </div>
    <div class="footer">
        <span>{course_name} &bull; {class_title}</span>
        <span>Página 5 de 9</span>
    </div>
</div>

<!-- ========================================== -->
<!-- PÁGINA 6: CÓDIGO PYTHON PROFESIONAL        -->
<!-- ========================================== -->
<div class="page">
    <div class="header">
        <span>{course_name} &bull; {class_code}</span>
        <span>03. Implementación Práctica</span>
    </div>
    <div class="content-body">
        <h2>3. {meta["p6_title"]}</h2>
        <p>{meta["p6_desc"]}</p>

        <div class="code-wrapper">
            <div class="code-header">
                <span>main.py (Python 3.10+)</span>
                <span>UTF-8 &bull; PEP 8 Compliant</span>
            </div>
            <div class="code-box">{meta["p6_code"]}</div>
        </div>

        <h3>Análisis del Código Fuente</h3>
        <p style="font-size: 8.8pt;">{meta["p6_code_analysis"]}</p>
    </div>
    <div class="footer">
        <span>{course_name} &bull; {class_title}</span>
        <span>Página 6 de 9</span>
    </div>
</div>

<!-- ========================================== -->
<!-- PÁGINA 7: PATRONES, GOTCHAS Y DEBUGGING    -->
<!-- ========================================== -->
<div class="page">
    <div class="header">
        <span>{course_name} &bull; {class_code}</span>
        <span>04. Buenas Prácticas y Gotchas</span>
    </div>
    <div class="content-body">
        <h2>4. {meta["p7_title"]}</h2>
        <p>{meta["p7_intro"]}</p>

        <div class="callout callout-amber">
            <div class="callout-title">⚠️ Gotcha Frecuente (Trampa de Principiante)</div>
            <p>{meta["p7_gotcha"]}</p>
        </div>

        <h3>Patrón Recomendado vs Antipatrón</h3>
        <div class="two-col">
            <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 6px; padding: 8px;">
                <div style="color: #991b1b; font-weight: bold; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 8.5pt; margin-bottom: 4px;">❌ Antipatrón / Mal Código</div>
                <div style="font-family: 'Fira Code', monospace; font-size: 7.5pt; color: #7f1d1d; white-space: pre-wrap;">{meta["p7_bad_code"]}</div>
            </div>
            <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 6px; padding: 8px;">
                <div style="color: #166534; font-weight: bold; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 8.5pt; margin-bottom: 4px;">✅ Patrón Pythonic / Correcto</div>
                <div style="font-family: 'Fira Code', monospace; font-size: 7.5pt; color: #14532d; white-space: pre-wrap;">{meta["p7_good_code"]}</div>
            </div>
        </div>

        <div class="callout callout-purple">
            <div class="callout-title">🛡️ Consejo de Resiliencia en Producción</div>
            <p>{meta["p7_pro_tip"]}</p>
        </div>
    </div>
    <div class="footer">
        <span>{course_name} &bull; {class_title}</span>
        <span>Página 7 de 9</span>
    </div>
</div>

<!-- ========================================== -->
<!-- PÁGINA 8: CONCLUSIONES Y AGRADECIMIENTO    -->
<!-- ========================================== -->
<div class="page">
    <div class="header">
        <span>{course_name} &bull; {class_code}</span>
        <span>05. Conclusiones y Cierre</span>
    </div>
    <div class="content-body">
        <h2>5. Resumen Ejecutivo y Conclusiones</h2>
        <p>{meta["p8_summary"]}</p>

        <div class="callout callout-emerald">
            <div class="callout-title">🏆 Logro Alcanzado en esta Clase</div>
            <p>{meta["p8_achievement"]}</p>
        </div>

        <h2>Notas del Instructor y Siguientes Pasos</h2>
        <p>{meta["p8_instructor_notes"]}</p>

        <div class="callout">
            <div class="callout-title">🤝 Mensaje de Agradecimiento</div>
            <p>
                Muchas gracias por tu entusiasmo, disciplina y dedicación al participar en este programa formativo.
                La programación es un superpoder que transforma vidas cuando se ejerce con constancia y curiosidad.
                ¡Nos vemos en la próxima sesión para seguir construyendo juntos!
            </p>
        </div>

        <p style="text-align: center; font-style: italic; color: #64748b; margin-top: 15px; font-size: 9pt;">
            «El código más elegante es aquel que cualquiera puede entender y nadie necesita reescribir.»
        </p>
    </div>
    <div class="footer">
        <span>{course_name} &bull; {class_title}</span>
        <span>Página 8 de 9</span>
    </div>
</div>

<!-- ========================================== -->
<!-- PÁGINA 9: BIBLIOGRAFÍA Y ENLACES OFICIALES -->
<!-- ========================================== -->
<div class="page">
    <div class="header">
        <span>{course_name} &bull; {class_code}</span>
        <span>06. Bibliografía y Recursos</span>
    </div>
    <div class="content-body">
        <h2>6. Fuentes Bibliográficas y Recursos de Estudio</h2>
        <p>Para profundizar y consolidar los conocimientos adquiridos en esta clase, consulta las siguientes referencias:</p>

        <table class="styled-table">
            <thead>
                <tr>
                    <th style="width: 30%;">Recurso / Fuente</th>
                    <th style="width: 45%;">Descripción Temática</th>
                    <th style="width: 25%;">Enlace Oficial</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Documentación Oficial de Python</strong></td>
                    <td>Referencia canónica del lenguaje y librería estándar</td>
                    <td><a href="https://docs.python.org/3/" style="color: #2563eb;">docs.python.org/3/</a></td>
                </tr>
                <tr>
                    <td><strong>PEP 8 - Style Guide for Python</strong></td>
                    <td>Guía oficial de estilo, formato e indentación</td>
                    <td><a href="https://peps.python.org/pep-0008/" style="color: #2563eb;">peps.python.org</a></td>
                </tr>
                <tr>
                    <td><strong>Real Python Tutorials</strong></td>
                    <td>Artículos técnicos y patrones de desarrollo moderno</td>
                    <td><a href="https://realpython.com/" style="color: #2563eb;">realpython.com</a></td>
                </tr>
                <tr>
                    <td><strong>Python Type Checking (PEP 484)</strong></td>
                    <td>Anotaciones de tipo y análisis estático en Python</td>
                    <td><a href="https://docs.python.org/3/library/typing.html" style="color: #2563eb;">docs.python.org/typing</a></td>
                </tr>
                <tr>
                    <td><strong>Suite Open Source wisrovi</strong></td>
                    <td>Paquetes Python para orquestación y alto rendimiento</td>
                    <td><a href="https://github.com/wisrovi" style="color: #2563eb;">github.com/wisrovi</a></td>
                </tr>
            </tbody>
        </table>

        <h2>Canales de Consulta y Comunidad</h2>
        <p style="font-size: 8.8pt; color: #334155;">
            Si encuentras dificultades al replicar el código o tienes dudas sobre la arquitectura de los ejercicios, no dudes en abrir un Issue en el repositorio oficial del curso en GitHub o participar activamente en nuestras sesiones grupales de mentoría.
        </p>

        <div class="callout callout-purple">
            <div class="callout-title">📚 Desafío de Autoestudio Recomendado</div>
            <p>{meta["p9_challenge"]}</p>
        </div>
    </div>
    <div class="footer">
        <span>{course_name} &bull; {class_title}</span>
        <span>Página 9 de 9</span>
    </div>
</div>

</body>
</html>
"""
    return html

CLASSES_METADATA = [
    # -------------------------------------------------------------
    # CURSO 1: FUNDAMENTOS DE PYTHON
    # -------------------------------------------------------------
    {
        "target_dir": f"{BASE_DIR}/01-fundamentos-python/clase-01-panorama-general",
        "pdf_filename": "clase-01-panorama-general.pdf",
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "course_num": "1 (Principiantes)",
        "class_title": "Clase 01: El Panorama General de la Programación",
        "class_code": "Clase 01",
        "level": "Principiante Absoluto",
        "metaphor": "El Asistente, las Cajas, el Semáforo y la Licuadora",
        "description": "Una inmersión panorámica e intuitiva a los 4 pilares fundamentales del pensamiento lógico de un programador: Variables, Condicionales, Bucles y Funciones.",
        "diagram_type": "flow",
        "obj_conceptual": "Comprender que programar es dar instrucciones secuenciales precisas y dominar la función mental de los 4 pilares.",
        "obj_practical": "Ejecutar tu primer script en VS Code usando print(), variables, condicionales if y funciones def.",
        "p4_title": "Los Cuatro Pilares Fundamentales del Software",
        "p4_intro": "Toda aplicación moderna, desde un script de automatización hasta una Inteligencia Artificial, está construida sobre cuatro bloques lógicos elementales.",
        "p4_metaphor_desc": "Imagina que la computadora es un asistente súper eficiente pero literal: las variables son cajas etiquetadas donde guarda cosas, el if es un semáforo que decide el camino según la luz, el for es una cinta transportadora que procesa elementos uno a uno, y la función def es una licuadora que recibe ingredientes y entrega un licuado.",
        "p4_theory_1": "1. Variables (Memoria): Espacios con nombre para retener datos temporalmente. 2. Condicionales (Decisión): Bifurcaciones lógicas según condiciones booleanas. 3. Bucles (Repetición): Automatización de tareas repetitivas sin duplicar código. 4. Funciones (Modularidad): Bloques reutilizables con entradas y salidas bien definidas.",
        "p4_theory_2": "La magia del software no radica en la complejidad de cada pieza aislada, sino en la sinergia con la que se combinan para modelar la realidad.",
        "p4_golden_rule": "Python es un lenguaje interpretado, de tipado dinámico y fuertemente tipado: respeta la indentación y la semántica.",
        "p5_title": "Diagrama de Ejecución Secuencial y Control",
        "p5_desc": "Cómo el intérprete de Python procesa el código línea por línea desde el punto de entrada hasta la resolución.",
        "p5_step1_action": "Lee la instrucción inicial e inicializa el entorno de variables en memoria.",
        "p5_step1_state": "Tabla de símbolos vacía -> asigna valores",
        "p5_step2_action": "Evalúa expresiones booleanas en condicionales para determinar la ruta.",
        "p5_step2_state": "Evalúa True o False en CPU",
        "p5_step3_action": "Ejecuta el bloque indentado correspondiente a la condición satisfecha.",
        "p5_step3_state": "Transformación de variables",
        "p5_step4_action": "Invoca funciones y devuelve el resultado a la consola con print().",
        "p5_step4_state": "Liberación de stack frame",
        "p5_mental_tip": "Piensa en el intérprete de Python como un lector con un marcador que avanza de arriba a abajo, saltando sólo cuando encuentra estructuras de control.",
        "p6_title": "Script Integrador de los 4 Pilares",
        "p6_desc": "Código autónomo que demuestra la interacción armónica entre variables, condicionales, bucles y funciones:",
        "p6_code": '<span class="cm"># 1. Definición de Función Reutilizable (La Licuadora)</span>\n<span class="kw">def</span> <span class="fn">evaluar_estudiante</span>(nombre: <span class="bi">str</span>, nota: <span class="bi">float</span>) -> <span class="bi">str</span>:\n    <span class="kw">if</span> nota >= <span class="nu">7.0</span>:\n        <span class="kw">return</span> <span class="st">f"¡Felicidades {nombre}! Aprobaste con éxito 🚀"</span>\n    <span class="kw">else</span>:\n        <span class="kw">return</span> <span class="st">f"Ánimo {nombre}, debes reforzar los conceptos 📚"</span>\n\n<span class="cm"># 2. Variables y Colección (Cajas en memoria)</span>\nestudiantes = [<span class="st">"Ana"</span>, <span class="st">"Carlos"</span>, <span class="st">"Sofía"</span>]\ncalificaciones = [<span class="nu">9.5</span>, <span class="nu">5.8</span>, <span class="nu">8.2</span>]\n\n<span class="cm"># 3. Bucle de Procesamiento (Cinta Transportadora)</span>\n<span class="kw">for</span> i <span class="kw">in</span> <span class="bi">range</span>(<span class="bi">len</span>(estudiantes)):\n    resultado = <span class="fn">evaluar_estudiante</span>(estudiantes[i], calificaciones[i])\n    <span class="bi">print</span>(resultado)',
        "p6_code_analysis": "El código define una función pura con type hints, itera una colección de datos mediante un bucle for y delega la toma de decisiones al condicional interno.",
        "p7_title": "Buenas Prácticas, Gotchas y Depuración",
        "p7_intro": "Consejos clave para evitar los errores más comunes al dar tus primeros pasos en Python:",
        "p7_gotcha": "Olvidar los dos puntos (:) al final de las estructuras if, for o def, o mezclar espacios y tabulaciones en la indentación.",
        "p7_bad_code": "if nota > 5\nprint(\"Aprobado\") # Error de sintaxis",
        "p7_good_code": "if nota > 5:\n    print(\"Aprobado\") # Correcto e indentado",
        "p7_pro_tip": "Configura VS Code para insertar 4 espacios automáticos al presionar la tecla Tab y activa el formateador black o ruff.",
        "p8_summary": "Has adquirido el mapa completo del territorio de la programación. Ya conoces los 4 pilares y cómo se coordinan.",
        "p8_achievement": "Primer script integrador ejecutado con éxito y comprensión clara del flujo lógico.",
        "p8_instructor_notes": "En la próxima sesión profundizaremos en el Almacén de Datos: tipos primitivos, conversión de tipos e interacción con el usuario mediante input().",
        "p9_challenge": "Modifica el script de la página 6 para que evalúe a 5 alumnos y clasifique notas con honores (mayores a 9.0)."
    },

    {
        "target_dir": f"{BASE_DIR}/01-fundamentos-python/clase-02-variables-y-tipos",
        "pdf_filename": "clase-02-variables-y-tipos.pdf",
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "course_num": "1 (Principiantes)",
        "class_title": "Clase 02: Variables, Tipos de Datos y Funciones",
        "class_code": "Clase 02",
        "level": "Principiante Absoluto",
        "metaphor": "El Almacén de Cajas en Memoria y la Licuadora Tipada",
        "description": "Dominio de la memoria Heap en Python: tipos primitivos (str, int, float, bool), paso de parámetros a funciones con Type Hints (PEP 484) y casting.",
        "diagram_type": "flow",
        "obj_conceptual": "Comprender la asignación por referencia en el Heap de memoria, inmutabilidad y contratos de funciones con Type Hints.",
        "obj_practical": "Construir funciones modulares tipadas que soliciten datos, ejecuten conversiones seguras y devuelvan resultados formateados.",
        "p4_title": "El Almacén de Datos y la Memoria de la Computadora",
        "p4_intro": "En Python, las variables no contienen datos directamente; son identificadores que apuntan a objetos en la memoria Heap.",
        "p4_metaphor_desc": "Imagina un almacén con cajas etiquetadas (variables) y una licuadora modular (funciones). La licuadora recibe ingredientes tipados (parámetros str, float, int), procesa la mezcla mediante casting y entrega una nueva caja con el resultado.",
        "p4_theory_1": "Python es fuertemente tipado: no realiza conversiones implícitas incompatibles. Los tipos primitivos (int, float, str, bool) son inmutables.",
        "p4_theory_2": "Al conectar variables con funciones tipadas (PEP 484), creamos transformaciones seguras, documentadas y fácilmente depurables.",
        "p4_golden_rule": "Convierte tipos explícitamente con int() o float() y anota siempre los tipos de parámetros y retornos en tus funciones.",
        "p5_title": "Ciclo de Transformación, Casting y Retorno",
        "p5_desc": "Flujo de recepción de datos textuales, paso de referencias a funciones, casting numérico y retorno en Heap.",
        "p5_step1_action": "La función input() captura la entrada del usuario como string en memoria.",
        "p5_step1_state": "Buffer de entrada -> '45.90' (str)",
        "p5_step2_action": "Paso de referencia a la función modular calcular_precio_total().",
        "p5_step2_state": "Parámetros locales reciben punteros del Heap",
        "p5_step3_action": "Casting explícito float() e int() y cálculo matemático con impuestos.",
        "p5_step3_state": "Nuevo objeto float instanciado en Heap",
        "p5_step4_action": "return entrega el resultado y f-string proyecta el resumen en pantalla.",
        "p5_step4_state": "Render formateado en consola",
        "p5_mental_tip": "Siempre encapsula tus operaciones de cálculo y casting en funciones puras para facilitar la verificación con pruebas unitarias.",
        "p6_title": "Calculadora Financiera Modular con Type Hints",
        "p6_desc": "Programa modular que define funciones con anotaciones de tipo, realiza casting seguro y formatea con f-strings:",
        "p6_code": '<span class="cm"># 1. Función Modular con Type Hints (PEP 484)</span>\n<span class="kw">def</span> <span class="fn">calcular_total_pedido</span>(precio_str: <span class="bi">str</span>, cantidad_str: <span class="bi">str</span>, tasa_iva: <span class="bi">float</span> = <span class="nu">0.21</span>) -> <span class="bi">float</span>:\n    <span class="st">"""Castea entradas de texto a float/int y calcula el monto total con IVA."""</span>\n    precio: <span class="bi">float</span> = <span class="bi">float</span>(precio_str)\n    unidades: <span class="bi">int</span> = <span class="bi">int</span>(cantidad_str)\n    subtotal: <span class="bi">float</span> = precio * unidades\n    total_con_iva: <span class="bi">float</span> = subtotal * (<span class="nu">1.0</span> + tasa_iva)\n    <span class="kw">return</span> <span class="bi">round</span>(total_con_iva, <span class="nu">2</span>)\n\n<span class="cm"># 2. Invocación del flujo de cálculo</span>\nprecio_input: <span class="bi">str</span> = <span class="st">"45.90"</span>\ncantidad_input: <span class="bi">str</span> = <span class="st">"3"</span>\ntotal_pagar: <span class="bi">float</span> = <span class="fn">calcular_total_pedido</span>(precio_input, cantidad_input)\n\n<span class="bi">print</span>(<span class="st">f"Total a Pagar: ${total_pagar:,.2f}"</span>)',
        "p6_code_analysis": "La función declara contratos estrictos de tipo (precio_str: str -> float), realiza casting explícito y devuelve un valor redondeado listo para producción.",
        "p7_title": "Trampas Clásicas con Variables y Casting",
        "p7_intro": "Errores comunes de principiantes al trabajar con tipos de datos y parámetros:",
        "p7_gotcha": "Intentar sumar directamente cadenas con números ('10' + 5) generando TypeError, o no convertir entradas antes de operar.",
        "p7_bad_code": "precio = input('Precio: ')\ntotal = precio * 2 # Concatena: '1010'",
        "p7_good_code": "def calcular(precio_str: str) -> float:\n    return float(precio_str) * 2 # Operación numérica real",
        "p7_pro_tip": "Define siempre funciones con anotaciones de tipo explícitas para prevenir fallos silenciosos en tiempo de ejecución.",
        "p8_summary": "Dominas los tipos primitivos esenciales de Python, la inmutabilidad en memoria Heap y la modularización en funciones con Type Hints.",
        "p8_achievement": "Capacidad para construir funciones robustas con casting seguro y cálculos matemáticos testeados.",
        "p8_instructor_notes": "En la siguiente clase exploraremos las compuertas lógicas y condicionales (if/elif/else): cómo dotar a la computadora de toma de decisiones.",
        "p9_challenge": "Implementa una función calcular_propina(total_cuenta: float, porcentaje: float) -> float y pruébala con pytest."
    },

    {
        "target_dir": f"{BASE_DIR}/01-fundamentos-python/clase-03-control-flujo-condicionales",
        "pdf_filename": "clase-03-control-flujo-condicionales.pdf",
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "course_num": "1 (Principiantes)",
        "class_title": "Clase 03: Control de Flujo - Condicionales",
        "class_code": "Clase 03",
        "level": "Principiante Absoluto",
        "metaphor": "El Guardia de la Puerta y el Menú de Opciones",
        "description": "Toma de decisiones lógicas en Python: operadores relacionales, operadores lógicos booleanos (and, or, not) y estructuras if, elif y else.",
        "diagram_type": "flow",
        "obj_conceptual": "Comprender la evaluación de expresiones booleanas y la exclusión mutua en cadenas if-elif-else.",
        "obj_practical": "Implementar sistemas de validación de reglas de negocio, control de acceso y árboles de decisión.",
        "p4_title": "Bifurcaciones Lógicas y Toma de Decisiones",
        "p4_intro": "Un programa no es una línea recta; es un camino con encrucijadas donde el flujo toma una dirección según las condiciones.",
        "p4_metaphor_desc": "Imagina un guardia en la entrada de un club: revisa tu entrada (if). Si tienes pase VIP entra gratis (if), si tienes entrada general paga boleto (elif), y si no tienes entrada se le deniega el acceso (else).",
        "p4_theory_1": "Operadores relacionales: == (igualdad), != (diferente), > (mayor), < (menor), >= (mayor o igual), <= (menor o igual).",
        "p4_theory_2": "Operadores lógicos: and (ambas condiciones deben ser True), or (al menos una True), not (invierte el valor de verdad).",
        "p4_golden_rule": "En una cadena if-elif-else, tan pronto como una condición resulta True, se ejecuta su bloque y se omiten todas las demás.",
        "p5_title": "Árbol de Decisión y Evaluación de Condiciones",
        "p5_desc": "Representación del flujo booleano con múltiples alternativas excluyentes.",
        "p5_step1_action": "Evalúa la primera condición del if principal.",
        "p5_step1_state": "Condición 1: ¿edad >= 18?",
        "p5_step2_action": "Si es True, entra al bloque if y salta al final de la estructura.",
        "p5_step2_state": "Ejecuta bloque prioritario",
        "p5_step3_action": "Si es False, evalúa secuencialmente los bloques elif.",
        "p5_step3_state": "Condición 2: ¿tiene_permiso?",
        "p5_step4_action": "Si ninguna condición previa fue True, se ejecuta el bloque else por defecto.",
        "p5_step4_state": "Rama fallback de seguridad",
        "p5_mental_tip": "Ordena tus condiciones de la más específica a la más general para evitar que un caso amplio oculte casos particulares.",
        "p6_title": "Sistema de Clasificación de Préstamos Bancarios",
        "p6_desc": "Ejemplo práctico con operadores lógicos combinados y evaluación de reglas financieras:",
        "p6_code": 'salario = <span class="bi">float</span>(<span class="bi">input</span>(<span class="st">"Salario mensual ($): "</span>))\npuntaje_credito = <span class="bi">int</span>(<span class="bi">input</span>(<span class="st">"Puntaje crediticio (300-850): "</span>))\ntiene_deudas = <span class="bi">input</span>(<span class="st">"¿Tiene deudas activas? (s/n): "</span>).<span class="fn">lower</span>() == <span class="st">"s"</span>\n\n<span class="kw">if</span> salario >= <span class="nu">3000.0</span> <span class="kw">and</span> puntaje_credito >= <span class="nu">720</span> <span class="kw">and</span> <span class="kw">not</span> tiene_deudas:\n    estado = <span class="st">"Aprobado Premium (Tasa de interés preferencial)"</span>\n<span class="kw">elif</span> salario >= <span class="nu">1800.0</span> <span class="kw">and</span> puntaje_credito >= <span class="nu">650</span>:\n    estado = <span class="st">"Aprobado Estándar (Sujeto a verificación)"</span>\n<span class="kw">elif</span> salario >= <span class="nu">1200.0</span> <span class="kw">or</span> puntaje_credito >= <span class="nu">600</span>:\n    estado = <span class="st">"Requiere Codeudor o Aval"</span>\n<span class="kw">else</span>:\n    estado = <span class="st">"Rechazado (No cumple los requisitos mínimos)"</span>\n\n<span class="bi">print</span>(<span class="st">f"\\nResultado de la solicitud: {estado}"</span>)',
        "p6_code_analysis": "El código implementa lógica booleana compuesta con and, not y or, garantizando una jerarquía de evaluación limpia.",
        "p7_title": "Errores Frecuentes con Condicionales",
        "p7_intro": "Trampas clásicas de sintaxis y lógica booleana en Python:",
        "p7_gotcha": "Confundir el operador de asignación (=) con el operador de comparación (==).",
        "p7_bad_code": "if rol = \"admin\": # SyntaxError\n    print(\"Acceso total\")",
        "p7_good_code": "if rol == \"admin\": # Comparación correcta\n    print(\"Acceso total\")",
        "p7_pro_tip": "Aprovecha la evaluación de cortocircuito (short-circuit evaluation) en Python para proteger llamadas riesgosas.",
        "p8_summary": "Has dominado el núcleo de la toma de decisiones en software mediante condicionales y lógica booleana.",
        "p8_achievement": "Capacidad para codificar flujos lógicos complejos y reglas de negocio robustas.",
        "p8_instructor_notes": "En la próxima clase abordaremos la repetición inteligente: bucles for y while para procesar volúmenes masivos de datos.",
        "p9_challenge": "Diseña un sistema de tarificación de boletos de cine con descuentos por edad, día de la semana y membresía VIP."
    },

    {
        "target_dir": f"{BASE_DIR}/01-fundamentos-python/clase-04-control-flujo-bucles",
        "pdf_filename": "clase-04-control-flujo-bucles.pdf",
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "course_num": "1 (Principiantes)",
        "class_title": "Clase 04: Control de Flujo - Bucles",
        "class_code": "Clase 04",
        "level": "Principiante Absoluto",
        "metaphor": "Las Vueltas a la Pista y el Termostato",
        "description": "Automatización iterativa en Python: bucles for sobre secuencias y range(), bucles condicionales while, y control con break, continue y else.",
        "diagram_type": "loop",
        "obj_conceptual": "Diferenciar con claridad cuándo emplear una iteración acotada (for) vs una iteración gobernada por estado (while).",
        "obj_practical": "Construir bucles eficientes con acumuladores, validaciones con reintentos y control de salida.",
        "p4_title": "La Repetición Inteligente y la Automatización",
        "p4_intro": "La mayor fortaleza de una computadora es su capacidad para ejecutar una misma tarea millones de veces sin cansarse ni cometer errores.",
        "p4_metaphor_desc": "El bucle for es como un atleta que da un número exacto de vueltas a la pista de carreras (5 vueltas definidas). El bucle while es como el termostato de un calentador: funciona continuamente mientras la temperatura esté por debajo de 22 grados, y se detiene automáticamente cuando se alcanza la meta.",
        "p4_theory_1": "Bucle for: Ideal cuando conoces de antemano el número de repeticiones o cuando recorres una colección finita.",
        "p4_theory_2": "Bucle while: Ideal cuando la repetición depende de una condición externa que puede cambiar dinámicamente durante la ejecución.",
        "p4_golden_rule": "Todo bucle while debe modificar en su cuerpo la variable de control; de lo contrario, se convierte en un bucle infinito que congela el programa.",
        "p5_title": "Ciclo de Vida de una Iteración",
        "p5_desc": "Estructura del flujo de control iterativo y mecanismos de interrupción anticipada.",
        "p5_step1_action": "Inicializa el índice o evalúa la condición de entrada del bucle.",
        "p5_step1_state": "Variable de control lista",
        "p5_step2_action": "Ejecuta las instrucciones del bloque interno.",
        "p5_step2_state": "Cálculo en la iteración actual",
        "p5_step3_action": "Si encuentra 'continue', salta directamente a la siguiente iteración.",
        "p5_step3_state": "Bypass de código restante",
        "p5_step4_action": "Si encuentra 'break', aborta el bucle inmediatamente hacia la siguiente línea externa.",
        "p5_step4_state": "Salida forzada del ciclo",
        "p5_mental_tip": "Visualiza el bucle como una rueda que gira; cada vuelta procesa un dato individual hasta que se agota el combustible de la condición.",
        "p6_title": "Sistema de Autenticación con Reintentos Limitados",
        "p6_desc": "Implementación que combina bucles while, banderas booleanas y control de intentos:",
        "p6_code": 'PASSWORD_SECRETA = <span class="st">"python2026"</span>\nintentos_maximos = <span class="nu">3</span>\nintentos_realizados = <span class="nu">0</span>\nacceso_concedido = <span class="kw">False</span>\n\n<span class="kw">while</span> intentos_realizados < intentos_maximos:\n    intento = <span class="bi">input</span>(<span class="st">f"Intento [{intentos_realizados + 1}/{intentos_maximos}] - Contraseña: "</span>)\n    <span class="kw">if</span> intento == PASSWORD_SECRETA:\n        acceso_concedido = <span class="kw">True</span>\n        <span class="bi">print</span>(<span class="st">"¡Acceso exitoso al sistema! 🔓"</span>)\n        <span class="kw">break</span>\n    <span class="kw">else</span>:\n        <span class="bi">print</span>(<span class="st">"❌ Contraseña incorrecta."</span>)\n        intentos_realizados += <span class="nu">1</span>\n\n<span class="kw">if</span> <span class="kw">not</span> acceso_concedido:\n    <span class="bi">print</span>(<span class="st">"🚫 Sistema bloqueado por demasiados intentos fallidos."</span>)',
        "p6_code_analysis": "Demuestra el uso de contadores incrementales, la instrucción break para salida inmediata y la bandera booleana de estado.",
        "p7_title": "Gotchas Clásicos en Bucles",
        "p7_intro": "Errores habituales que provocan fallos de rendimiento o bucles congelados:",
        "p7_gotcha": "Olvidar incrementar el contador en un bucle while, resultando en un bucle infinito que consume el 100% de la CPU.",
        "p7_bad_code": "i = 0\nwhile i < 5:\n    print(i) # Olvido de i += 1 -> Bucle infinito",
        "p7_good_code": "for i in range(5):\n    print(i) # Seguro, limpio e idiomático",
        "p7_pro_tip": "Prefiere siempre for sobre while cuando conozcas el número de iteraciones o trabajes sobre secuencias.",
        "p8_summary": "Comprendes los dos mecanismos de repetición de Python y sabes controlar su flujo con precisión milimétrica.",
        "p8_achievement": "Capacidad para procesar lotes de datos y crear flujos interactivos resilientes con reintentos.",
        "p8_instructor_notes": "En la próxima clase entraremos a las Estructuras de Datos: Listas y Colecciones para almacenar múltiples valores ordenados.",
        "p9_challenge": "Escribe un programa que utilice bucles anidados para generar la tabla de multiplicar completa del 1 al 10 con formato tabular."
    },

    {
        "target_dir": f"{BASE_DIR}/01-fundamentos-python/clase-05-listas-y-colecciones",
        "pdf_filename": "clase-05-listas-y-colecciones.pdf",
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "course_num": "1 (Principiantes)",
        "class_title": "Clase 05: Listas y Colecciones de Datos",
        "class_code": "Clase 05",
        "level": "Principiante Absoluto",
        "metaphor": "La Mochila del Programador y los Casilleros",
        "description": "Estructuras de datos secuenciales: listas mutables (list), indexación positiva y negativa, cortes (slicing), métodos esenciales y tuplas inmutables (tuple).",
        "diagram_type": "flow",
        "obj_conceptual": "Comprender la indexación basada en cero (0-indexed), la mutabilidad de listas y la inmutabilidad de tuplas.",
        "obj_practical": "Manipular colecciones mediante append(), insert(), pop(), slicing avanzado y comprensión de listas básica.",
        "p4_title": "La Mochila de Datos y las Secuencias Ordenadas",
        "p4_intro": "En el mundo real rara vez trabajamos con datos aislados; casi siempre gestionamos conjuntos de elementos como listas de clientes, precios o mediciones.",
        "p4_metaphor_desc": "Imagina una fila de casilleros escolares numerados desde el 0. En cada casillero puedes guardar lo que quieras. Las listas son casilleros que puedes abrir, cambiar y reordenar (mutables). Las tuplas son cajas de cristal selladas: puedes ver lo que hay dentro, pero nadie puede alterarlo (inmutables).",
        "p4_theory_1": "Indexación: El primer elemento está en el índice 0, y el último en el índice -1.",
        "p4_theory_2": "Slicing: La sintaxis lista[inicio:fin:paso] permite extraer subconjuntos sin modificar la lista original.",
        "p4_golden_rule": "Las listas son mutables (se modifican en el mismo lugar de memoria); las tuplas son inmutables y ofrecen mayor seguridad e integridad.",
        "p5_title": "Anatomía de la Indexación y Operaciones de Slicing",
        "p5_desc": "Mapeo de memoria para índices directos, inversos y sub-rangos de datos.",
        "p5_step1_action": "Python asigna un puntero de memoria ordenado a cada elemento.",
        "p5_step1_state": "['A', 'B', 'C', 'D']",
        "p5_step2_action": "Índices positivos: [0]=A, [1]=B, [2]=C, [3]=D.",
        "p5_step2_state": "Lectura hacia adelante",
        "p5_step3_action": "Índices negativos: [-1]=D, [-2]=C, [-3]=B, [-4]=A.",
        "p5_step3_state": "Lectura desde el final",
        "p5_step4_action": "Slicing [1:3] extrae los índices 1 y 2 (el límite superior es excluyente).",
        "p5_step4_state": "Nueva lista: ['B', 'C']",
        "p5_mental_tip": "Recuerda siempre la regla del límite superior: lista[0:3] extrae 3 elementos (índices 0, 1 y 2), el 3 queda fuera.",
        "p6_title": "Gestión de Carrito de Compras con Listas",
        "p6_desc": "Script que aplica operaciones CRUD sobre listas de Python con métodos nativos:",
        "p6_code": 'carrito: <span class="bi">list</span>[<span class="bi">str</span>] = [<span class="st">"Laptop"</span>, <span class="st">"Mouse"</span>, <span class="st">"Teclado"</span>]\n\n<span class="cm"># 1. Agregar elementos</span>\ncarrito.<span class="fn">append</span>(<span class="st">"Monitor 4K"</span>)\ncarrito.<span class="fn">insert</span>(<span class="nu">1</span>, <span class="st">"Auriculares"</span>)\n\n<span class="cm"># 2. Slicing (primeros 3 productos)</span>\nprioritarios = carrito[<span class="nu">0</span>:<span class="nu">3</span>]\n<span class="bi">print</span>(<span class="st">f"Productos prioritarios: {prioritarios}"</span>)\n\n<span class="cm"># 3. Eliminar y extraer</span>\neliminado = carrito.<span class="fn">pop</span>()\n<span class="bi">print</span>(<span class="st">f"Producto extraído: {eliminado}"</span>)\n\n<span class="cm"># 4. Iteración elegante con enumeración</span>\n<span class="kw">for</span> idx, prod <span class="kw">in</span> <span class="bi">enumerate</span>(carrito, start=<span class="nu">1</span>):\n    <span class="bi">print</span>(<span class="st">f"{idx}. {prod}"</span>)',
        "p6_code_analysis": "Uso de métodos nativos append, insert, pop, slicing y la función enumerate() para iteración limpia con índices.",
        "p7_title": "Gotchas Clásicos con Listas",
        "p7_intro": "Errores comunes al manipular listas y colecciones mutables:",
        "p7_gotcha": "Copiar una lista por asignación simple (lista2 = lista1) solo copia la referencia, no los datos.",
        "p7_bad_code": "a = [1, 2, 3]\nb = a\nb.append(4) # ¡Modifica también la lista 'a'!",
        "p7_good_code": "a = [1, 2, 3]\nb = a.copy() # Copia superficial independiente\nb.append(4)",
        "p7_pro_tip": "Usa lista[:] o lista.copy() cuando quieras duplicar una lista sin afectar la original.",
        "p8_summary": "Has dominado el uso de listas y tuplas, la indexación bidireccional y las operaciones fundamentales de colección.",
        "p8_achievement": "Capacidad para estructurar y transformar conjuntos secuenciales de información.",
        "p8_instructor_notes": "En la próxima clase conoceremos los Diccionarios: la estructura clave-valor que potencia la web moderna y los formatos JSON.",
        "p9_challenge": "Crea una función que reciba una lista de números y devuelva una tupla con (mínimo, máximo, promedio)."
    },

    {
        "target_dir": f"{BASE_DIR}/01-fundamentos-python/clase-06-diccionarios",
        "pdf_filename": "clase-06-diccionarios.pdf",
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "course_num": "1 (Principiantes)",
        "class_title": "Clase 06: Diccionarios y Mapeos Clave-Valor",
        "class_code": "Clase 06",
        "level": "Principiante Absoluto",
        "metaphor": "La Agenda Telefónica y el Expediente Médico",
        "description": "Estructuras asociativas de alto rendimiento: diccionarios (dict), asociación clave-valor, métodos (.get(), .keys(), .items()), anidamiento y similitud con JSON.",
        "diagram_type": "architecture",
        "obj_conceptual": "Comprender la indexación por clave semántica en lugar de posición numérica y la eficiencia O(1) de las tablas hash.",
        "obj_practical": "Construir modelos de datos complejos con diccionarios anidados y procesar registros estructurados.",
        "p4_title": "Mapeos Asociativos y la Estructura Clave-Valor",
        "p4_intro": "Buscar un dato por su posición (índice 4) es poco intuitivo; en el mundo real buscamos por nombre, correo o ID.",
        "p4_metaphor_desc": "Un diccionario es como tu agenda del teléfono: no buscas a tu mamá por el número de orden en que la agregaste, buscas la etiqueta 'Mamá' (la clave) y obtienes su número de teléfono (el valor).",
        "p4_theory_1": "Las claves en un diccionario deben ser únicas e inmutables (comúnmente strings o ints). Los valores pueden ser de cualquier tipo, incluidas listas u otros diccionarios.",
        "p4_theory_2": "La búsqueda en un diccionario es instantánea (tiempo constante O(1)) gracias al algoritmo interno de tabla hash.",
        "p4_golden_rule": "Nunca accedas a una clave con dict['clave'] si no estás 100% seguro de que existe; usa dict.get('clave', valor_por_defecto) para evitar KeyError.",
        "p5_title": "Arquitectura de un Diccionario y Búsqueda por Hash",
        "p5_desc": "Cómo Python mapea claves alfanuméricas a ubicaciones de memoria específicas.",
        "p5_step1_action": "Python aplica una función hash a la clave (ej: hash('email')).",
        "p5_step1_state": "Clave -> Hash ID numérico",
        "p5_step2_action": "Localiza el casillero exacto en la tabla hash de memoria.",
        "p5_step2_state": "Búsqueda O(1)",
        "p5_step3_action": "Recupera o modifica el valor asociado sin recorrer toda la estructura.",
        "p5_step3_state": "Lectura/Escritura inmediata",
        "p5_step4_action": "Permite serialización directa hacia y desde formato JSON para APIs web.",
        "p5_step4_state": "Compatibilidad universal",
        "p5_mental_tip": "Los diccionarios son el equivalente en Python a los objetos de JavaScript o los registros de bases de datos NoSQL.",
        "p6_title": "Sistema de Gestión de Inventario con Diccionarios",
        "p6_desc": "Manipulación de registros de productos con métodos .get(), .items() y anidamiento:",
        "p6_code": 'inventario = {\n    <span class="st">"PROD-001"</span>: {<span class="st">"nombre"</span>: <span class="st">"Teclado Mecánico"</span>, <span class="st">"precio"</span>: <span class="nu">85.0</span>, <span class="st">"stock"</span>: <span class="nu">12</span>},\n    <span class="st">"PROD-002"</span>: {<span class="st">"nombre"</span>: <span class="st">"Mouse Ergonómico"</span>, <span class="st">"precio"</span>: <span class="nu">45.0</span>, <span class="st">"stock"</span>: <span class="nu">0</span>}\n}\n\n<span class="cm"># Acceso seguro con .get()</span>\nsku_buscado = <span class="st">"PROD-001"</span>\nproducto = inventario.<span class="fn">get</span>(sku_buscado, <span class="kw">None</span>)\n\n<span class="kw">if</span> producto:\n    <span class="bi">print</span>(<span class="st">f"Producto: {producto[\'nombre\']} | Stock: {producto[\'stock\']} uds"</span>)\n\n<span class="cm"># Iteración completa de claves y valores</span>\n<span class="kw">for</span> sku, datos <span class="kw">in</span> inventario.<span class="fn">items</span>():\n    disponible = <span class="st">"En Stock"</span> <span class="kw">if</span> datos[<span class="st">"stock"</span>] > <span class="nu">0</span> <span class="kw">else</span> <span class="st">"Agotado"</span>\n    <span class="bi">print</span>(<span class="st">f"[{sku}] {datos[\'nombre\']} -> {disponible}"</span>)',
        "p6_code_analysis": "Se utiliza una estructura anidada dict-of-dicts, acceso resiliente con get() y desempaquetado de tuplas con el método .items().",
        "p7_title": "Gotchas Clásicos con Diccionarios",
        "p7_intro": "Errores habituales al consultar y mutar diccionarios:",
        "p7_gotcha": "Consultar una clave inexistente con corchetes (dict['inexistente']) provoca un KeyError que detiene el programa.",
        "p7_bad_code": "user = {'nombre': 'Leo'}\nprint(user['edad']) # KeyError: 'edad'",
        "p7_good_code": "user = {'nombre': 'Leo'}\nprint(user.get('edad', 0)) # Retorna 0 de forma segura",
        "p7_pro_tip": "Utiliza dictionary comprehensions ({k: v for k, v in ...}) para filtrar y transformar diccionarios en una sola línea.",
        "p8_summary": "Comprendes a fondo los diccionarios, la estructura clave-valor y el modelado de entidades del mundo real.",
        "p8_achievement": "Capacidad para manipular datos estructurados complejos, payloads JSON y configuraciones de software.",
        "p8_instructor_notes": "En la próxima clase estudiaremos las Funciones (def): el arte de empaquetar código reutilizable y modular.",
        "p9_challenge": "Crea una función que reciba una lista de palabras y devuelva un diccionario con la frecuencia de aparición de cada palabra."
    },

    {
        "target_dir": f"{BASE_DIR}/01-fundamentos-python/clase-07-funciones",
        "pdf_filename": "clase-07-funciones.pdf",
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "course_num": "1 (Principiantes)",
        "class_title": "Clase 07: Funciones Reutilizables y Modulares",
        "class_code": "Clase 07",
        "level": "Principiante Absoluto",
        "metaphor": "El Electrodoméstico y la Entrega del Cajero",
        "description": "Modularización y abstracción: definición con def, parámetros posicionales y nombrados, valores por defecto, valor de retorno (return), ámbito (scope) y type hints.",
        "diagram_type": "architecture",
        "obj_conceptual": "Comprender el principio DRY (Don't Repeat Yourself), la diferencia entre print y return, y el scope local de variables.",
        "obj_practical": "Escribir funciones modulares, documentadas con docstrings y fuertemente tipadas listas para producción.",
        "p4_title": "La Modularización y el Principio DRY",
        "p4_intro": "El código profesional no se escribe dos veces; cuando una lógica se necesita en múltiples lugares, se encapsula en una función.",
        "p4_metaphor_desc": "Una función es como un electrodoméstico: tiene una ranura de entrada (parámetros), un motor interno que realiza una tarea específica, y una bandeja de salida donde entrega el resultado terminado (return).",
        "p4_theory_1": "Parámetros vs Argumentos: Los parámetros son los nombres en la firma (def), los argumentos son los valores reales que pasas al invocarla.",
        "p4_theory_2": "Diferencia crucial: print() solo muestra texto en la pantalla pero devuelve None; return devuelve el valor a la variable que llamó a la función para seguir trabajando con él.",
        "p4_golden_rule": "Una función debe hacer una sola cosa y hacerla excepcionalmente bien (Principio de Responsabilidad Única).",
        "p5_title": "Caja Negra Funcional y Ámbito de Variables (Scope)",
        "p5_desc": "Flujo de invocación, paso de argumentos, aislamiento de variables locales y retorno de valor.",
        "p5_step1_action": "La función es llamada y se asignan los argumentos a los parámetros.",
        "p5_step1_state": "Creación del Call Stack Frame",
        "p5_step2_action": "Se ejecutan las instrucciones en un ámbito local aislado.",
        "p5_step2_state": "Variables locales temporales",
        "p5_step3_action": "La instrucción 'return' finaliza la ejecución de la función y emite el resultado.",
        "p5_step3_state": "Envío del valor de retorno",
        "p5_step4_action": "El stack frame se destruye y la memoria local se libera.",
        "p5_step4_state": "Retorno al flujo principal",
        "p5_mental_tip": "Las variables creadas dentro de una función mueren cuando la función termina: nunca intentes acceder a una variable local desde fuera.",
        "p6_title": "Módulo de Facturación con Funciones Tipadas",
        "p6_desc": "Diseño de funciones modulares con valores por defecto, docstrings y anotaciones de tipo:",
        "p6_code": '<span class="kw">def</span> <span class="fn">calcular_total_factura</span>(\n    subtotal: <span class="bi">float</span>,\n    tasa_impuesto: <span class="bi">float</span> = <span class="nu">0.21</span>,\n    descuento: <span class="bi">float</span> = <span class="nu">0.0</span>\n) -> <span class="bi">dict</span>[<span class="bi">str</span>, <span class="bi">float</span>]:\n    <span class="st">"""Calcula el desglose final de una factura comercial."""</span>\n    monto_descuento = subtotal * descuento\n    base_imponible = subtotal - monto_descuento\n    impuestos = base_imponible * tasa_impuesto\n    total_pagar = base_imponible + impuestos\n    \n    <span class="kw">return</span> {\n        <span class="st">"subtotal"</span>: subtotal,\n        <span class="st">"descuento_aplicado"</span>: monto_descuento,\n        <span class="st">"impuestos"</span>: impuestos,\n        <span class="st">"total"</span>: <span class="bi">round</span>(total_pagar, <span class="nu">2</span>)\n    }\n\n<span class="cm"># Uso con argumentos por nombre (keyword arguments)</span>\nfactura = <span class="fn">calcular_total_factura</span>(subtotal=<span class="nu">150.0</span>, descuento=<span class="nu">0.10</span>)\n<span class="bi">print</span>(<span class="st">f"Total a pagar: ${factura[\'total\']}"</span>)',
        "p6_code_analysis": "Función pura con parámetros opcionales con valores predeterminados, tipado formal y retorno estructurado en diccionario.",
        "p7_title": "Gotchas Clásicos con Funciones",
        "p7_intro": "Errores comunes de diseño y sintaxis en funciones de Python:",
        "p7_gotcha": "Usar argumentos mutables por defecto (como def func(lista=[])); la lista se comparte entre llamadas sucesivas.",
        "p7_bad_code": "def agregar(item, lista=[]): # ¡Peligro mutable!\n    lista.append(item)\n    return lista",
        "p7_good_code": "def agregar(item, lista=None):\n    if lista is None: lista = []\n    lista.append(item)\n    return lista",
        "p7_pro_tip": "Usa siempre None como valor predeterminado para parámetros que contengan estructuras mutables.",
        "p8_summary": "Dominas el pilar de la abstracción y la reutilización de código mediante funciones profesionales.",
        "p8_achievement": "Capacidad para escribir código limpio, modular, desacoplado y fácil de probar.",
        "p8_instructor_notes": "En la Clase 08 integraremos los 7 temas en un Proyecto Integrador completo: el Gestor de Tareas en Consola.",
        "p9_challenge": "Escribe una función recursiva que calcule el factorial de un número entero positivo con su caso base bien definido."
    },

    {
        "target_dir": f"{BASE_DIR}/01-fundamentos-python/clase-08-proyecto-integrador-basico",
        "pdf_filename": "clase-08-proyecto-integrador-basico.pdf",
        "course_name": "Curso 1: Fundamentos Básicos de Python",
        "course_num": "1 (Principiantes)",
        "class_title": "Clase 08: Integración Total & Proyecto Integrador",
        "class_code": "Clase 08",
        "level": "Principiante a Intermedio",
        "metaphor": "El Casco de Seguridad y Salir a Rodar en Bici",
        "description": "Consolidación de todo el Curso 1 en una aplicación completa: arquitectura CRUD (Create, Read, Update, Delete) para un gestor interactivo de tareas en consola.",
        "diagram_type": "architecture",
        "obj_conceptual": "Comprender cómo se interconectan todos los pilares del lenguaje para crear una aplicación funcional y resiliente.",
        "obj_practical": "Construir de principio a fin un sistema de gestión en terminal con menús interactivos, validaciones y persistencia conceptual.",
        "p4_title": "Arquitectura del Proyecto Integrador: Gestor de Tareas",
        "p4_intro": "Llegó el momento de unir todas las piezas: variables, condicionales, bucles, listas, diccionarios y funciones trabajando en armonía.",
        "p4_metaphor_desc": "Hasta ahora hemos practicado el equilibrio con las rueditas de entrenamiento. Hoy nos quitamos las rueditas, nos ponemos el casco de seguridad y salimos a rodar en la bicicleta por nosotros mismos en el mundo real.",
        "p4_theory_1": "Patrón de Menú Principal: Un bucle infinito while True mantiene viva la aplicación hasta que el usuario decida salir explícitamente.",
        "p4_theory_2": "Capa de Datos: Una lista de diccionarios en memoria actúa como la base de datos temporal de la aplicación.",
        "p4_golden_rule": "Separa la presentación (print, input) de la lógica de negocio (las funciones que agregan, buscan y transforman datos).",
        "p5_title": "Diagrama de Arquitectura de la Aplicación CLI",
        "p5_desc": "Interacción entre la capa de interfaz de consola, el enrutador de comandos y el modelo de datos.",
        "p5_step1_action": "Bucle principal muestra el menú de opciones (1. Agregar, 2. Listar, 3. Completar, 4. Salir).",
        "p5_step1_state": "Esperando opción del usuario",
        "p5_step2_action": "Enrutador if/elif invoca la función específica según la opción elegida.",
        "p5_step2_state": "Despacho a función modular",
        "p5_step3_action": "La función ejecuta la operación CRUD sobre la lista de tareas en memoria.",
        "p5_step3_state": "Actualización del estado",
        "p5_step4_action": "Se muestra retroalimentación visual al usuario y se reinicia el ciclo del menú.",
        "p5_step4_state": "Ciclo listo para nueva orden",
        "p5_mental_tip": "Esta arquitectura modular en consola es idéntica en concepto a los controladores y servicios de las APIs web modernas.",
        "p6_title": "Implementación del Task Manager CLI",
        "p6_desc": "Estructura modular del proyecto integrador con funciones CRUD completas:",
        "p6_code": 'tareas: <span class="bi">list</span>[<span class="bi">dict</span>] = []\n\n<span class="kw">def</span> <span class="fn">agregar_tarea</span>(titulo: <span class="bi">str</span>) -> <span class="kw">None</span>:\n    nueva_tarea = {<span class="st">"id"</span>: <span class="bi">len</span>(tareas) + <span class="nu">1</span>, <span class="st">"titulo"</span>: titulo, <span class="st">"completada"</span>: <span class="kw">False</span>}\n    tareas.<span class="fn">append</span>(nueva_tarea)\n    <span class="bi">print</span>(<span class="st">f"✅ Tarea #{nueva_tarea[\'id\']} agregada con éxito."</span>)\n\n<span class="kw">def</span> <span class="fn">listar_tareas</span>() -> <span class="kw">None</span>:\n    <span class="kw">if</span> <span class="kw">not</span> tareas:\n        <span class="bi">print</span>(<span class="st">"📭 No hay tareas registradas."</span>)\n        <span class="kw">return</span>\n    <span class="kw">for</span> t <span class="kw">in</span> tareas:\n        estado = <span class="st">"✔️ [LISTA]"</span> <span class="kw">if</span> t[<span class="st">"completada"</span>] <span class="kw">else</span> <span class="st">"⏳ [PENDIENTE]"</span>\n        <span class="bi">print</span>(<span class="st">f"#{t[\'id\']} - {t[\'titulo\']} {estado}"</span>)\n\n<span class="kw">def</span> <span class="fn">completar_tarea</span>(id_tarea: <span class="bi">int</span>) -> <span class="kw">None</span>:\n    <span class="kw">for</span> t <span class="kw">in</span> tareas:\n        <span class="kw">if</span> t[<span class="st">"id"</span>] == id_tarea:\n            t[<span class="st">"completada"</span>] = <span class="kw">True</span>\n            <span class="bi">print</span>(<span class="st">f"🎉 Tarea #{id_tarea} marcada como completada."</span>)\n            <span class="kw">return</span>\n    <span class="bi">print</span>(<span class="st">"❌ ID de tarea no encontrado."</span>)',
        "p6_code_analysis": "Sistema modular que implementa el ciclo CRUD completo, demostrando el dominio integral de las estructuras de datos y funciones.",
        "p7_title": "Buenas Prácticas para Proyectos Reales",
        "p7_intro": "Reglas de oro para dar el salto de principiante a desarrollador junior estructurado:",
        "p7_gotcha": "Escribir código espagueti con cientos de líneas sin funciones y mezclando variables globales descontroladas.",
        "p7_bad_code": "# Código monolítico sin funciones ni modularidad\nwhile True:\n    op = input()\n    # 300 líneas de if/else anidados sin separación",
        "p7_good_code": "# Código desacoplado\ndef main():\n    while True:\n        mostrar_menu()\n        procesar_opcion()",
        "p7_pro_tip": "Encapsula siempre el punto de entrada de tu programa dentro de if __name__ == '__main__': main().",
        "p8_summary": "¡Felicitaciones! Has completado con éxito el Curso 1 de Fundamentos de Python. Has pasado de cero a programador activo.",
        "p8_achievement": "Creación y comprensión integral de tu primera aplicación de software estructurada en Python.",
        "p8_instructor_notes": "En el Curso 2 daremos el salto a Algoritmos Avanzados, Notación Big-O, Pilas, Colas, Búsqueda Binaria y Optimización.",
        "p9_challenge": "Agrega la función para guardar y cargar las tareas en un archivo JSON en disco para tener persistencia real."
    },

    # -------------------------------------------------------------
    # CURSO 2: ALGORITMOS Y ESTRUCTURAS DE DATOS
    # -------------------------------------------------------------
    {
        "target_dir": f"{BASE_DIR}/02-algoritmos-estructuras/01-estructuras-datos-avanzadas",
        "pdf_filename": "01-estructuras-datos-avanzadas.pdf",
        "course_name": "Curso 2: Algoritmos Avanzados y Estructuras de Datos",
        "course_num": "2 (Intermedio)",
        "class_title": "Módulo 01: Estructuras de Datos Avanzadas",
        "class_code": "Módulo 01",
        "level": "Intermedio",
        "metaphor": "Pilas LIFO, Colas FIFO y Árboles Jerárquicos",
        "description": "Estructuración de datos de alto rendimiento: Pilas (Stack - LIFO), Colas (Queue / deque - FIFO), Conjuntos (sets) y árboles binarios de búsqueda (BST).",
        "diagram_type": "architecture",
        "obj_conceptual": "Comprender las disciplinas de acceso LIFO y FIFO y el coste temporal O(1) vs O(n) en memoria.",
        "obj_practical": "Implementar pilas para validación sintáctica, colas para buffers de tareas y árboles binarios para búsqueda rápida.",
        "p4_title": "Estructuras Lineales y Jerárquicas en Memoria",
        "p4_intro": "Las listas básicas no siempre son la estructura óptima cuando la velocidad de inserción y extracción en los extremos es crítica.",
        "p4_metaphor_desc": "Una Pila (Stack) es como una pila de platos: el último que colocas arriba es el primero que lavas (LIFO: Last In, First Out). Una Cola (Queue) es como la fila del supermercado: el primero que llega es el primero en ser atendido (FIFO: First In, First Out).",
        "p4_theory_1": "collections.deque en Python permite inserciones y extracciones O(1) tanto por la izquierda como por la derecha, a diferencia de list.pop(0) que cuesta O(n).",
        "p4_theory_2": "Los conjuntos (sets) implementan álgebra de conjuntos (unión, intersección, diferencia) con consultas O(1) y garantizan elementos únicos.",
        "p4_golden_rule": "Para colas FIFO de alto rendimiento en Python, utiliza siempre collections.deque en lugar de listas estándar.",
        "p5_title": "Comparativa Visual: Pila (LIFO) vs Cola (FIFO)",
        "p5_desc": "Mecanismos de inserción (push/enqueue) y extracción (pop/dequeue) en memoria:",
        "p5_step1_action": "Operación Push / Enqueue: Ingreso de nuevo elemento.",
        "p5_step1_state": "Elemento en memoria",
        "p5_step2_action": "En Stack (LIFO): Se coloca en el tope y se extrae del tope.",
        "p5_step2_state": "Último en entrar = Primero en salir",
        "p5_step3_action": "En Queue (FIFO): Se ingresa por la cola y se extrae por la cabeza.",
        "p5_step3_state": "Primero en entrar = Primero en salir",
        "p5_step4_action": "Árboles: Ramifican decisiones jerárquicas izquierda/derecha.",
        "p5_step4_state": "Acceso logarítmico O(log n)",
        "p5_mental_tip": "Las pilas gestionan llamadas de funciones y el botón Deshacer (Ctrl+Z); las colas gestionan mensajes y colas de impresión.",
        "p6_title": "Validador de Paréntesis Balanceados con Pilas",
        "p6_desc": "Algoritmo clásico de entrevistas técnicas implementado con una Pila LIFO:",
        "p6_code": '<span class="kw">def</span> <span class="fn">validar_parentesis</span>(expresion: <span class="bi">str</span>) -> <span class="bi">bool</span>:\n    pila: <span class="bi">list</span>[<span class="bi">str</span>] = []\n    pares = {<span class="st">")"</span>: <span class="st">"("</span>, <span class="st">"}"</span>: <span class="st">"{"</span>, <span class="st">"]"</span>: <span class="st">"["</span>}\n    \n    <span class="kw">for</span> char <span class="kw">in</span> expresion:\n        <span class="kw">if</span> char <span class="kw">in</span> pares.<span class="fn">values</span>():\n            pila.<span class="fn">append</span>(char) <span class="cm"># Push</span>\n        <span class="kw">elif</span> char <span class="kw">in</span> pares:\n            <span class="kw">if</span> <span class="kw">not</span> pila <span class="kw">or</span> pila.<span class="fn">pop</span>() != pares[char]: <span class="cm"># Pop & Check</span>\n                <span class="kw">return</span> <span class="kw">False</span>\n                \n    <span class="kw">return</span> <span class="bi">len</span>(pila) == <span class="nu">0</span>\n\n<span class="cm"># Pruebas</span>\n<span class="bi">print</span>(<span class="fn">validar_parentesis</span>(<span class="st">"{[()()]}"</span>))  <span class="cm"># True</span>\n<span class="bi">print</span>(<span class="fn">validar_parentesis</span>(<span class="st">"{[(])}"</span>))    <span class="cm"># False</span>',
        "p6_code_analysis": "El algoritmo apila los caracteres de apertura y los desapila al encontrar cierres, garantizando correspondencia simétrica en O(n).",
        "p7_title": "Gotchas y Optimización de Estructuras",
        "p7_intro": "Errores de rendimiento habituales al elegir estructuras de datos:",
        "p7_gotcha": "Usar list.pop(0) para implementar una cola; obliga a desplazar todos los elementos restantes en memoria generando complejidad O(n).",
        "p7_bad_code": "cola = []\ncola.insert(0, item) # O(n) en cada inserción",
        "p7_good_code": "from collections import deque\ncola = deque()\ncola.append(item) # O(1) instantáneo",
        "p7_pro_tip": "Usa sets para eliminar duplicados de una lista en una sola operación: unicos = list(set(datos)).",
        "p8_summary": "Dominas las estructuras de datos fundamentales para diseñar software de alta concurrencia y algoritmos eficientes.",
        "p8_achievement": "Capacidad para elegir la estructura de datos óptima según los requerimientos de tiempo y espacio.",
        "p8_instructor_notes": "En el siguiente módulo aprenderemos Búsqueda Binaria, Algoritmos de Ordenamiento y Notación Big-O.",
        "p9_challenge": "Implementa una cola de prioridad utilizando el módulo heapq de Python para despachar tareas según su urgencia."
    },

    {
        "target_dir": f"{BASE_DIR}/02-algoritmos-estructuras/02-algoritmos-ordenamiento-busqueda",
        "pdf_filename": "02-algoritmos-ordenamiento-busqueda.pdf",
        "course_name": "Curso 2: Algoritmos Avanzados y Estructuras de Datos",
        "course_num": "2 (Intermedio)",
        "class_title": "Módulo 02: Ordenamiento, Búsqueda y Big-O",
        "class_code": "Módulo 02",
        "level": "Intermedio",
        "metaphor": "El Diccionario por la Mitad y Divide y Vencerás",
        "description": "Análisis de complejidad y eficiencia computacional: Notación Big-O, Búsqueda Lineal O(n) vs Búsqueda Binaria O(log n), y algoritmos de ordenamiento (MergeSort, QuickSort).",
        "diagram_type": "flow",
        "obj_conceptual": "Comprender cómo escala el tiempo de ejecución a medida que el tamaño de entrada (n) crece hacia el infinito.",
        "obj_practical": "Implementar búsqueda binaria y entender la estrategia 'Divide y Vencerás' de QuickSort frente a BubbleSort.",
        "p4_title": "Notación Asintótica Big-O y Complejidad",
        "p4_intro": "En software la velocidad no se mide en segundos, sino en cómo crece el número de operaciones en función del volumen de datos (n).",
        "p4_metaphor_desc": "Si buscas una palabra en un diccionario de 1,000 páginas hojeando página por página (búsqueda lineal), puedes tardar 1,000 pasos. Si abres el diccionario por la mitad exacta y descartas la mitad irrelevante (búsqueda binaria), encontrarás la palabra en solo 10 pasos.",
        "p4_theory_1": "Escalas de Complejidad: O(1) Constante < O(log n) Logarítmica < O(n) Lineal < O(n log n) Casi-lineal < O(n^2) Cuadrática.",
        "p4_theory_2": "Búsqueda Binaria requiere que la colección esté previamente ordenada para garantizar reducción del espacio de búsqueda a la mitad.",
        "p4_golden_rule": "Evita los bucles anidados innecesarios: dos bucles anidados sobre n elementos convierten un algoritmo de O(n) a O(n^2).",
        "p5_title": "Diagrama de Búsqueda Binaria (Divide & Conquer)",
        "p5_desc": "Estrategia de reducción logarítmica del intervalo de búsqueda con punteros low, mid y high.",
        "p5_step1_action": "Calcula el punto medio: mid = (low + high) // 2.",
        "p5_step1_state": "low=0, high=n-1, mid",
        "p5_step2_action": "Compara el elemento en 'mid' con el objetivo buscado.",
        "p5_step2_state": "Evalúa igualdad",
        "p5_step3_action": "Si objetivo < array[mid], descarta la mitad derecha ajustando high = mid - 1.",
        "p5_step3_state": "Espacio reducido al 50%",
        "p5_step4_action": "Si objetivo > array[mid], descarta la mitad izquierda ajustando low = mid + 1.",
        "p5_step4_state": "Repite hasta converger",
        "p5_mental_tip": "La búsqueda binaria puede encontrar un registro entre 4 mil millones de elementos en tan solo 32 comparaciones.",
        "p6_title": "Búsqueda Binaria y QuickSort en Python",
        "p6_desc": "Implementación idiomática de búsqueda binaria y particionado recursivo QuickSort:",
        "p6_code": '<span class="kw">def</span> <span class="fn">busqueda_binaria</span>(lista: <span class="bi">list</span>[<span class="bi">int</span>], objetivo: <span class="bi">int</span>) -> <span class="bi">int</span>:\n    low, high = <span class="nu">0</span>, <span class="bi">len</span>(lista) - <span class="nu">1</span>\n    <span class="kw">while</span> low <= high:\n        mid = (low + high) // <span class="nu">2</span>\n        <span class="kw">if</span> lista[mid] == objetivo:\n            <span class="kw">return</span> mid <span class="cm"># Encontrado</span>\n        <span class="kw">elif</span> lista[mid] < objetivo:\n            low = mid + <span class="nu">1</span>\n        <span class="kw">else</span>:\n            high = mid - <span class="nu">1</span>\n    <span class="kw">return</span> -<span class="nu">1</span> <span class="cm"># No existe</span>\n\n<span class="kw">def</span> <span class="fn">quicksort</span>(arr: <span class="bi">list</span>[<span class="bi">int</span>]) -> <span class="bi">list</span>[<span class="bi">int</span>]:\n    <span class="kw">if</span> <span class="bi">len</span>(arr) <= <span class="nu">1</span>:\n        <span class="kw">return</span> arr\n    pivote = arr[<span class="bi">len</span>(arr) // <span class="nu">2</span>]\n    izq = [x <span class="kw">for</span> x <span class="kw">in</span> arr <span class="kw">if</span> x < pivote]\n    centro = [x <span class="kw">for</span> x <span class="kw">in</span> arr <span class="kw">if</span> x == pivote]\n    der = [x <span class="kw">for</span> x <span class="kw">in</span> arr <span class="kw">if</span> x > pivote]\n    <span class="kw">return</span> <span class="fn">quicksort</span>(izq) + centro + <span class="fn">quicksort</span>(der)',
        "p6_code_analysis": "Búsqueda Binaria O(log n) combinada con QuickSort O(n log n) basado en listas por comprensión.",
        "p7_title": "Gotchas en Algoritmos de Búsqueda",
        "p7_intro": "Errores clásicos al implementar algoritmos de búsqueda y ordenamiento:",
        "p7_gotcha": "Ejecutar búsqueda binaria sobre una lista no ordenada; produce falsos negativos y resultados erráticos.",
        "p7_bad_code": "desordenada = [9, 1, 5, 2]\nbusqueda_binaria(desordenada, 5) # ¡Falla!",
        "p7_good_code": "ordenada = sorted(desordenada)\nbusqueda_binaria(ordenada, 5) # Retorna índice correcto",
        "p7_pro_tip": "Python utiliza Timsort (híbrido de MergeSort e InsertionSort) en lista.sort(), el cual tiene complejidad garantizada O(n log n).",
        "p8_summary": "Comprendes el impacto exponencial de los algoritmos en el rendimiento y dominas las técnicas de ordenamiento y búsqueda.",
        "p8_achievement": "Capacidad para analizar la complejidad temporal de algoritmos y optimizar cuellos de botella.",
        "p8_instructor_notes": "En el siguiente módulo exploraremos la Recursividad y la Programación Dinámica con Memoización.",
        "p9_challenge": "Compara el tiempo de ejecución en segundos entre una búsqueda lineal y una binaria sobre 1 millón de elementos con el módulo time."
    },

    {
        "target_dir": f"{BASE_DIR}/02-algoritmos-estructuras/03-recursividad-optimizacion",
        "pdf_filename": "03-recursividad-optimizacion.pdf",
        "course_name": "Curso 2: Algoritmos Avanzados y Estructuras de Datos",
        "course_num": "2 (Intermedio)",
        "class_title": "Módulo 03: Recursividad y Programación Dinámica",
        "class_code": "Módulo 03",
        "level": "Intermedio",
        "metaphor": "Las Muñecas Rusas (Matrioshkas) y la Libreta de Apuntes",
        "description": "Optimización algorítmica avanzada: Caso base y recursión, desbordamiento del Call Stack, Programación Dinámica, Memoización con @functools.lru_cache y Tabulación.",
        "diagram_type": "architecture",
        "obj_conceptual": "Comprender la descomposición recursiva y cómo la memoización transforma complejidades exponenciales O(2^n) en lineales O(n).",
        "obj_practical": "Implementar algoritmos recursivos seguros y optimizar cálculos pesados con decoradores nativos de Python.",
        "p4_title": "Pensamiento Recursivo y Subproblemas Superpuestos",
        "p4_intro": "La recursividad ocurre cuando una función se invoca a sí misma para resolver una versión más pequeña del mismo problema.",
        "p4_metaphor_desc": "La recursión es como abrir una muñeca rusa (Matrioshka): abres una y hay otra idéntica más pequeña dentro, hasta llegar a la más diminuta que no se puede abrir (el Caso Base). La memoización es como tener una libreta de apuntes: cuando resuelves un cálculo difícil, anotas el resultado para no tener que volver a calcularlo jamás.",
        "p4_theory_1": "Todo algoritmo recursivo DEBE tener al menos un Caso Base para detener las llamadas antes de saturar el Call Stack (RecursionError).",
        "p4_theory_2": "Programación Dinámica (DP): Técnica para resolver problemas complejos descomponiéndolos en subproblemas y guardando sus soluciones.",
        "p4_golden_rule": "Sin memoización, Fibonacci recursivo tiene complejidad O(2^n); con memoización se reduce a O(n).",
        "p5_title": "Árbol de Llamadas Recursivas vs Tabla de Memoización",
        "p5_desc": "Eliminación de ramas redundantes en el árbol de ejecución mediante caché en memoria.",
        "p5_step1_action": "Llamada inicial a la función con el parámetro n.",
        "p5_step1_state": "f(5) en Call Stack",
        "p5_step2_action": "Bifurcación recursiva en f(n-1) y f(n-2).",
        "p5_step2_state": "Subárbol de cálculos",
        "p5_step3_action": "Verificación en caché: si el resultado ya existe, lo devuelve inmediatamente sin recalcular.",
        "p5_step3_state": "Hit en caché O(1)",
        "p5_step4_action": "Si no existe, computa el caso base y almacena el resultado antes de retornar.",
        "p5_step4_state": "Guardado en memoria",
        "p5_mental_tip": "La memoización es intercambiar memoria (RAM) por tiempo de CPU: un compromiso altamente beneficioso en sistemas modernos.",
        "p6_title": "Fibonacci Optimizado con Memoización",
        "p6_desc": "Comparativa entre recursión ingenua y optimización con el decorador lru_cache de la librería estándar:",
        "p6_code": '<span class="kw">from</span> functools <span class="kw">import</span> lru_cache\n<span class="kw">import</span> time\n\n<span class="cm"># Versión Optimizada con Programación Dinámica</span>\n@lru_cache(maxsize=<span class="kw">None</span>)\n<span class="kw">def</span> <span class="fn">fibonacci_memo</span>(n: <span class="bi">int</span>) -> <span class="bi">int</span>:\n    <span class="kw">if</span> n <= <span class="nu">0</span>: <span class="kw">return</span> <span class="nu">0</span>\n    <span class="kw">if</span> n == <span class="nu">1</span>: <span class="kw">return</span> <span class="nu">1</span>\n    <span class="kw">return</span> <span class="fn">fibonacci_memo</span>(n - <span class="nu">1</span>) + <span class="fn">fibonacci_memo</span>(n - <span class="nu">2</span>)\n\n<span class="cm"># Cálculo instantáneo para n=100</span>\ninicio = time.<span class="fn">perf_counter</span>()\nresultado = <span class="fn">fibonacci_memo</span>(<span class="nu">100</span>)\nfin = time.<span class="fn">perf_counter</span>()\n\n<span class="bi">print</span>(<span class="st">f"Fibonacci(100) = {resultado}"</span>)\n<span class="bi">print</span>(<span class="st">f"Tiempo de cálculo: {(fin - inicio)*1000:.4f} ms"</span>)',
        "p6_code_analysis": "El decorador @lru_cache intercepta las llamadas y almacena los resultados en una tabla hash en memoria, logrando tiempo de ejecución instantáneo.",
        "p7_title": "Gotchas en Recursividad",
        "p7_intro": "Errores críticos que pueden derribar servicios productivos:",
        "p7_gotcha": "Olvidar el caso base o no avanzar hacia él en cada iteración, provocando un RecursionError por desbordamiento de pila.",
        "p7_bad_code": "def loop(n):\n    return loop(n) # RecursionError: maximum recursion depth exceeded",
        "p7_good_code": "def loop(n):\n    if n <= 0: return 0 # Caso base\n    return n + loop(n - 1)",
        "p7_pro_tip": "Python tiene un límite de recursión por defecto de 1000 llamadas (sys.getrecursionlimit()).",
        "p8_summary": "Has dominado las técnicas de optimización más avanzadas de la ciencia de la computación aplicadas a Python.",
        "p8_achievement": "Capacidad para transformar problemas intratables en algoritmos de alto rendimiento con programación dinámica.",
        "p8_instructor_notes": "En el Curso 3 entraremos de lleno a la Inteligencia Artificial: LLMs, Prompt Engineering, RAG y Agentes Autónomos.",
        "p9_challenge": "Resuelve el clásico problema del cambio de monedas (Coin Change Problem) usando programación dinámica con tabulación."
    },

    # -------------------------------------------------------------
    # CURSO 3: DESARROLLO DE AGENTES DE IA
    # -------------------------------------------------------------
    {
        "target_dir": f"{BASE_DIR}/03-agentes-ia/01-fundamentos-ia-llm",
        "pdf_filename": "01-fundamentos-ia-llm.pdf",
        "course_name": "Curso 3: Creación y Desarrollo de Agentes de IA",
        "course_num": "3 (Avanzado)",
        "class_title": "Módulo 01: Fundamentos de IA Generativa y LLMs",
        "class_code": "Módulo 01",
        "level": "Avanzado",
        "metaphor": "El Cerebro Probabilístico y el Molde de Salida",
        "description": "Integración de Modelos de Lenguaje Grande (LLMs): arquitectura Transformer, APIs modernas (Gemini, OpenAI, Ollama), Prompt Engineering avanzado y salidas estructuradas JSON con Pydantic.",
        "diagram_type": "architecture",
        "obj_conceptual": "Comprender la naturaleza probabilística de los LLMs, el cálculo de tokens, la ventana de contexto y el control determinista de temperatura.",
        "obj_practical": "Construir clientes robustos de IA en Python con validación estricta de esquemas de respuesta tipados.",
        "p4_title": "Arquitectura de Modelos de Lenguaje Grande (LLMs)",
        "p4_intro": "Los LLMs no 'piensan' como los humanos; son gigantescas redes neuronales que predicen la siguiente palabra más probable dado un contexto.",
        "p4_metaphor_desc": "Un LLM es como un erudito que ha leído toda la biblioteca de Alejandría: si le haces una pregunta abierta responderá con fluidez literaria, pero si le colocas un molde rígido (un esquema JSON con Pydantic), vertirá su conocimiento exclusivamente dentro de la forma exacta que necesitas.",
        "p4_theory_1": "Tokens y Contexto: Los textos se tokenizan en fragmentos sub-palabra; la ventana de contexto limita cuántos tokens puede procesar simultáneamente.",
        "p4_theory_2": "Parámetros Clave: Temperatura (0.0 para respuestas deterministas y código; 0.7+ para creatividad), Top-P y penalización de repetición.",
        "p4_golden_rule": "En entornos de producción nunca uses texto libre del LLM; fuerza siempre salidas tipadas estructuradas validadas con Pydantic.",
        "p5_title": "Pipeline de Inferencia y Validación Estructurada",
        "p5_desc": "Flujo desde la construcción del System Prompt hasta la validación del objeto de salida.",
        "p5_step1_action": "Construcción del System Prompt con instrucciones de rol y Few-Shot examples.",
        "p5_step1_state": "Tokenización del prompt",
        "p5_step2_action": "Envío a la API del modelo (Gemini / OpenAI / Ollama) con schema JSON.",
        "p5_step2_state": "Inferencia en la GPU",
        "p5_step3_action": "El modelo genera un payload JSON estricto cumpliendo la especificación.",
        "p5_step3_state": "Payload JSON crudo",
        "p5_step4_action": "Pydantic parsea y valida los tipos de datos en un objeto Python listo.",
        "p5_step4_state": "Instancia BaseModel validada",
        "p5_mental_tip": "Trata al LLM como un microservicio no determinista: coloca siempre una capa de validación antes de entregar los datos a tu backend.",
        "p6_title": "Extractor de Entidades con Pydantic y LLM",
        "p6_desc": "Esquema tipado para forzar respuestas deterministas en Python:",
        "p6_code": '<span class="kw">from</span> pydantic <span class="kw">import</span> BaseModel, Field\n<span class="kw">from</span> typing <span class="kw">import</span> List\n\n<span class="cm"># Esquema de validación estricta</span>\n<span class="kw">class</span> <span class="fn">AnalisisSentimiento</span>(BaseModel):\n    sentimiento: <span class="bi">str</span> = Field(description=<span class="st">"POSITIVO, NEGATIVO o NEUTRO"</span>)\n    puntuacion_confianza: <span class="bi">float</span> = Field(ge=<span class="nu">0.0</span>, le=<span class="nu">1.0</span>)\n    temas_clave: List[<span class="bi">str</span>] = Field(default_factory=<span class="bi">list</span>)\n    resumen_ejecutivo: <span class="bi">str</span>\n\n<span class="cm"># Simulación de respuesta parseada por el motor</span>\npayload_llm = \'\'\'{\n    "sentimiento": "POSITIVO",\n    "puntuacion_confianza": 0.96,\n    "temas_clave": ["soporte rápido", "calidad software", "precio justo"],\n    "resumen_ejecutivo": "El cliente expresa gran satisfacción con la atención recibida."\n}\'\'\'\n\nanalisis = AnalisisSentimiento.<span class="fn">model_validate_json</span>(payload_llm)\n<span class="bi">print</span>(<span class="st">f"Sentimiento: {analisis.sentimiento} ({analisis.puntuacion_confianza*100:.1f}%)"</span>)\n<span class="bi">print</span>(<span class="st">f"Temas: {\', \'.join(analisis.temas_clave)}"</span>)',
        "p6_code_analysis": "Uso de Pydantic V2 para validación robusta con límites de rango numérico (ge, le) y serialización JSON directa.",
        "p7_title": "Gotchas en Integración con LLMs",
        "p7_intro": "Errores frecuentes al conectar modelos de IA generativa a sistemas de software:",
        "p7_gotcha": "Confiar ciegamente en que el LLM siempre responderá JSON válido sin capturar excepciones de parseo o alucinaciones.",
        "p7_bad_code": "data = json.loads(llm_response) # Fallará si el LLM incluye texto extra",
        "p7_good_code": "try:\n    data = Model.model_validate_json(llm_response)\nexcept ValidationError as e:\n    # Estrategia de reintento / corrección",
        "p7_pro_tip": "Utiliza Temperature=0.0 para extracción de datos, clasificación y generación de código reproducible.",
        "p8_summary": "Comprendes los fundamentos de la IA generativa y sabes conectar modelos LLM con validación de esquemas tipados.",
        "p8_achievement": "Capacidad para construir tuberías de datos asistidas por IA que no fallen en producción.",
        "p8_instructor_notes": "En el siguiente módulo aprenderemos Tool Calling (Function Calling), Memoria y RAG con bases de datos vectoriales.",
        "p9_challenge": "Crea un script que consulte la API de Gemini u Ollama para resumir un artículo largo forzando salida en JSON con Pydantic."
    },

    {
        "target_dir": f"{BASE_DIR}/03-agentes-ia/02-herramientas-y-memoria",
        "pdf_filename": "02-herramientas-y-memoria.pdf",
        "course_name": "Curso 3: Creación y Desarrollo de Agentes de IA",
        "course_num": "3 (Avanzado)",
        "class_title": "Módulo 02: Herramientas, Memoria y RAG",
        "class_code": "Módulo 02",
        "level": "Avanzado",
        "metaphor": "La Caja de Herramientas y el Bibliotecario con Memoria",
        "description": "Dotando de superpoderes a los LLMs: Invocación de funciones (Tool Use / Function Calling), memoria a corto/largo plazo y RAG (Retrieval-Augmented Generation) con embeddings y bases de datos vectoriales.",
        "diagram_type": "architecture",
        "obj_conceptual": "Comprender cómo un modelo utiliza herramientas externas para ejecutar código y cómo RAG elimina alucinaciones inyectando contexto verificado.",
        "obj_practical": "Implementar un pipeline RAG con búsqueda por similitud de coseno y definir herramientas Python ejecutables por el modelo.",
        "p4_title": "Capacidades Aumentadas: Tool Calling y RAG",
        "p4_intro": "Un LLM aislado solo puede generar texto; cuando le otorgas herramientas y memoria, se transforma en un agente inteligente capaz de interactuar con el mundo.",
        "p4_metaphor_desc": "El LLM es como un consultor brillante pero encerrado en una habitación: Tool Calling es darle un teléfono para llamar a APIs o consultar bases de datos. RAG es ponerle al lado a un bibliotecario que busca en segundos los documentos exactos de tu empresa y se los pasa antes de que responda.",
        "p4_theory_1": "Tool Calling: El LLM decide qué función invocar y genera los argumentos exactos; tu código ejecuta la función y devuelve el resultado al LLM.",
        "p4_theory_2": "Embeddings Vectoriales: Representaciones numéricas de significado semántico; textos con significados similares tienen alta similitud de coseno en el espacio vectorial.",
        "p4_golden_rule": "RAG resuelve el problema del conocimiento desactualizado y las alucinaciones sin necesidad de reentrenar el modelo fundacional.",
        "p5_title": "Arquitectura de un Sistema RAG (Retrieval-Augmented Generation)",
        "p5_desc": "Flujo de ingestión, búsqueda semántica y generación contextualizada con documentos privados.",
        "p5_step1_action": "Los documentos se dividen en fragmentos (chunks) y se vectorizan con un modelo de embeddings.",
        "p5_step1_state": "Vectores en Vector DB",
        "p5_step2_action": "El usuario hace una pregunta; se vectoriza la consulta del usuario.",
        "p5_step2_state": "Query vector",
        "p5_step3_action": "Se realiza búsqueda de similitud (k-Nearest Neighbors / Cosine Similarity) para extraer los chunks más relevantes.",
        "p5_step3_state": "Contexto recuperado",
        "p5_step4_action": "Se ensambla el prompt enriquecido [Contexto + Pregunta] y el LLM formula la respuesta final respaldada en hechos.",
        "p5_step4_state": "Respuesta precisa y sin alucinación",
        "p5_mental_tip": "RAG es el examen a libro abierto del LLM: en lugar de memorizar todo, le das el párrafo exacto donde está la respuesta.",
        "p6_title": "Definición y Ejecución de Herramientas (Tool Calling)",
        "p6_desc": "Registro dinámico de funciones Python para ser ejecutadas autónomamente por el modelo:",
        "p6_code": '<span class="kw">import</span> json\n\n<span class="cm"># 1. Definición de la Herramienta en Python puro</span>\n<span class="kw">def</span> <span class="fn">consultar_clima</span>(ciudad: <span class="bi">str</span>) -> <span class="bi">str</span>:\n    <span class="st">"""Consulta la temperatura actual de una ciudad."""</span>\n    datos = {<span class="st">"Madrid"</span>: <span class="st">"24°C Despejado"</span>, <span class="st">"Bogotá"</span>: <span class="st">"18°C Lluvioso"</span>}\n    <span class="kw">return</span> datos.<span class="fn">get</span>(ciudad, <span class="st">"20°C Clima templado"</span>)\n\n<span class="cm"># 2. Registro de herramientas disponibles para el agente</span>\nHERRAMIENTAS_DISPONIBLES = {<span class="st">"consultar_clima"</span>: consultar_clima}\n\n<span class="cm"># 3. Simulación de orden de Tool Call emitida por el LLM</span>\nllamada_modelo = {\n    <span class="st">"funcion"</span>: <span class="st">"consultar_clima"</span>,\n    <span class="st">"argumentos"</span>: {<span class="st">"ciudad"</span>: <span class="st">"Madrid"</span>}\n}\n\n<span class="cm"># 4. Despachador de ejecución segura</span>\nnombre_fn = llamada_modelo[<span class="st">"funcion"</span>]\nargs = llamada_modelo[<span class="st">"argumentos"</span>]\nresultado_tool = HERRAMIENTAS_DISPONIBLES[nombre_fn](**args)\n\n<span class="bi">print</span>(<span class="st">f"Resultado de la herramienta para el LLM: {resultado_tool}"</span>)',
        "p6_code_analysis": "Mecanismo de despacho dinámico mediante desempaquetado de argumentos (**kwargs) para conectar funciones locales con el LLM.",
        "p7_title": "Gotchas en Tool Calling y RAG",
        "p7_intro": "Errores clásicos al implementar memorias y herramientas:",
        "p7_gotcha": "Fragmentar documentos en chunks demasiado grandes (que diluyen la relevancia semántica) o demasiado pequeños (que pierden contexto).",
        "p7_bad_code": "# Chunks de 5000 tokens: el embedding pierde especificidad semántica",
        "p7_good_code": "# Chunks de 300-500 tokens con 50 tokens de solapamiento (overlap)",
        "p7_pro_tip": "Incluye siempre docstrings claros y detallados en tus funciones Python; los LLMs leen esos docstrings para saber cuándo invocar la herramienta.",
        "p8_summary": "Dominas los dos pilares que transforman un modelo de lenguaje en un sistema interactivo: Tool Calling y RAG.",
        "p8_achievement": "Capacidad para conectar modelos de IA con APIs externas, bases de datos vectoriales y fuentes documentales.",
        "p8_instructor_notes": "En el siguiente módulo integraremos estos componentes en Agentes Autónomos con el ciclo de razonamiento ReAct.",
        "p9_challenge": "Crea una herramienta que consulte una base de datos SQLite y permita a un LLM responder preguntas sobre inventarios."
    },

    {
        "target_dir": f"{BASE_DIR}/03-agentes-ia/03-construccion-de-agentes",
        "pdf_filename": "03-construccion-de-agentes.pdf",
        "course_name": "Curso 3: Creación y Desarrollo de Agentes de IA",
        "course_num": "3 (Avanzado)",
        "class_title": "Módulo 03: Construcción de Agentes Autónomos",
        "class_code": "Módulo 03",
        "level": "Avanzado",
        "metaphor": "El Ciclo Cognitivo ReAct y el Enjambre de Agentes",
        "description": "Arquitecturas de agentes inteligentes: Ciclo cognitivo ReAct (Reasoning + Acting), planificación multi-paso, memoria episódica, auto-reflexión y sistemas multi-agente orquestados.",
        "diagram_type": "architecture",
        "obj_conceptual": "Comprender la diferencia entre un script lineal y un bucle de razonamiento autónomo donde el agente decide su próximo paso.",
        "obj_practical": "Construir un motor de agente ReAct en Python puro y orquestar flujos de trabajo multi-agente complejos.",
        "p4_title": "El Paradigma ReAct: Razonar y Actuar en Ciclos",
        "p4_intro": "Un agente autónomo no ejecuta un camino fijo; observa su entorno, razona sobre el objetivo, decide qué herramienta usar y evalúa los resultados de forma iterativa.",
        "p4_metaphor_desc": "El ciclo ReAct es como un detective privado resolviendo un misterio: tiene un Pensamiento (Thought: 'Necesito ver la cámara de seguridad'), realiza una Acción (Action: busca el video con una herramienta), analiza la Observación (Observation: 'El sospechoso salió a las 10:00'), y repite el ciclo hasta llegar a la Respuesta Final.",
        "p4_theory_1": "Ciclo Cognitivo: Thought (Razonamiento interno) -> Action (Invocación de herramienta) -> Observation (Lectura del entorno) -> Evaluación.",
        "p4_theory_2": "Sistemas Multi-Agente: División de trabajo entre agentes especializados (Investigador, Programador, Auditor de Calidad) orquestados por un Supervisor.",
        "p4_golden_rule": "Todo bucle de agente autónomo debe tener un límite estricto de pasos máximos (max_iterations) para evitar bucles infinitos y consumo desmedido de tokens.",
        "p5_title": "Grafo Cíclico de Razonamiento ReAct",
        "p5_desc": "Flujo de control dinámico donde el agente decide autónomamente continuar investigando o emitir la solución final.",
        "p5_step1_action": "Recibe la misión del usuario y formula el primer pensamiento estratégico.",
        "p5_step1_state": "Thought 1 formulado",
        "p5_step2_action": "Emite una orden de acción hacia una herramienta específica.",
        "p5_step2_state": "Action: Tool invocation",
        "p5_step3_action": "Recibe la observación del entorno con los datos reales generados.",
        "p5_step3_state": "Observation incorporada al prompt",
        "p5_step4_action": "¿Objetivo cumplido? Si no, repite ciclo; si sí, genera Final Answer.",
        "p5_step4_state": "Solución entregada",
        "p5_mental_tip": "El agente mantiene un historial acumulativo de pensamientos y observaciones pasadas para no repetir errores.",
        "p6_title": "Motor de Agente ReAct en Python Puro",
        "p6_desc": "Implementación minimalista y autónoma del ciclo de razonamiento y acción:",
        "p6_code": '<span class="kw">class</span> <span class="fn">AgenteReAct</span>:\n    <span class="kw">def</span> <span class="fn">__init__</span>(self, herramientas: <span class="bi">dict</span>, max_pasos: <span class="bi">int</span> = <span class="nu">5</span>):\n        self.herramientas = herramientas\n        self.max_pasos = max_pasos\n        self.memoria: <span class="bi">list</span>[<span class="bi">str</span>] = []\n\n    <span class="kw">def</span> <span class="fn">ejecutar_mision</span>(self, objetivo: <span class="bi">str</span>) -> <span class="bi">str</span>:\n        self.memoria.<span class="fn">append</span>(<span class="st">f"Objetivo: {objetivo}"</span>)\n        <span class="kw">for</span> paso <span class="kw">in</span> <span class="bi">range</span>(<span class="nu">1</span>, self.max_pasos + <span class="nu">1</span>):\n            <span class="bi">print</span>(<span class="st">f"\\n--- [Paso {paso}] Ciclo Cognitivo ---"</span>)\n            <span class="cm"># 1. Simulación de pensamiento y decisión del LLM</span>\n            pensamiento = <span class="st">"Consultar base de datos para extraer métricas"</span>\n            accion_tool = <span class="st">"consultar_db"</span>\n            \n            <span class="bi">print</span>(<span class="st">f"💭 Thought: {pensamiento}"</span>)\n            <span class="bi">print</span>(<span class="st">f"⚡ Action: {accion_tool}()"</span>)\n            \n            <span class="cm"># 2. Ejecución de la herramienta y observación</span>\n            observacion = <span class="st">"Ventas del mes: $45,000 USD (Crecimiento +12%)"</span>\n            <span class="bi">print</span>(<span class="st">f"👁️ Observation: {observacion}"</span>)\n            \n            <span class="cm"># 3. Condición de término</span>\n            <span class="kw">return</span> <span class="st">f"Respuesta Final: Las ventas crecieron un 12% alcanzando $45,000 USD."</span>\n        <span class="kw">return</span> <span class="st">"Límite de pasos alcanzado."</span>',
        "p6_code_analysis": "Clase controladora que orquesta el bucle de ejecución de agentes, acumula contexto en memoria episódica y previene bloqueos.",
        "p7_title": "Gotchas en Desarrollo de Agentes",
        "p7_intro": "Riesgos arquitectónicos en sistemas multi-agente autónomos:",
        "p7_gotcha": "Permitir que un agente ejecute comandos en el sistema operativo o mutaciones destructivas en bases de datos sin una capa de confirmación humana (Human-in-the-loop).",
        "p7_bad_code": "# Agente ejecutando rm -rf o DROP TABLE sin validación",
        "p7_good_code": "# Validar permisos y requerir confirmación antes de acciones críticas",
        "p7_pro_tip": "Implementa timeouts y presupuestos de tokens por sesión para evitar costos imprevistos en APIs comerciales.",
        "p8_summary": "¡Has completado el Curso 3! Dominas el diseño, la memoria y la orquestación de Agentes de Inteligencia Artificial.",
        "p8_achievement": "Capacidad para construir agentes autónomos que resuelven problemas complejos combinando herramientas y razonamiento.",
        "p8_instructor_notes": "En el Curso 4 aplicarás todo lo aprendido en tu Proyecto Final: Aplicaciones Web, Chatbots de Producción o Sistemas de Gestión.",
        "p9_challenge": "Construye un sistema de dos agentes donde el primer agente genere un reporte y el segundo actúe como auditor crítico."
    },

    # -------------------------------------------------------------
    # CURSO 4: PROYECTO FINAL PERSONALIZADO
    # -------------------------------------------------------------
    {
        "target_dir": f"{BASE_DIR}/04-proyecto-final/plantillas/01-aplicacion-web",
        "pdf_filename": "01-aplicacion-web.pdf",
        "course_name": "Curso 4: Taller Práctico & Proyecto Final Personalizado",
        "course_num": "4 (Integrador)",
        "class_title": "Track 01: Aplicaciones Web con Python (FastAPI & Streamlit)",
        "class_code": "Track 01",
        "level": "Integrador / Producción",
        "metaphor": "El Restaurante: La Carta (Frontend) y la Cocina de Alta Eficiencia (Backend)",
        "description": "Arquitectura de aplicaciones web full-stack en Python: Backend asíncrono de alto rendimiento con FastAPI, documentación Swagger automática y Frontend interactivo con Streamlit.",
        "diagram_type": "architecture",
        "obj_conceptual": "Comprender la separación de responsabilidades Cliente-Servidor, APIs RESTful y el paradigma asíncrono async/await.",
        "obj_practical": "Construir y desplegar una aplicación web completa con endpoints RESTful, validación con Pydantic y dashboard interactivo.",
        "p4_title": "Arquitectura Cliente-Servidor y APIs Modernas",
        "p4_intro": "Una aplicación web desacoplada divide la presentación visual del procesamiento central de datos mediante contratos de comunicación HTTP (APIs REST).",
        "p4_metaphor_desc": "El frontend (Streamlit) es la carta elegante y el mozo que atiende al comensal en la mesa. El backend (FastAPI) es la cocina profesional donde los chefs procesan las comandas con máxima higiene, rapidez y orden, entregando los platos listos en formato JSON.",
        "p4_theory_1": "FastAPI: Framework moderno, basado en Starlette y Pydantic, con soporte nativo de asincronía (ASGI) y tipado estático.",
        "p4_theory_2": "Verbos HTTP Semánticos: GET (consultar datos), POST (crear nuevos registros), PUT (actualizar), DELETE (eliminar).",
        "p4_golden_rule": "Nunca mezcles lógica pesada de base de datos en el cliente visual; el cliente solo consume y renderiza.",
        "p5_title": "Diagrama de Flujo Full-Stack: Streamlit <-> FastAPI <-> DB",
        "p5_desc": "Comunicación asíncrona mediante peticiones HTTP/JSON y validación cruzada.",
        "p5_step1_action": "El usuario interactúa con widgets en Streamlit y presiona un botón.",
        "p5_step1_state": "Evento en UI",
        "p5_step2_action": "Streamlit envía una petición HTTP POST /api/v1/recurso con payload JSON.",
        "p5_step2_state": "Request sobre HTTP",
        "p5_step3_action": "FastAPI valida los datos con Pydantic, ejecuta la lógica y persiste en DB.",
        "p5_step3_state": "Validación & Persistencia",
        "p5_step4_action": "FastAPI responde HTTP 201 Created y Streamlit actualiza la vista reactivamente.",
        "p5_step4_state": "UI actualizada",
        "p5_mental_tip": "FastAPI genera automáticamente documentación Swagger interactiva en la ruta /docs para probar todos tus endpoints.",
        "p6_title": "Backend FastAPI con Endpoint RESTful Tipado",
        "p6_desc": "Servicio web profesional con validación de modelos y control de estado HTTP:",
        "p6_code": '<span class="kw">from</span> fastapi <span class="kw">import</span> FastAPI, HTTPException, status\n<span class="kw">from</span> pydantic <span class="kw">import</span> BaseModel\n\napp = FastAPI(title=<span class="st">"API de Gestión de Productos"</span>, version=<span class="st">"1.0.0"</span>)\n\n<span class="kw">class</span> <span class="fn">ProductoDTO</span>(BaseModel):\n    nombre: <span class="bi">str</span>\n    precio: <span class="bi">float</span>\n    categoria: <span class="bi">str</span>\n\ndb_productos: <span class="bi">list</span>[<span class="bi">dict</span>] = []\n\n@app.post(<span class="st">"/productos"</span>, status_code=status.HTTP_201_CREATED)\n<span class="kw">async def</span> <span class="fn">crear_producto</span>(prod: ProductoDTO):\n    nuevo = {<span class="st">"id"</span>: <span class="bi">len</span>(db_productos) + <span class="nu">1</span>, **prod.model_dump()}\n    db_productos.<span class="fn">append</span>(nuevo)\n    <span class="kw">return</span> {<span class="st">"mensaje"</span>: <span class="st">"Producto creado"</span>, <span class="st">"data"</span>: nuevo}\n\n@app.get(<span class="st">"/productos"</span>)\n<span class="kw">async def</span> <span class="fn">listar_productos</span>():\n    <span class="kw">return</span> {<span class="st">"total"</span>: <span class="bi">len</span>(db_productos), <span class="st">"productos"</span>: db_productos}',
        "p6_code_analysis": "Endpoints asíncronos decorados con FastAPI, validación automática mediante Pydantic DTO y códigos de estado HTTP semánticos.",
        "p7_title": "Gotchas y Seguridad en Aplicaciones Web",
        "p7_intro": "Vulnerabilidades y errores de arquitectura en APIs de producción:",
        "p7_gotcha": "Olvidar configurar el middleware CORS (Cross-Origin Resource Sharing), bloqueando las peticiones del frontend.",
        "p7_bad_code": "# Sin configuración CORS: Streamlit o React no podrán consumir la API",
        "p7_good_code": "from fastapi.middleware.cors import CORSMiddleware\napp.add_middleware(CORSMiddleware, allow_origins=['*'])",
        "p7_pro_tip": "Utiliza uvicorn main:app --reload durante desarrollo y despliega con contenedores Docker en producción.",
        "p8_summary": "Dominas el desarrollo de aplicaciones web full-stack profesionales en Python con FastAPI y Streamlit.",
        "p8_achievement": "Capacidad para diseñar y desplegar APIs REST escalables con interfaces interactivas para tu portafolio.",
        "p8_instructor_notes": "Acompañamiento personalizado disponible para la arquitectura y el despliegue de tu proyecto final.",
        "p9_challenge": "Integra autenticación JWT (JSON Web Tokens) en tu API de FastAPI para proteger endpoints sensibles."
    },

    {
        "target_dir": f"{BASE_DIR}/04-proyecto-final/plantillas/02-chatbot-inteligente",
        "pdf_filename": "02-chatbot-inteligente.pdf",
        "course_name": "Curso 4: Taller Práctico & Proyecto Final Personalizado",
        "course_num": "4 (Integrador)",
        "class_title": "Track 02: Chatbot Inteligente para Atención al Cliente",
        "class_code": "Track 02",
        "level": "Integrador / Producción",
        "metaphor": "El Recepcionista Omnicanal y el Manual de Operaciones",
        "description": "Arquitectura de chatbots conversacionales de producción: Integración de LLMs, memoria de sesión multi-usuario, guardrails de seguridad y conexión multicanal (Telegram, WhatsApp, Web).",
        "diagram_type": "architecture",
        "obj_conceptual": "Comprender la gestión del estado conversacional, el enrutamiento de intenciones y la prevención de alucinaciones corporativas.",
        "obj_practical": "Construir un bot conversacional con historial de diálogo, base de conocimiento RAG y despliegue en Telegram o Web.",
        "p4_title": "Arquitectura de un Chatbot Conversacional de Negocio",
        "p4_intro": "Un chatbot empresarial no solo charla: responde preguntas frecuentes con precisión quirúrgica, consulta el estado de pedidos y transfiere a humanos cuando es necesario.",
        "p4_metaphor_desc": "El chatbot es como el recepcionista estrella de una empresa: saluda cordialmente, recuerda todo lo que le dijiste en la conversación actual (memoria de sesión) y consulta de inmediato el manual de operaciones antes de dar una respuesta oficial.",
        "p4_theory_1": "Gestión de Sesión: Cada usuario tiene un session_id único asociado a su buffer de historial en memoria (o en Redis).",
        "p4_theory_2": "Guardrails y System Prompt: Delimitan estrictamente las fronteras temáticas del bot para evitar que hable de temas ajenos a la empresa.",
        "p4_golden_rule": "Instruye siempre al chatbot en su System Prompt para que admita honestamente si no conoce una respuesta en lugar de inventar información.",
        "p5_title": "Diagrama de Flujo Conversacional y Webhooks",
        "p5_desc": "Ciclo de vida del mensaje desde la app de mensajería hasta la síntesis de respuesta.",
        "p5_step1_action": "El usuario envía un mensaje en Telegram/WhatsApp; la plataforma emite un Webhook HTTP.",
        "p5_step1_state": "Mensaje entrante",
        "p5_step2_action": "El Session Manager recupera el historial previo del usuario desde la memoria caché.",
        "p5_step2_state": "Historial de diálogo cargado",
        "p5_step3_action": "Se inyecta el contexto RAG de la empresa y el LLM formula la respuesta corporativa.",
        "p5_step3_state": "Inferencia contextualizada",
        "p5_step4_action": "Se guarda el nuevo turno en el historial y se envía el mensaje al canal del usuario.",
        "p5_step4_state": "Respuesta entregada al chat",
        "p5_mental_tip": "Mantén los prompts del sistema concisos y enfócate en el tono de voz (amable, formal, conciso).",
        "p6_title": "Motor de Chatbot con Historial de Sesión",
        "p6_desc": "Gestor de memoria de diálogo multi-usuario en Python:",
        "p6_code": '<span class="kw">class</span> <span class="fn">ChatbotAtencionCliente</span>:\n    <span class="kw">def</span> <span class="fn">__init__</span>(self, nombre_empresa: <span class="bi">str</span>):\n        self.nombre_empresa = nombre_empresa\n        self.sesiones: <span class="bi">dict</span>[<span class="bi">str</span>, <span class="bi">list</span>] = {}\n        self.system_prompt = <span class="st">f"Eres el asistente virtual de {nombre_empresa}. Sé conciso y formal."</span>\n\n    <span class="kw">def</span> <span class="fn">responder_usuario</span>(self, user_id: <span class="bi">str</span>, mensaje: <span class="bi">str</span>) -> <span class="bi">str</span>:\n        <span class="kw">if</span> user_id <span class="kw">not in</span> self.sesiones:\n            self.sesiones[user_id] = [{<span class="st">"role"</span>: <span class="st">"system"</span>, <span class="st">"content"</span>: self.system_prompt}]\n        \n        <span class="cm"># Agregar turno del usuario</span>\n        self.sesiones[user_id].<span class="fn">append</span>({<span class="st">"role"</span>: <span class="st">"user"</span>, <span class="st">"content"</span>: mensaje})\n        \n        <span class="cm"># Simulación de respuesta del LLM contextualizada</span>\n        respuesta = <span class="st">f"Hola, gracias por contactar a {self.nombre_empresa}. ¿En qué puedo ayudarte?"</span>\n        self.sesiones[user_id].<span class="fn">append</span>({<span class="st">"role"</span>: <span class="st">"assistant"</span>, <span class="st">"content"</span>: respuesta})\n        \n        <span class="kw">return</span> respuesta',
        "p6_code_analysis": "Clase que gestiona sesiones independientes por usuario, acumulando el historial en el formato canónico de roles de los LLMs.",
        "p7_title": "Gotchas en Chatbots de Producción",
        "p7_intro": "Errores comunes en sistemas conversacionales:",
        "p7_gotcha": "No limitar el tamaño del historial acumulado; con el tiempo la conversación agota la ventana de contexto y eleva los costes innecesariamente.",
        "p7_bad_code": "# Acumular cientos de mensajes sin podar el historial",
        "p7_good_code": "# Mantener solo los últimos K mensajes (Sliding Window Memory)",
        "p7_pro_tip": "Usa una ventana deslizante (ej: últimos 10 mensajes) o resume periódicamente los turnos anteriores.",
        "p8_summary": "Dominas la arquitectura completa de un agente conversacional inteligente para atención a clientes.",
        "p8_achievement": "Capacidad para construir y desplegar chatbots empresariales con memoria y contexto corporativo.",
        "p8_instructor_notes": "Presenta este proyecto en tu portafolio como demostración de integración práctica de IA en procesos de negocio.",
        "p9_challenge": "Integra la biblioteca python-telegram-bot para publicar tu chatbot en vivo en un canal de Telegram."
    },

    {
        "target_dir": f"{BASE_DIR}/04-proyecto-final/plantillas/03-sistema-gestion-bd",
        "pdf_filename": "03-sistema-gestion-bd.pdf",
        "course_name": "Curso 4: Taller Práctico & Proyecto Final Personalizado",
        "course_num": "4 (Integrador)",
        "class_title": "Track 03: Sistema de Gestión con Base de Datos Relacional",
        "class_code": "Track 03",
        "level": "Integrador / Producción",
        "metaphor": "El Archivo Notarial y la Bóveda de Datos ACID",
        "description": "Modelado de datos y persistencia robusta en Python: Conexión con SQLite y PostgreSQL, operaciones CRUD seguras con parámetros SQL, prevención de inyecciones y transacciones ACID.",
        "diagram_type": "architecture",
        "obj_conceptual": "Comprender el modelo relacional de datos, las claves primarias/foráneas y la integridad transaccional ACID.",
        "obj_practical": "Construir un sistema de persistencia completo con repositorios en Python puro interactuando con SQLite / PostgreSQL.",
        "p4_title": "Persistencia de Datos e Integridad Transaccional (ACID)",
        "p4_intro": "La memoria RAM se borra al apagar la computadora; una base de datos relacional garantiza que la información de tus clientes y finanzas persista para siempre de forma atómica e íntegra.",
        "p4_metaphor_desc": "Una base de datos relacional es como una bóveda notarial de alta seguridad: cada tabla es un libro de registros con columnas estrictas, y cada transacción es un contrato firmado. O se realizan todos los pasos de la operación o se cancela por completo sin dejar inconsistencias a medias.",
        "p4_theory_1": "Propiedades ACID: Atomicidad (todo o nada), Consistencia (cumple reglas), Aislamiento (concurrencia segura), Durabilidad (persiste en disco).",
        "p4_theory_2": "Inyección SQL: La vulnerabilidad #1 en bases de datos; ocurre al concatenar texto crudo en queries. Se previene siempre con consultas parametrizadas (?) o (%s).",
        "p4_golden_rule": "NUNCA uses f-strings para construir sentencias SQL (ej: f'SELECT * FROM u WHERE id={id}'); usa siempre queries parametrizadas con tuplas.",
        "p5_title": "Diagrama de Capas: Aplicación <-> Repositorio <-> Motor SQL",
        "p5_desc": "Arquitectura en capas (Layered Architecture) para aislar las sentencias SQL de la lógica de negocio.",
        "p5_step1_action": "La capa de negocio solicita guardar o consultar una entidad.",
        "p5_step1_state": "Llamada a método del Repositorio",
        "p5_step2_action": "El Repositorio abre una conexión/cursor y prepara la sentencia parametrizada.",
        "p5_step2_state": "Preparación de la query",
        "p5_step3_action": "El motor de base de datos ejecuta la transacción y valida claves únicas.",
        "p5_step3_state": "Ejecución ACID en disco",
        "p5_step4_action": "Se realiza commit() para asegurar los cambios y se cierra la conexión de forma segura.",
        "p5_step4_state": "Datos persistidos permanentemente",
        "p5_mental_tip": "Utiliza siempre context managers (with sqlite3.connect(...) as conn:) para asegurar el cierre de conexiones.",
        "p6_title": "Repositorio de Datos Seguro con SQLite",
        "p6_desc": "Implementación de persistencia relacional con transacciones y consultas parametrizadas:",
        "p6_code": '<span class="kw">import</span> sqlite3\n\n<span class="kw">class</span> <span class="fn">RepositorioUsuarios</span>:\n    <span class="kw">def</span> <span class="fn">__init__</span>(self, db_path: <span class="bi">str</span> = <span class="st">"app.db"</span>):\n        self.db_path = db_path\n        self._crear_tabla()\n\n    <span class="kw">def</span> <span class="fn">_crear_tabla</span>(self) -> <span class="kw">None</span>:\n        <span class="kw">with</span> sqlite3.<span class="fn">connect</span>(self.db_path) <span class="kw">as</span> conn:\n            cursor = conn.<span class="fn">cursor</span>()\n            cursor.<span class="fn">execute</span>(\'\'\'\n                CREATE TABLE IF NOT EXISTS usuarios (\n                    id INTEGER PRIMARY KEY AUTOINCREMENT,\n                    nombre TEXT NOT NULL,\n                    email TEXT UNIQUE NOT NULL,\n                    saldo REAL DEFAULT 0.0\n                )\n            \'\'\')\n            conn.<span class="fn">commit</span>()\n\n    <span class="kw">def</span> <span class="fn">insertar_usuario</span>(self, nombre: <span class="bi">str</span>, email: <span class="bi">str</span>, saldo: <span class="bi">float</span>) -> <span class="bi">int</span>:\n        <span class="kw">with</span> sqlite3.<span class="fn">connect</span>(self.db_path) <span class="kw">as</span> conn:\n            cursor = conn.<span class="fn">cursor</span>()\n            <span class="cm"># Consulta parametrizada segura contra Inyección SQL</span>\n            cursor.<span class="fn">execute</span>(\n                <span class="st">"INSERT INTO usuarios (nombre, email, saldo) VALUES (?, ?, ?)"</span>,\n                (nombre, email, saldo)\n            )\n            conn.<span class="fn">commit</span>()\n            <span class="kw">return</span> cursor.lastrowid',
        "p6_code_analysis": "Clase Repository que encapsula la lógica SQL, maneja el ciclo de vida de conexiones y previene vulnerabilidades de inyección SQL.",
        "p7_title": "Gotchas en Gestión de Bases de Datos",
        "p7_intro": "Errores críticos que provocan pérdida de datos o brechas de seguridad:",
        "p7_gotcha": "Concatenar variables de usuario directamente dentro de sentencias SQL, permitiendo ataques de Inyección SQL.",
        "p7_bad_code": "cursor.execute(f\"SELECT * FROM users WHERE user = '{user}'\") # ¡Vulnerable!",
        "p7_good_code": "cursor.execute(\"SELECT * FROM users WHERE user = ?\", (user,)) # Inmune a inyección",
        "p7_pro_tip": "Crea siempre índices (CREATE INDEX) sobre las columnas que uses frecuentemente en cláusulas WHERE o JOIN.",
        "p8_summary": "¡Felicitaciones! Has dominado el diseño y persistencia de bases de datos relacionales en Python.",
        "p8_achievement": "Capacidad para construir sistemas de información profesionales con integridad de datos garantizada.",
        "p8_instructor_notes": "Presenta este sistema con su esquema relacional como parte de tu proyecto final integrador.",
        "p9_challenge": "Implementa una transacción bancaria que transfiera saldo entre dos usuarios asegurando atomicidad con rollback en caso de error."
    }
]

def build_pdf_for_class(meta: Dict[str, Any]) -> bool:
    """Genera el PDF para una clase usando una carpeta temporal y luego lo mueve."""
    
    target_dir = meta["target_dir"]
    pdf_filename = meta["pdf_filename"]
    final_pdf_path = os.path.join(target_dir, pdf_filename)
    
    # 1. Asegurar que existe el directorio de destino
    os.makedirs(target_dir, exist_ok=True)
    
    # 2. Crear carpeta temporal
    temp_dir = tempfile.mkdtemp(prefix="build_pdf_temp_")
    print(f"🔨 [Iniciando] {meta['class_title']}")
    print(f"   📁 Directorio temporal: {temp_dir}")
    
    try:
        # 3. Generar HTML con estilo LaTeX
        html_content = build_class_html(meta)
        html_file = os.path.join(temp_dir, "document.html")
        temp_pdf_file = os.path.join(temp_dir, pdf_filename)
        
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        # 4. Compilar a PDF con Chrome Headless
        cmd = [
            "google-chrome",
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            f"--print-to-pdf={temp_pdf_file}",
            html_file
        ]
        
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"❌ Error compilando PDF en Chrome: {res.stderr}")
            return False
            
        # 5. Verificar con pdfinfo
        info_res = subprocess.run(["pdfinfo", temp_pdf_file], capture_output=True, text=True)
        pages_line = [l for l in info_res.stdout.split("\n") if l.startswith("Pages:")]
        pages_count = pages_line[0] if pages_line else "Pages: Desconocido"
        
        file_size = os.path.getsize(temp_pdf_file)
        print(f"   📄 Generado con éxito ({pages_count}, {file_size} bytes)")
        
        # 6. Copiar PDF a la carpeta de clase
        shutil.copy2(temp_pdf_file, final_pdf_path)
        print(f"   ✅ Movido a destino: {final_pdf_path}")
        
        return True
        
    except Exception as e:
        print(f"❌ Excepción durante la generación: {e}")
        return False
        
    finally:
        # 7. Borrar la carpeta temporal
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print(f"   🧹 Carpeta temporal eliminada: {temp_dir}\n")

def main():
    print("=" * 70)
    print("🚀 INICIANDO GENERACIÓN DE PDFs PARA TODAS LAS CLASES Y CURSOS")
    print(f"👤 Autor: {AUTHOR_INFO['name']} ({AUTHOR_INFO['title']})")
    print(f"📦 Total de clases/módulos a generar: {len(CLASSES_METADATA)}")
    print("=" * 70 + "\n")
    
    success_count = 0
    for meta in CLASSES_METADATA:
        ok = build_pdf_for_class(meta)
        if ok:
            success_count += 1
            
    print("=" * 70)
    print(f"✨ PROCESO COMPLETADO: {success_count}/{len(CLASSES_METADATA)} PDFs generados exitosamente.")
    print("=" * 70)

if __name__ == "__main__":
    main()
