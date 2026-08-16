#!/usr/bin/env python3
"""
Embedded UI Frontend (Wisrovi Academy - Virtual AI Tutor & RPG v2.0).
Incluye sistema de bloqueos secuenciales estrictos (4 pasos obligatorios por clase),
efectos de sonido sintetizados (Web Audio API), narración socrática (Web Speech API),
visualizador interactivo de Heap/Stack y diseño Neo-Cyber Glassmorphism de clase mundial.
"""

def get_embedded_html() -> str:
    return """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wisrovi Academy - Virtual AI Tutor & RPG de Programación</title>
  
  <!-- Google Fonts: Inter, Outfit & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Outfit:wght@600;700;800;900&family=JetBrains+Mono:wght@400;500;700;800&display=swap" rel="stylesheet">
  
  <!-- CDN Libraries: Mermaid & Canvas Confetti -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>

  <style>
    /* ==========================================================================
       WISROVI MASTERPIECE DESIGN SYSTEM (NEO-CYBER GLASSMORPHISM)
       ========================================================================== */
    :root {
      --bg-canvas: #050811;
      --bg-card: rgba(13, 20, 36, 0.88);
      --bg-card-solid: #0d1424;
      --bg-card-hover: #1e293b;
      --bg-editor: #03060d;
      --border-glass: rgba(56, 189, 248, 0.18);
      --border-accent: #0284c7;
      --border-glow: rgba(2, 132, 199, 0.4);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --primary: #0284c7;
      --primary-hover: #0369a1;
      --primary-glow: rgba(2, 132, 199, 0.35);
      --success: #059669;
      --success-hover: #047857;
      --success-glow: rgba(5, 150, 105, 0.4);
      --accent-gold: #f59e0b;
      --accent-gold-glow: rgba(245, 158, 11, 0.4);
      --accent-purple: #8b5cf6;
      --danger: #ef4444;
      --font-ui: 'Inter', -apple-system, sans-serif;
      --font-display: 'Outfit', sans-serif;
      --font-code: 'JetBrains Mono', 'Fira Code', monospace;
      --radius: 12px;
      --radius-lg: 16px;
      --shadow-card: 0 12px 30px -8px rgba(0, 0, 0, 0.6);
      --shadow-neon: 0 0 20px rgba(2, 132, 199, 0.25);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: var(--font-ui);
      background-color: var(--bg-canvas);
      background-image: 
        radial-gradient(at 0% 0%, rgba(2, 132, 199, 0.15) 0px, transparent 55%),
        radial-gradient(at 100% 0%, rgba(139, 92, 246, 0.12) 0px, transparent 50%),
        radial-gradient(at 50% 100%, rgba(5, 150, 105, 0.08) 0px, transparent 60%);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }

    .app-wrapper {
      display: flex;
      flex-direction: column;
      height: 100vh;
    }

    /* --------------------------------------------------------------------------
       HEADER GAMIFICADO & AUDIO BAR
       -------------------------------------------------------------------------- */
    .app-header {
      background: rgba(10, 16, 30, 0.95);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border-glass);
      padding: 0.75rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 50;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }

    .brand-container {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .brand-logo-badge {
      width: 44px;
      height: 44px;
      background: linear-gradient(135deg, #0284c7, #8b5cf6);
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.6rem;
      box-shadow: 0 0 20px rgba(2, 132, 199, 0.5);
      animation: pulseGlow 4s infinite alternate;
    }

    @keyframes pulseGlow {
      0% { box-shadow: 0 0 15px rgba(2, 132, 199, 0.3); }
      100% { box-shadow: 0 0 25px rgba(139, 92, 246, 0.6); }
    }

    .brand-titles h1 {
      font-family: var(--font-display);
      font-size: 1.3rem;
      font-weight: 900;
      letter-spacing: -0.5px;
      background: linear-gradient(90deg, #38bdf8, #818cf8, #34d399);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .brand-titles p {
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 600;
    }

    .gamification-bar {
      display: flex;
      align-items: center;
      gap: 1.1rem;
    }

    .badge-pill {
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid var(--border-glass);
      padding: 0.45rem 0.95rem;
      border-radius: 999px;
      font-size: 0.82rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      box-shadow: var(--shadow-card);
      transition: all 0.2s;
    }

    .badge-level {
      border-color: rgba(56, 189, 248, 0.5);
      color: #38bdf8;
      background: rgba(2, 132, 199, 0.15);
    }

    .badge-streak {
      border-color: rgba(249, 115, 22, 0.5);
      color: #fb923c;
      background: rgba(249, 115, 22, 0.15);
    }

    .badge-timer {
      border-color: rgba(52, 211, 153, 0.4);
      color: #34d399;
      background: rgba(5, 150, 105, 0.15);
      font-family: var(--font-code);
    }

    .sound-toggle-btn {
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid var(--border-glass);
      color: #cbd5e1;
      padding: 0.45rem 0.8rem;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s;
    }

    .sound-toggle-btn:hover {
      background: #1e293b;
      color: #fff;
    }

    .xp-meter {
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
      width: 150px;
    }

    .xp-text {
      display: flex;
      justify-content: space-between;
      font-size: 0.72rem;
      color: var(--text-muted);
      font-weight: 700;
    }

    .xp-track {
      height: 7px;
      background: #1e293b;
      border-radius: 999px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }

    .xp-fill {
      height: 100%;
      background: linear-gradient(90deg, #0284c7, #38bdf8, #34d399);
      border-radius: 999px;
      transition: width 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    .cert-btn {
      background: linear-gradient(135deg, #78350f, #d97706);
      border: 1px solid #f59e0b;
      color: #fff;
      padding: 0.5rem 1.15rem;
      border-radius: 9px;
      font-size: 0.84rem;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.45rem;
      transition: all 0.2s;
      box-shadow: 0 4px 15px rgba(217, 119, 6, 0.35);
    }

    .cert-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(217, 119, 6, 0.5);
    }

    /* --------------------------------------------------------------------------
       LAYOUT PRINCIPAL
       -------------------------------------------------------------------------- */
    .main-body {
      display: flex;
      flex: 1;
      overflow: hidden;
    }

    /* SIDEBAR CURRICULAR */
    .sidebar {
      width: 340px;
      background: rgba(10, 16, 30, 0.85);
      backdrop-filter: blur(16px);
      border-right: 1px solid var(--border-glass);
      display: flex;
      flex-direction: column;
    }

    .sidebar-title {
      padding: 1.25rem 1.4rem;
      border-bottom: 1px solid var(--border-glass);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .sidebar-title h2 {
      font-family: var(--font-display);
      font-size: 0.95rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      color: var(--text-muted);
    }

    .progress-tag {
      background: rgba(5, 150, 105, 0.2);
      border: 1px solid #059669;
      color: #34d399;
      padding: 0.25rem 0.65rem;
      border-radius: 999px;
      font-size: 0.74rem;
      font-weight: 800;
      box-shadow: 0 0 10px rgba(5, 150, 105, 0.2);
    }

    .curriculum-tree {
      flex: 1;
      overflow-y: auto;
      padding: 0.85rem;
    }

    .course-section {
      margin-bottom: 1.1rem;
    }

    .course-header {
      font-size: 0.74rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: #64748b;
      padding: 0.4rem 0.6rem;
      margin-bottom: 0.3rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .class-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.6rem 0.85rem;
      border-radius: 9px;
      font-size: 0.83rem;
      font-weight: 600;
      color: #94a3b8;
      cursor: pointer;
      margin-bottom: 0.3rem;
      border: 1px solid transparent;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      position: relative;
    }

    .class-item:hover:not(.locked) {
      background: rgba(30, 41, 59, 0.9);
      color: #fff;
      transform: translateX(3px);
    }

    .class-item.active {
      background: linear-gradient(90deg, rgba(2, 132, 199, 0.35), rgba(2, 132, 199, 0.1));
      border-color: #0284c7;
      color: #fff;
      font-weight: 700;
      box-shadow: 0 0 18px rgba(2, 132, 199, 0.25);
    }

    .class-item.completed {
      color: #e2e8f0;
    }

    .class-item.completed .item-status-icon {
      color: #34d399;
      font-weight: 900;
      text-shadow: 0 0 8px rgba(52, 211, 153, 0.6);
    }

    .class-item.locked {
      opacity: 0.45;
      cursor: not-allowed;
    }

    .class-item.locked .item-status-icon {
      color: #64748b;
    }

    /* ESTUDIO CENTRAL */
    .studio {
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow-y: auto;
      padding: 1.75rem 2.25rem;
      gap: 1.4rem;
    }

    /* HERO CARD DE LA CLASE */
    .hero-card {
      background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.7) 100%);
      border: 1px solid var(--border-glass);
      border-radius: var(--radius-lg);
      padding: 1.4rem 1.75rem;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
      position: relative;
    }

    .hero-tags {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .tag-course {
      color: #38bdf8;
      font-size: 0.76rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.6px;
    }

    .tag-boss {
      background: linear-gradient(90deg, #991b1b, #dc2626);
      color: #fff;
      font-size: 0.72rem;
      font-weight: 900;
      padding: 0.2rem 0.6rem;
      border-radius: 6px;
      box-shadow: 0 0 14px rgba(220, 38, 38, 0.5);
      animation: pulseBoss 2s infinite alternate;
    }

    @keyframes pulseBoss {
      0% { transform: scale(0.98); }
      100% { transform: scale(1.02); }
    }

    .hero-title {
      font-family: var(--font-display);
      font-size: 1.55rem;
      font-weight: 900;
      color: #f8fafc;
      letter-spacing: -0.4px;
    }

    .metaphor-box {
      background: rgba(2, 132, 199, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: 9px;
      padding: 0.6rem 1rem;
      font-size: 0.88rem;
      color: #7dd3fc;
      font-style: italic;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
    }

    .listen-btn {
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid #38bdf8;
      color: #38bdf8;
      padding: 0.25rem 0.65rem;
      border-radius: 6px;
      font-size: 0.74rem;
      font-weight: 700;
      cursor: pointer;
      transition: all 0.2s;
    }

    .listen-btn:hover {
      background: #0284c7;
      color: #fff;
    }

    /* --------------------------------------------------------------------------
       CHECKLIST DE LOS 4 PASOS OBLIGATORIOS (BARRA DINÁMICA DE BLOQUEO)
       -------------------------------------------------------------------------- */
    .stepper-container {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 0.75rem;
      background: rgba(10, 16, 30, 0.75);
      padding: 0.6rem;
      border-radius: var(--radius);
      border: 1px solid var(--border-glass);
    }

    .step-gate-pill {
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 9px;
      padding: 0.65rem 0.9rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .step-gate-pill:hover {
      background: rgba(30, 41, 59, 0.8);
    }

    .step-gate-pill.active {
      background: linear-gradient(135deg, rgba(2, 132, 199, 0.35), rgba(2, 132, 199, 0.15));
      border-color: #0284c7;
      box-shadow: 0 0 15px rgba(2, 132, 199, 0.3);
    }

    .step-gate-pill.done {
      border-color: rgba(5, 150, 105, 0.6);
      background: rgba(5, 150, 105, 0.12);
    }

    .step-gate-info {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.83rem;
      font-weight: 700;
      color: #cbd5e1;
    }

    .step-gate-status {
      font-size: 0.72rem;
      font-weight: 800;
      padding: 0.15rem 0.45rem;
      border-radius: 4px;
      background: rgba(100, 116, 139, 0.2);
      color: #94a3b8;
    }

    .step-gate-pill.done .step-gate-status {
      background: rgba(5, 150, 105, 0.3);
      color: #34d399;
    }

    /* CONTENEDOR DE CONTENIDOS */
    .tab-pane {
      display: none;
      flex-direction: column;
      gap: 1.25rem;
      animation: fadeIn 0.3s ease;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .tab-pane.active {
      display: flex;
    }

    .two-col-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.4rem;
    }

    .glass-card {
      background: var(--bg-card);
      backdrop-filter: blur(12px);
      border: 1px solid var(--border-glass);
      border-radius: var(--radius);
      padding: 1.5rem;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .glass-card h3 {
      font-family: var(--font-display);
      font-size: 1.1rem;
      font-weight: 800;
      color: #f1f5f9;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .theory-desc {
      font-size: 0.94rem;
      line-height: 1.7;
      color: #cbd5e1;
    }

    .mentor-box {
      background: rgba(139, 92, 246, 0.12);
      border-left: 4px solid #8b5cf6;
      padding: 1rem 1.25rem;
      border-radius: 0 10px 10px 0;
      display: flex;
      gap: 1rem;
      font-size: 0.88rem;
      color: #ddd6fe;
      align-items: center;
      box-shadow: 0 4px 15px rgba(139, 92, 246, 0.15);
    }

    .mentor-avatar {
      font-size: 1.8rem;
    }

    .mermaid-canvas {
      background: #04060c;
      border: 1px solid var(--border-glass);
      border-radius: 10px;
      padding: 1.25rem;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 290px;
      box-shadow: inset 0 2px 10px rgba(0,0,0,0.6);
    }

    /* EDITORES DE CÓDIGO */
    .code-editor {
      width: 100%;
      height: 250px;
      background: var(--bg-editor);
      border: 1px solid var(--border-glass);
      border-radius: 10px;
      color: #38bdf8;
      font-family: var(--font-code);
      font-size: 0.92rem;
      line-height: 1.55;
      padding: 1rem;
      resize: vertical;
      outline: none;
      box-shadow: inset 0 3px 8px rgba(0,0,0,0.6);
      transition: border-color 0.2s;
    }

    .code-editor:focus {
      border-color: #0284c7;
      box-shadow: 0 0 15px rgba(2, 132, 199, 0.35);
    }

    .terminal-output {
      background: #03050a;
      border: 1px solid var(--border-glass);
      border-radius: 10px;
      padding: 0.85rem 1.15rem;
      font-family: var(--font-code);
      font-size: 0.85rem;
      color: #4ade80;
      min-height: 80px;
      max-height: 200px;
      overflow-y: auto;
      white-space: pre-wrap;
      box-shadow: inset 0 2px 8px rgba(0,0,0,0.7);
    }

    /* VISUALIZADOR DE MEMORIA EN VIVO */
    .memory-board {
      background: #04060c;
      border: 1px solid var(--border-glass);
      border-radius: 10px;
      padding: 1rem;
      min-height: 270px;
      max-height: 340px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }

    .empty-state {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100%;
      color: #64748b;
      font-size: 0.88rem;
      font-style: italic;
    }

    .mem-card {
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid var(--border-glass);
      border-left: 4px solid #0284c7;
      border-radius: 9px;
      padding: 0.7rem 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.88rem;
      transition: transform 0.2s, box-shadow 0.2s;
    }

    .mem-card:hover {
      transform: translateX(4px);
      box-shadow: 0 4px 15px rgba(2, 132, 199, 0.2);
    }

    .mem-name {
      font-weight: 800;
      color: #38bdf8;
      font-family: var(--font-code);
    }

    .mem-type {
      color: #94a3b8;
      font-size: 0.8rem;
      font-family: var(--font-code);
    }

    .mem-bytes-badge {
      background: #1e293b;
      border: 1px solid #334155;
      padding: 0.2rem 0.55rem;
      border-radius: 5px;
      font-size: 0.74rem;
      color: #fbbf24;
      font-weight: 800;
      font-family: var(--font-code);
    }

    .mem-hex-id {
      font-family: var(--font-code);
      font-size: 0.76rem;
      color: #64748b;
    }

    /* BOTONES */
    .btn {
      padding: 0.65rem 1.35rem;
      border-radius: 9px;
      font-weight: 800;
      font-size: 0.88rem;
      cursor: pointer;
      border: none;
      display: inline-flex;
      align-items: center;
      gap: 0.55rem;
      transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    .btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
      transform: none !important;
      box-shadow: none !important;
    }

    .btn-primary {
      background: linear-gradient(135deg, #0284c7, #0369a1);
      color: #fff;
      box-shadow: 0 4px 15px var(--primary-glow);
    }

    .btn-primary:hover:not(:disabled) {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(2, 132, 199, 0.55);
    }

    .btn-success {
      background: linear-gradient(135deg, #059669, #047857);
      color: #fff;
      box-shadow: 0 4px 15px var(--success-glow);
    }

    .btn-success:hover:not(:disabled) {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(5, 150, 105, 0.55);
    }

    .btn-secondary {
      background: #1e293b;
      color: #cbd5e1;
      border: 1px solid #334155;
    }

    .btn-secondary:hover:not(:disabled) {
      background: #334155;
      color: #fff;
      transform: translateY(-1px);
    }

    .flex-between {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    /* FOOTER */
    .studio-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid var(--border-glass);
      padding-top: 1.4rem;
      margin-top: 0.6rem;
    }

    .class-status-summary {
      font-size: 0.85rem;
      color: var(--text-muted);
      font-weight: 700;
    }

    /* MODAL CERTIFICADO */
    .modal-backdrop {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(10px);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 100;
    }

    .modal-backdrop.hidden { display: none; }

    .modal-panel {
      background: #0d1424;
      border: 1px solid var(--border-glass);
      border-radius: var(--radius-lg);
      width: 90%;
      max-width: 880px;
      max-height: 90vh;
      display: flex;
      flex-direction: column;
      padding: 1.85rem;
      gap: 1.1rem;
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.8);
    }

    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .cert-view {
      flex: 1;
      background: #fff;
      border-radius: 10px;
      min-height: 320px;
      max-height: 420px;
      overflow: auto;
      border: 2px solid #d97706;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
  </style>
</head>
<body>
  <div class="app-wrapper">
    
    <!-- HEADER GAMIFICADO -->
    <header class="app-header">
      <div class="brand-container">
        <div class="brand-logo-badge">🐍</div>
        <div class="brand-titles">
          <h1>Wisrovi Academy</h1>
          <p>Virtual AI Tutor &bull; RPG de Aprendizaje en Espiral</p>
        </div>
      </div>

      <div class="gamification-bar">
        <div class="badge-pill badge-level" id="player-level-badge">
          <span>🌱</span>
          <span id="player-level-title">Nv. 1 Aprendiz</span>
        </div>

        <div class="xp-meter">
          <div class="xp-text">
            <span>XP: <strong id="player-xp-val" style="color: #38bdf8;">0</strong></span>
            <span id="xp-progress-percent">0%</span>
          </div>
          <div class="xp-track">
            <div class="xp-fill" id="player-xp-fill" style="width: 5%;"></div>
          </div>
        </div>

        <div class="badge-pill badge-streak" title="Racha de estudio activo">
          <span>🔥</span>
          <span id="player-streak">1 Días</span>
        </div>

        <div class="badge-pill badge-timer" title="Tiempo de pedaleo activo">
          <span>⏱️</span>
          <span id="session-timer">00:00</span>
        </div>

        <button class="sound-toggle-btn" id="sound-toggle-btn" title="Activar/Desactivar Efectos de Sonido">
          <span id="sound-icon">🔊</span> Sonido
        </button>

        <button class="cert-btn" id="open-cert-btn">
          📜 Certificado
        </button>
      </div>
    </header>

    <!-- CUERPO PRINCIPAL -->
    <div class="main-body">
      
      <!-- SIDEBAR CURRICULAR -->
      <aside class="sidebar">
        <div class="sidebar-title">
          <h2>🗺️ Hoja de Ruta (32 Clases)</h2>
          <span class="progress-tag" id="total-progress-pill">0% Hecho</span>
        </div>
        <div class="curriculum-tree" id="class-tree-container">
          <!-- Clases inyectadas por JS -->
        </div>
      </aside>

      <!-- ESTUDIO CENTRAL -->
      <main class="studio">
        
        <!-- HERO CARD DE LA CLASE -->
        <div class="hero-card">
          <div class="hero-tags">
            <span class="tag-course" id="lesson-course-name">Curso 1: Fundamentos Básicos</span>
            <span class="tag-boss" id="lesson-boss-badge" style="display: none;">⚔️ Boss Battle</span>
          </div>
          <h2 class="hero-title" id="lesson-title">Cargando Clase...</h2>
          <div class="metaphor-box">
            <div style="display: flex; align-items: center; gap: 0.5rem;">
              <span>🌟</span>
              <span id="lesson-metaphor">Metáfora: «El Megáfono, las Cajas y el Semáforo»</span>
            </div>
            <button class="listen-btn" id="listen-metaphor-btn">🔊 Escuchar</button>
          </div>
        </div>

        <!-- CHECKLIST DE LOS 4 PASOS OBLIGATORIOS (STEPPER GATES) -->
        <nav class="stepper-container">
          <div class="step-gate-pill active" id="gate-step-1" data-step="1">
            <div class="step-gate-info">
              <span>💡</span> 1. Concepto
            </div>
            <span class="step-gate-status" id="status-step-1">Pendiente</span>
          </div>

          <div class="step-gate-pill" id="gate-step-2" data-step="2">
            <div class="step-gate-info">
              <span>💻</span> 2. Demo
            </div>
            <span class="step-gate-status" id="status-step-2">Pendiente</span>
          </div>

          <div class="step-gate-pill" id="gate-step-3" data-step="3">
            <div class="step-gate-info">
              <span>🔬</span> 3. Arenero
            </div>
            <span class="step-gate-status" id="status-step-3">Pendiente</span>
          </div>

          <div class="step-gate-pill" id="gate-step-4" data-step="4">
            <div class="step-gate-info">
              <span>🏋️</span> 4. Reto
            </div>
            <span class="step-gate-status" id="status-step-4">Pendiente</span>
          </div>
        </nav>

        <!-- PASO 1: CONCEPTO & MERMAID -->
        <div class="tab-pane active" id="pane-step-1">
          <div class="two-col-grid">
            <div class="glass-card">
              <h3>💡 Fundamentación Teórica</h3>
              <p class="theory-desc" id="theory-text">Cargando fundamentación...</p>
              <div class="mentor-box">
                <div class="mentor-avatar">👨‍🏫</div>
                <div>
                  <strong>Consejo del Mentor (Wisrovi):</strong>
                  <p id="mentor-advice">Piensa en los datos como objetos tangibles en la memoria RAM antes de escribir código.</p>
                </div>
              </div>
              <button class="btn btn-success" id="confirm-concept-btn" style="margin-top: auto;">
                ✅ He comprendido el Concepto (Completar Paso 1)
              </button>
            </div>

            <div class="glass-card">
              <h3>🗺️ Arquitectura Visual de Flujo</h3>
              <div class="mermaid-canvas" id="mermaid-render-box"></div>
            </div>
          </div>
        </div>

        <!-- PASO 2: DEMOSTRACIÓN INTERACTIVA -->
        <div class="tab-pane" id="pane-step-2">
          <div class="glass-card">
            <div class="flex-between">
              <h3>💻 Código de Demostración Comentado</h3>
              <button class="btn btn-primary" id="run-demo-btn">▶️ Ejecutar Demo (Completar Paso 2)</button>
            </div>
            <textarea class="code-editor" id="demo-code-area" readonly spellcheck="false"></textarea>
            <div class="terminal-output" id="demo-terminal">&gt; Presiona 'Ejecutar Demo' para compilar y validar.</div>
          </div>
        </div>

        <!-- PASO 3: ARENERO & VISUALIZADOR DE MEMORIA -->
        <div class="tab-pane" id="pane-step-3">
          <div class="two-col-grid">
            <div class="glass-card">
              <div class="flex-between">
                <h3>🔬 Arenero de Experimentación</h3>
                <button class="btn btn-primary" id="run-sandbox-btn">⚡ Inspeccionar Memoria (Completar Paso 3)</button>
              </div>
              <textarea class="code-editor" id="sandbox-code-area" spellcheck="false"></textarea>
              <div class="terminal-output" id="sandbox-terminal">&gt; Modifica variables y pulsa 'Inspeccionar Memoria'.</div>
            </div>

            <div class="glass-card">
              <h3>🧠 Visualizador de Variables & Heap en Vivo</h3>
              <div class="memory-board" id="memory-canvas">
                <div class="empty-state">Ejecuta código para visualizar las variables en la memoria RAM.</div>
              </div>
            </div>
          </div>
        </div>

        <!-- PASO 4: RETO EVALUADO -->
        <div class="tab-pane" id="pane-step-4">
          <div class="two-col-grid">
            <div class="glass-card">
              <div class="flex-between">
                <div>
                  <h3>🏋️ Desafío Práctico de la Clase</h3>
                  <p style="font-size: 0.86rem; color: #94a3b8; margin-top: 0.2rem;" id="challenge-prompt-text">Crea la función indicada.</p>
                </div>
                <button class="btn btn-success" id="eval-challenge-btn">🚀 Evaluar Reto (+150 XP)</button>
              </div>
              <textarea class="code-editor" id="challenge-code-area" spellcheck="false"></textarea>
              <div id="challenge-results-box" style="margin-top: 0.5rem;">
                <div style="color: #64748b; font-size: 0.85rem; font-style: italic;">Modifica la plantilla con tu solución y pulsa 'Evaluar Reto'.</div>
              </div>
            </div>

            <div class="glass-card">
              <h3>💡 Pistas Socráticas del Mentor</h3>
              <div id="hints-accordion" style="display: flex; flex-direction: column; gap: 0.5rem;"></div>
              <div style="background: rgba(2, 132, 199, 0.12); border: 1px solid #0284c7; padding: 0.85rem; border-radius: 9px; margin-top: auto;">
                <strong style="color: #38bdf8;">🏆 Recompensa:</strong>
                <p style="font-size: 0.83rem; color: #cbd5e1; margin-top: 0.25rem;">+150 XP &bull; Sello de acreditación &bull; Desbloqueo de siguiente clase.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- FOOTER DE NAVEGACIÓN CON ESTADO DE DESBLOQUEO -->
        <footer class="studio-footer">
          <button class="btn btn-secondary" id="prev-class-btn">⬅️ Clase Anterior</button>
          <div class="class-status-summary" id="class-status-summary">
            🔒 Completa los 4 pasos para desbloquear la siguiente clase.
          </div>
          <button class="btn btn-primary" id="next-class-btn" disabled>Siguiente Clase ➡️</button>
        </footer>

      </main>
    </div>

    <!-- MODAL DE CERTIFICADO -->
    <div class="modal-backdrop hidden" id="cert-modal">
      <div class="modal-panel">
        <div class="modal-header">
          <h2>📜 Certificación Oficial de Acreditación</h2>
          <button style="background:none; border:none; color:#fff; font-size:1.6rem; cursor:pointer;" id="close-cert-btn">&times;</button>
        </div>
        <div style="display:flex; gap:0.6rem; align-items:center;">
          <label style="font-size:0.88rem; color:#94a3b8;">Nombre en el Diploma:</label>
          <input type="text" id="student-name-input" style="flex:1; padding:0.5rem 0.75rem; background:#060911; border:1px solid #334155; color:#fff; border-radius:7px; font-weight:700;" value="Alejandro Martínez">
          <button class="btn btn-primary" id="refresh-cert-btn">Actualizar Vista</button>
        </div>
        <div class="cert-view" id="cert-preview-frame"></div>
        <div style="display:flex; justify-content:flex-end; gap:0.75rem;">
          <button class="btn btn-secondary" id="copy-badge-btn">📋 Copiar Badge GitHub</button>
          <button class="btn btn-success" id="download-cert-btn">📥 Descargar PDF Oficial</button>
        </div>
      </div>
    </div>

  </div>

  <!-- SCRIPT JS REACTIVO CON SINTETIZADOR DE AUDIO Y BLOQUEOS -->
  <script>
    document.addEventListener("DOMContentLoaded", () => {
      // Estado de la aplicación
      const state = {
        currentCourse: 1,
        currentClass: 1,
        profile: null,
        curriculum: [],
        classContent: null,
        currentStep: 1,
        soundEnabled: true,
        // Checklist de los 4 pasos obligatorios
        stepsCompleted: { 1: false, 2: false, 3: false, 4: false },
        starterChallengeCode: "",
        elapsedSeconds: 0
      };

      // Sintetizador de Audio Web (Web Audio API nativa sin archivos externos)
      const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      function playTone(freq, type, duration, gainVal = 0.1) {
        if (!state.soundEnabled || !audioCtx) return;
        try {
          if (audioCtx.state === 'suspended') audioCtx.resume();
          const osc = audioCtx.createOscillator();
          const gain = audioCtx.createGain();
          osc.type = type;
          osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
          gain.gain.setValueAtTime(gainVal, audioCtx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);
          osc.connect(gain);
          gain.connect(audioCtx.destination);
          osc.start();
          osc.stop(audioCtx.currentTime + duration);
        } catch (e) {}
      }

      function soundClick() { playTone(440, 'sine', 0.08, 0.05); }
      function soundChime() { playTone(587.33, 'triangle', 0.15, 0.08); setTimeout(() => playTone(880, 'sine', 0.25, 0.08), 100); }
      function soundVictory() {
        [523.25, 659.25, 783.99, 1046.50].forEach((f, idx) => {
          setTimeout(() => playTone(f, 'triangle', 0.35, 0.1), idx * 120);
        });
      }
      function soundError() { playTone(220, 'sawtooth', 0.2, 0.1); }

      // Inicializar Mermaid
      if (window.mermaid) {
        mermaid.initialize({ startOnLoad: false, theme: "dark", securityLevel: "loose" });
      }

      // Temporizador de sesión
      setInterval(() => {
        state.elapsedSeconds++;
        const m = Math.floor(state.elapsedSeconds / 60).toString().padStart(2, '0');
        const s = (state.elapsedSeconds % 60).toString().padStart(2, '0');
        document.getElementById("session-timer").textContent = `${m}:${s}`;
      }, 1000);

      const dom = {
        levelTitle: document.getElementById("player-level-title"),
        xpVal: document.getElementById("player-xp-val"),
        xpPercent: document.getElementById("xp-progress-percent"),
        xpFill: document.getElementById("player-xp-fill"),
        streak: document.getElementById("player-streak"),
        progressPill: document.getElementById("total-progress-pill"),
        classTree: document.getElementById("class-tree-container"),
        courseName: document.getElementById("lesson-course-name"),
        bossBadge: document.getElementById("lesson-boss-badge"),
        lessonTitle: document.getElementById("lesson-title"),
        metaphor: document.getElementById("lesson-metaphor"),
        listenMetaphorBtn: document.getElementById("listen-metaphor-btn"),
        soundToggleBtn: document.getElementById("sound-toggle-btn"),
        soundIcon: document.getElementById("sound-icon"),
        
        // Stepper gates
        gatePills: document.querySelectorAll(".step-gate-pill"),
        statusStep1: document.getElementById("status-step-1"),
        statusStep2: document.getElementById("status-step-2"),
        statusStep3: document.getElementById("status-step-3"),
        statusStep4: document.getElementById("status-step-4"),
        tabPanes: document.querySelectorAll(".tab-pane"),
        
        // Paso 1
        theoryText: document.getElementById("theory-text"),
        mermaidBox: document.getElementById("mermaid-render-box"),
        confirmConceptBtn: document.getElementById("confirm-concept-btn"),

        // Paso 2
        demoCode: document.getElementById("demo-code-area"),
        demoTerm: document.getElementById("demo-terminal"),
        runDemoBtn: document.getElementById("run-demo-btn"),

        // Paso 3
        sandboxCode: document.getElementById("sandbox-code-area"),
        sandboxTerm: document.getElementById("sandbox-terminal"),
        runSandboxBtn: document.getElementById("run-sandbox-btn"),
        memoryCanvas: document.getElementById("memory-canvas"),

        // Paso 4
        challengePrompt: document.getElementById("challenge-prompt-text"),
        challengeCode: document.getElementById("challenge-code-area"),
        challengeResults: document.getElementById("challenge-results-box"),
        evalChallengeBtn: document.getElementById("eval-challenge-btn"),
        hintsAccordion: document.getElementById("hints-accordion"),

        // Footer
        prevBtn: document.getElementById("prev-class-btn"),
        nextBtn: document.getElementById("next-class-btn"),
        classStatusSummary: document.getElementById("class-status-summary"),

        // Certificado
        certModal: document.getElementById("cert-modal"),
        openCertBtn: document.getElementById("open-cert-btn"),
        closeCertBtn: document.getElementById("close-cert-btn"),
        studentNameInput: document.getElementById("student-name-input"),
        certPreviewFrame: document.getElementById("cert-preview-frame"),
        refreshCertBtn: document.getElementById("refresh-cert-btn"),
        copyBadgeBtn: document.getElementById("copy-badge-btn"),
        downloadCertBtn: document.getElementById("download-cert-btn")
      };

      async function initApp() {
        await fetchProfile();
        await fetchCurriculum();
        await loadClass(state.currentCourse, state.currentClass);
        setupEvents();
      }

      async function fetchProfile() {
        try {
          const res = await fetch("/api/progress");
          const data = await res.json();
          state.profile = data;
          state.currentCourse = data.current_course || 1;
          state.currentClass = data.current_class || 1;
          updateProfileUI();
        } catch (e) { console.error(e); }
      }

      function updateProfileUI() {
        if (!state.profile) return;
        const p = state.profile;
        dom.levelTitle.textContent = `Nv. ${p.level} ${p.level_title.split(' ')[1] || 'Aprendiz'}`;
        dom.xpVal.textContent = p.xp;
        dom.streak.textContent = `${p.streak_days} Días`;
        const currentLvlXP = p.xp % 500;
        const pct = Math.min(100, Math.round((currentLvlXP / 500) * 100));
        dom.xpPercent.textContent = `${pct}%`;
        dom.xpFill.style.width = `${pct}%`;
      }

      async function fetchCurriculum() {
        try {
          const res = await fetch("/api/curriculum");
          const data = await res.json();
          state.curriculum = data.classes;
          dom.progressPill.textContent = `${data.progress_percent}% Completado`;
          renderTree();
        } catch (e) { console.error(e); }
      }

      function isClassUnlocked(courseNum, classNum) {
        if (courseNum > 1) return false; // Cursos 2, 3 y 4 desactivados por ahora
        if (courseNum === 1 && classNum === 1) return true;
        const completed = new Set(state.profile ? state.profile.completed_classes : []);
        return completed.has(`1-${classNum - 1}`);
      }

      function renderTree() {
        dom.classTree.innerHTML = "";
        const courses = [
          { id: 1, name: "Curso 1: Fundamentos Básicos", available: true },
          { id: 2, name: "Curso 2: Algoritmos y Estructuras", available: false, badge: "Próximamente" },
          { id: 3, name: "Curso 3: Agentes de IA", available: false, badge: "Próximamente" },
          { id: 4, name: "Curso 4: Proyecto Final Integrador", available: false, badge: "Próximamente" }
        ];

        courses.forEach(c => {
          const grp = document.createElement("div");
          grp.className = "course-section";
          const badgeHtml = c.available ? "" : '<span style="color:#fbbf24; font-size:0.68rem; text-transform:none; border:1px solid rgba(245,158,11,0.4); padding:0.1rem 0.4rem; border-radius:4px; background:rgba(245,158,11,0.1);">🔒 Próximamente</span>';
          grp.innerHTML = `<div class="course-header"><span>${c.name}</span> ${badgeHtml}</div>`;

          const courseClasses = state.curriculum.filter(cls => cls.course_num === c.id);
          courseClasses.forEach(cls => {
            const item = document.createElement("div");
            const isActive = (cls.course_num === state.currentCourse && cls.class_num === state.currentClass);
            const unlocked = isClassUnlocked(cls.course_num, cls.class_num);
            
            item.className = `class-item ${isActive ? 'active' : ''} ${cls.completed ? 'completed' : ''} ${!unlocked ? 'locked' : ''}`;
            const boss = cls.boss_battle ? "⚔️ " : "";
            const lockIcon = cls.completed ? "✓" : (unlocked ? "○" : "🔒");
            
            item.innerHTML = `
              <span>${boss}S${cls.class_num.toString().padStart(2, '0')}: ${cls.title.split(':')[1] || cls.title}</span>
              <span class="item-status-icon">${lockIcon}</span>
            `;

            if (unlocked) {
              item.addEventListener("click", () => {
                soundClick();
                loadClass(cls.course_num, cls.class_num);
              });
            } else {
              item.addEventListener("click", () => {
                soundError();
                if (!c.available) {
                  alert("🔒 Este curso se encuentra temporalmente desactivado. Completa las 8 clases del Curso 1: Fundamentos Básicos de Python para obtener tu acreditación oficial.");
                } else {
                  alert("🔒 Esta clase está bloqueada. Debes completar y superar la clase anterior.");
                }
              });
            }

            grp.appendChild(item);
          });
          dom.classTree.appendChild(grp);
        });
      }

      async function loadClass(courseNum, classNum) {
        state.currentCourse = courseNum;
        state.currentClass = classNum;
        
        // Reiniciar estado de los 4 pasos si no está previamente completada
        const key = `${courseNum}-${classNum}`;
        const isDone = state.profile && state.profile.completed_classes.includes(key);
        state.stepsCompleted = { 1: isDone, 2: isDone, 3: isDone, 4: isDone };

        try {
          const res = await fetch(`/api/class/${courseNum}/${classNum}`);
          const data = await res.json();
          state.classContent = data;
          renderClass(data);
          updateStepperUI();
          renderTree();
          switchStep(1);
        } catch (e) { console.error(e); }
      }

      function renderClass(data) {
        dom.courseName.textContent = data.course_name;
        dom.lessonTitle.textContent = data.title;
        dom.metaphor.textContent = `Metáfora Central: «${data.metaphor}»`;
        dom.bossBadge.style.display = data.boss_battle ? "inline-block" : "none";

        dom.theoryText.innerHTML = data.theory.replace(/\\n/g, "<br>");
        renderMermaid(data.mermaid);

        dom.demoCode.value = data.demo_code;
        dom.demoTerm.innerHTML = "&gt; Presiona 'Ejecutar Demo' para compilar y validar el paso 2.";

        dom.sandboxCode.value = data.playground_code;
        dom.sandboxTerm.innerHTML = "&gt; Modifica variables y pulsa 'Inspeccionar Memoria' para el paso 3.";
        dom.memoryCanvas.innerHTML = `<div class="empty-state">Ejecuta código para visualizar las variables en la memoria RAM.</div>`;

        dom.challengePrompt.textContent = data.challenge_prompt;
        state.starterChallengeCode = data.challenge_starter;
        dom.challengeCode.value = data.challenge_starter;
        dom.challengeResults.innerHTML = `<div style="color: #64748b; font-size: 0.85rem; font-style: italic;">Modifica la plantilla y pulsa 'Evaluar Reto'.</div>`;

        dom.hintsAccordion.innerHTML = "";
        data.socratic_hints.forEach((h, idx) => {
          const d = document.createElement("details");
          d.style.cssText = "background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(56, 189, 248, 0.2); border-radius: 8px; padding: 0.6rem 0.85rem; font-size: 0.84rem; color: #cbd5e1; cursor: pointer;";
          d.innerHTML = `<summary style="font-weight: 700; color: #38bdf8;">💡 Pista ${idx + 1}</summary><p style="margin-top: 0.4rem;">${h}</p>`;
          dom.hintsAccordion.appendChild(d);
        });
      }

      function renderMermaid(chartCode) {
        dom.mermaidBox.innerHTML = "";
        if (window.mermaid && chartCode) {
          const id = "mermaid-svg-" + Date.now();
          mermaid.render(id, chartCode).then(({ svg }) => {
            dom.mermaidBox.innerHTML = svg;
          }).catch(err => {
            dom.mermaidBox.innerHTML = `<pre style="color:#94a3b8; font-size:0.8rem;">${chartCode}</pre>`;
          });
        }
      }

      function updateStepperUI() {
        dom.gatePills.forEach(pill => {
          const s = parseInt(pill.dataset.step);
          const isDone = state.stepsCompleted[s];
          pill.classList.toggle("done", isDone);
          const statusElem = document.getElementById(`status-step-${s}`);
          if (statusElem) {
            statusElem.textContent = isDone ? "✓ Hecho" : "Pendiente";
          }
        });

        // Verificar si los 4 pasos están completos
        const allDone = Object.values(state.stepsCompleted).every(Boolean);
        dom.nextBtn.disabled = !allDone;
        if (allDone) {
          dom.classStatusSummary.innerHTML = "<span style='color:#34d399; font-weight:800;'>🎉 ¡Clase completada! Puedes avanzar a la siguiente.</span>";
        } else {
          const remaining = Object.entries(state.stepsCompleted).filter(([k, v]) => !v).map(([k]) => `Paso ${k}`).join(", ");
          dom.classStatusSummary.innerHTML = `🔒 <span style="color:#fb923c;">Faltan por completar: ${remaining}</span>`;
        }
      }

      function switchStep(num) {
        soundClick();
        state.currentStep = num;
        dom.gatePills.forEach(p => p.classList.toggle("active", parseInt(p.dataset.step) === num));
        dom.tabPanes.forEach(p => p.classList.toggle("active", p.id === `pane-step-${num}`));
      }

      function setupEvents() {
        // Stepper tabs
        dom.gatePills.forEach(pill => {
          pill.addEventListener("click", () => switchStep(parseInt(pill.dataset.step)));
        });

        // Paso 1: Confirmar concepto
        dom.confirmConceptBtn.addEventListener("click", () => {
          state.stepsCompleted[1] = true;
          soundChime();
          updateStepperUI();
          switchStep(2);
        });

        // Paso 2: Ejecutar Demo
        dom.runDemoBtn.addEventListener("click", async () => {
          soundClick();
          dom.demoTerm.innerHTML = "&gt; Compilando y ejecutando demo...";
          const res = await fetch("/api/run-code", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: dom.demoCode.value })
          });
          const data = await res.json();
          dom.demoTerm.innerHTML = `&gt; ${data.stdout || data.stderr || 'Demo ejecutado con éxito.'}`;
          state.stepsCompleted[2] = true;
          soundChime();
          updateStepperUI();
        });

        // Paso 3: Ejecutar Arenero & Memoria
        dom.runSandboxBtn.addEventListener("click", async () => {
          soundClick();
          dom.sandboxTerm.innerHTML = "&gt; Inspeccionando estado del Heap en RAM...";
          const res = await fetch("/api/run-code", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: dom.sandboxCode.value })
          });
          const data = await res.json();
          dom.sandboxTerm.innerHTML = `&gt; ${data.stdout || data.stderr || 'Ejecutado.'}`;
          renderMemory(data.memory_variables);
          state.stepsCompleted[3] = true;
          soundChime();
          updateStepperUI();
        });

        // Paso 4: Evaluar Reto
        dom.evalChallengeBtn.addEventListener("click", async () => {
          soundClick();
          const currentCode = dom.challengeCode.value.trim();
          
          // Validación: Debe haber modificado el código de inicio
          if (currentCode === state.starterChallengeCode.trim()) {
            soundError();
            dom.challengeResults.innerHTML = `
              <div style="background: rgba(245, 158, 11, 0.2); border: 1px solid #f59e0b; color: #fde68a; padding: 0.75rem; border-radius: 8px;">
                ⚠️ <strong>¡Debes escribir tu solución!</strong><br>
                Modifica el código de la plantilla antes de solicitar la evaluación.
              </div>
            `;
            return;
          }

          dom.challengeResults.innerHTML = "<div style='color:#38bdf8;'>🧪 Ejecutando suite de pruebas automatizadas...</div>";
          const res = await fetch("/api/evaluate-challenge", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              course_num: state.currentCourse,
              class_num: state.currentClass,
              code: currentCode
            })
          });
          const data = await res.json();

          if (data.evaluation.passed) {
            state.stepsCompleted[4] = true;
            soundVictory();
            if (window.confetti) confetti({ particleCount: 150, spread: 90, origin: { y: 0.6 } });
            dom.challengeResults.innerHTML = `
              <div style="background: rgba(5,150,105,0.25); border: 1px solid #059669; color: #6ee7b7; padding: 0.85rem; border-radius: 8px; box-shadow: 0 0 20px rgba(5,150,105,0.3);">
                🎉 <strong>¡RETO SUPERADO CON ÉXITO! (+150 XP)</strong><br>
                Tu solución ha superado el 100% de las pruebas y contratos de tipado.
              </div>
            `;
            await fetchProfile();
            await fetchCurriculum();
            updateStepperUI();
          } else {
            soundError();
            dom.challengeResults.innerHTML = `
              <div style="background: rgba(220,38,38,0.25); border: 1px solid #dc2626; color: #fca5a5; padding: 0.85rem; border-radius: 8px;">
                ⚠️ <strong>La solución aún no cumple todas las aserciones:</strong><br>
                <p style="margin-top:0.35rem; font-size:0.86rem;">${data.evaluation.socratic_hint}</p>
              </div>
            `;
          }
        });

        // Escuchar metáfora con voz
        dom.listenMetaphorBtn.addEventListener("click", () => {
          if ('speechSynthesis' in window && state.classContent) {
            window.speechSynthesis.cancel();
            const text = `${state.classContent.title}. Metáfora central: ${state.classContent.metaphor}. ${state.classContent.theory}`;
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'es-ES';
            utterance.rate = 1.0;
            window.speechSynthesis.speak(utterance);
          } else {
            alert("Tu navegador no soporta síntesis de voz.");
          }
        });

        // Alternar sonido
        dom.soundToggleBtn.addEventListener("click", () => {
          state.soundEnabled = !state.soundEnabled;
          dom.soundIcon.textContent = state.soundEnabled ? "🔊" : "🔇";
          dom.soundToggleBtn.style.borderColor = state.soundEnabled ? "#38bdf8" : "#64748b";
        });

        // Footer buttons (Exclusivo Curso 1)
        dom.prevBtn.addEventListener("click", () => {
          if (state.currentClass > 1) {
            loadClass(1, state.currentClass - 1);
          }
        });

        dom.nextBtn.addEventListener("click", () => {
          if (dom.nextBtn.disabled) return;
          if (state.currentClass < 8) {
            loadClass(1, state.currentClass + 1);
          } else if (state.currentClass === 8) {
            soundVictory();
            alert("🎉 ¡FELICITACIONES! Has completado y superado las 8 clases del Curso 1: Fundamentos Básicos de Python.\\n\\nGenerando tu Certificado Oficial de Acreditación...");
            openCert();
          }
        });

        // Certificado
        dom.openCertBtn.addEventListener("click", () => openCert());
        dom.closeCertBtn.addEventListener("click", () => dom.certModal.classList.add("hidden"));
        dom.refreshCertBtn.addEventListener("click", () => openCert());

        dom.copyBadgeBtn.addEventListener("click", () => {
          const badge = `[![Wisrovi Certified](https://img.shields.io/badge/Wisrovi%20Academy-Certified%20AI%20Engineer-gold.svg)](https://academy_python.wisrovi.dev)`;
          navigator.clipboard.writeText(badge);
          alert("¡Badge Markdown copiado al portapapeles!");
        });
      }

      function renderMemory(vars) {
        if (!vars || vars.length === 0) {
          dom.memoryCanvas.innerHTML = `<div class="empty-state">No se detectaron variables en el scope actual.</div>`;
          return;
        }
        dom.memoryCanvas.innerHTML = "";
        vars.forEach(v => {
          const c = document.createElement("div");
          c.className = "mem-card";
          c.innerHTML = `
            <div>
              <span class="mem-name">${v.icon} ${v.name}</span>
              <span class="mem-type">(${v.type})</span> = <strong style="color:#fff;">${v.value}</strong>
            </div>
            <div style="display:flex; gap:0.6rem; align-items:center;">
              <span class="mem-bytes-badge">${v.size_bytes} Bytes</span>
              <span class="mem-hex-id">${v.id}</span>
            </div>
          `;
          dom.memoryCanvas.appendChild(c);
        });
      }

      async function openCert() {
        dom.certModal.classList.remove("hidden");
        const name = dom.studentNameInput.value || "Alejandro Martínez";
        const res = await fetch("/api/certificate/generate", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ student_name: name, course_title: "Programa Integral de Formación en Python: De Cero a Agentes de IA", hours: 160 })
        });
        const data = await res.json();
        dom.certPreviewFrame.innerHTML = data.html;
      }

      initApp();
    });
  </script>
</body>
</html>
"""
