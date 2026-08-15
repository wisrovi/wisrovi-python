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

class CertificateGenerator:
    """Generador de diplomas PDF certificados."""

    @classmethod
    def generate_html(
        cls,
        student_name: str,
        course_title: str = "Programa Integral de Formación en Python: De Cero a Agentes de IA",
        hours: int = 160
    ) -> str:
        """Renderiza el documento HTML del certificado."""
        issue_date = datetime.now().strftime("%d de %B de %Y")
        
        # Generar hash de verificación único
        hash_seed = f"{student_name}-{course_title}-{issue_date}-wisrovi-academy-2026"
        cert_hash = hashlib.sha256(hash_seed.encode("utf-8")).hexdigest()[:24].upper()
        
        html = (
            CERTIFICATE_TEMPLATE_HTML
            .replace("{student_name}", student_name.strip())
            .replace("{course_title}", course_title)
            .replace("{hours}", str(hours))
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
        """Compila el certificado en PDF usando Google Chrome Headless en un directorio temporal."""
        html_content = cls.generate_html(student_name, course_title, hours)
        
        temp_dir = tempfile.mkdtemp()
        temp_html = os.path.join(temp_dir, "certificate.html")
        
        try:
            with open(temp_html, "w", encoding="utf-8") as f:
                f.write(html_content)
                
            os.makedirs(os.path.dirname(os.path.abspath(output_pdf_path)), exist_ok=True)
            
            cmd = [
                "google-chrome",
                "--headless",
                "--disable-gpu",
                "--no-sandbox",
                f"--print-to-pdf={output_pdf_path}",
                temp_html
            ]
            
            subprocess.run(cmd, check=True)
            return output_pdf_path
        finally:
            if os.path.exists(temp_html):
                try:
                    os.remove(temp_html)
                    os.rmdir(temp_dir)
                except Exception:
                    pass
