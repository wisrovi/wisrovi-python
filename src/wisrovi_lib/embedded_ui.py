#!/usr/bin/env python3
"""
Embedded UI Frontend (Wisrovi Academy - Virtual AI Tutor & RPG).
Garantiza que la interfaz web completa se sirva siempre al 100%,
incluso si los archivos estáticos no se hubieran empaquetado en el wheel.
"""

def get_embedded_html() -> str:
    return """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wisrovi Academy - Virtual AI Tutor & RPG</title>
  
  <!-- Google Fonts: Inter & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  
  <!-- CDN Libraries: Mermaid & Canvas Confetti -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>

  <style>
    /* ==========================================================================
       WISROVI DESIGN SYSTEM (NEO-CYBER GLASSMORPHISM)
       ========================================================================== */
    :root {
      --bg-canvas: #070a13;
      --bg-card: rgba(15, 23, 42, 0.85);
      --bg-card-solid: #0f172a;
      --bg-card-hover: #1e293b;
      --bg-editor: #060911;
      --border-glass: rgba(56, 189, 248, 0.15);
      --border-accent: #0284c7;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --primary: #0284c7;
      --primary-hover: #0369a1;
      --success: #059669;
      --success-hover: #047857;
      --accent-gold: #f59e0b;
      --accent-purple: #8b5cf6;
      --danger: #ef4444;
      --font-ui: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      --font-code: 'JetBrains Mono', 'Fira Code', monospace;
      --radius: 12px;
      --shadow-glow: 0 10px 30px -10px rgba(2, 132, 199, 0.3);
      --shadow-card: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: var(--font-ui);
      background-color: var(--bg-canvas);
      background-image: 
        radial-gradient(at 0% 0%, rgba(2, 132, 199, 0.12) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(139, 92, 246, 0.08) 0px, transparent 50%);
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
       HEADER GAMIFICADO
       -------------------------------------------------------------------------- */
    .app-header {
      background: rgba(15, 23, 42, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-glass);
      padding: 0.75rem 1.75rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 50;
    }

    .brand-container {
      display: flex;
      align-items: center;
      gap: 0.85rem;
    }

    .brand-logo-badge {
      width: 42px;
      height: 42px;
      background: linear-gradient(135deg, #0284c7, #8b5cf6);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      box-shadow: 0 0 15px rgba(2, 132, 199, 0.4);
    }

    .brand-titles h1 {
      font-size: 1.2rem;
      font-weight: 900;
      letter-spacing: -0.5px;
      background: linear-gradient(90deg, #38bdf8, #818cf8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .brand-titles p {
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 500;
    }

    .gamification-bar {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .badge-pill {
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid var(--border-glass);
      padding: 0.4rem 0.85rem;
      border-radius: 999px;
      font-size: 0.82rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.45rem;
      transition: all 0.2s;
    }

    .badge-level {
      border-color: rgba(56, 189, 248, 0.4);
      color: #38bdf8;
      background: rgba(2, 132, 199, 0.1);
    }

    .badge-streak {
      border-color: rgba(249, 115, 22, 0.4);
      color: #fb923c;
      background: rgba(249, 115, 22, 0.1);
    }

    .xp-meter {
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
      width: 140px;
    }

    .xp-text {
      display: flex;
      justify-content: space-between;
      font-size: 0.72rem;
      color: var(--text-muted);
      font-weight: 600;
    }

    .xp-track {
      height: 6px;
      background: #1e293b;
      border-radius: 999px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .xp-fill {
      height: 100%;
      background: linear-gradient(90deg, #0284c7, #38bdf8);
      border-radius: 999px;
      transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .cert-btn {
      background: linear-gradient(135deg, #78350f, #d97706);
      border: 1px solid #f59e0b;
      color: #fff;
      padding: 0.45rem 1rem;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s;
      box-shadow: 0 4px 12px rgba(217, 119, 6, 0.25);
    }

    .cert-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(217, 119, 6, 0.4);
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
      width: 330px;
      background: rgba(15, 23, 42, 0.7);
      backdrop-filter: blur(10px);
      border-right: 1px solid var(--border-glass);
      display: flex;
      flex-direction: column;
    }

    .sidebar-title {
      padding: 1.1rem 1.25rem;
      border-bottom: 1px solid var(--border-glass);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .sidebar-title h2 {
      font-size: 0.88rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-muted);
    }

    .progress-tag {
      background: rgba(5, 150, 105, 0.15);
      border: 1px solid #059669;
      color: #34d399;
      padding: 0.2rem 0.6rem;
      border-radius: 999px;
      font-size: 0.72rem;
      font-weight: 800;
    }

    .curriculum-tree {
      flex: 1;
      overflow-y: auto;
      padding: 0.75rem;
    }

    .course-section {
      margin-bottom: 1rem;
    }

    .course-header {
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: #64748b;
      padding: 0.35rem 0.5rem;
      margin-bottom: 0.25rem;
    }

    .class-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.55rem 0.75rem;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 500;
      color: #cbd5e1;
      cursor: pointer;
      margin-bottom: 0.25rem;
      border: 1px solid transparent;
      transition: all 0.15s ease;
    }

    .class-item:hover {
      background: rgba(30, 41, 59, 0.8);
      color: #fff;
    }

    .class-item.active {
      background: linear-gradient(90deg, rgba(2, 132, 199, 0.3), rgba(2, 132, 199, 0.1));
      border-color: #0284c7;
      color: #fff;
      font-weight: 700;
      box-shadow: 0 0 15px rgba(2, 132, 199, 0.2);
    }

    .class-item.completed .item-status-icon {
      color: #34d399;
      font-weight: 900;
    }

    /* ESTUDIO CENTRAL */
    .studio {
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow-y: auto;
      padding: 1.5rem 2rem;
      gap: 1.25rem;
    }

    /* HERO CARD DE LA CLASE */
    .hero-card {
      background: linear-gradient(135deg, rgba(15, 23, 42, 0.9) 0%, rgba(30, 41, 59, 0.6) 100%);
      border: 1px solid var(--border-glass);
      border-radius: var(--radius);
      padding: 1.25rem 1.5rem;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .hero-tags {
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }

    .tag-course {
      color: #38bdf8;
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .tag-boss {
      background: linear-gradient(90deg, #991b1b, #dc2626);
      color: #fff;
      font-size: 0.7rem;
      font-weight: 800;
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
      box-shadow: 0 0 10px rgba(220, 38, 38, 0.4);
    }

    .hero-title {
      font-size: 1.45rem;
      font-weight: 900;
      color: #f8fafc;
      letter-spacing: -0.3px;
    }

    .metaphor-box {
      background: rgba(2, 132, 199, 0.08);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 8px;
      padding: 0.5rem 0.85rem;
      font-size: 0.85rem;
      color: #7dd3fc;
      font-style: italic;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    /* PESTAÑAS PASO A PASO (1..4) */
    .step-tabs {
      display: flex;
      gap: 0.6rem;
      border-bottom: 1px solid var(--border-glass);
      padding-bottom: 0.6rem;
    }

    .tab-btn {
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid var(--border-glass);
      color: var(--text-muted);
      padding: 0.55rem 1.15rem;
      border-radius: 10px;
      font-size: 0.85rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .tab-btn:hover {
      background: #1e293b;
      color: #fff;
    }

    .tab-btn.active {
      background: linear-gradient(135deg, #0284c7, #0369a1);
      border-color: #38bdf8;
      color: #fff;
      box-shadow: 0 0 15px rgba(2, 132, 199, 0.4);
    }

    .tab-badge {
      width: 20px;
      height: 20px;
      background: rgba(255, 255, 255, 0.18);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.72rem;
    }

    /* CONTENEDOR DE PASOS */
    .tab-pane {
      display: none;
      flex-direction: column;
      gap: 1.25rem;
    }

    .tab-pane.active {
      display: flex;
    }

    .two-col-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.25rem;
    }

    .glass-card {
      background: var(--bg-card);
      border: 1px solid var(--border-glass);
      border-radius: var(--radius);
      padding: 1.35rem;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }

    .glass-card h3 {
      font-size: 1.05rem;
      font-weight: 800;
      color: #f1f5f9;
    }

    .theory-desc {
      font-size: 0.92rem;
      line-height: 1.65;
      color: #cbd5e1;
    }

    .mentor-box {
      background: rgba(139, 92, 246, 0.1);
      border-left: 4px solid #8b5cf6;
      padding: 0.85rem 1rem;
      border-radius: 0 8px 8px 0;
      display: flex;
      gap: 0.85rem;
      font-size: 0.86rem;
      color: #ddd6fe;
      align-items: center;
    }

    .mentor-avatar {
      font-size: 1.6rem;
    }

    .mermaid-canvas {
      background: #060911;
      border: 1px solid var(--border-glass);
      border-radius: 8px;
      padding: 1rem;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 270px;
    }

    /* EDITORES DE CÓDIGO */
    .code-editor {
      width: 100%;
      height: 240px;
      background: var(--bg-editor);
      border: 1px solid var(--border-glass);
      border-radius: 8px;
      color: #38bdf8;
      font-family: var(--font-code);
      font-size: 0.9rem;
      line-height: 1.5;
      padding: 0.85rem;
      resize: vertical;
      outline: none;
      box-shadow: inset 0 2px 6px rgba(0,0,0,0.5);
    }

    .code-editor:focus {
      border-color: #0284c7;
      box-shadow: 0 0 12px rgba(2, 132, 199, 0.3);
    }

    .terminal-output {
      background: #04060b;
      border: 1px solid var(--border-glass);
      border-radius: 8px;
      padding: 0.75rem 1rem;
      font-family: var(--font-code);
      font-size: 0.83rem;
      color: #4ade80;
      min-height: 70px;
      max-height: 180px;
      overflow-y: auto;
      white-space: pre-wrap;
    }

    /* VISUALIZADOR DE MEMORIA */
    .memory-board {
      background: #060911;
      border: 1px solid var(--border-glass);
      border-radius: 8px;
      padding: 0.85rem;
      min-height: 260px;
      max-height: 320px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .empty-state {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100%;
      color: #64748b;
      font-size: 0.85rem;
      font-style: italic;
    }

    .mem-card {
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid var(--border-glass);
      border-left: 4px solid #0284c7;
      border-radius: 8px;
      padding: 0.6rem 0.85rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.85rem;
      transition: transform 0.2s;
    }

    .mem-card:hover {
      transform: translateX(4px);
    }

    .mem-name {
      font-weight: 800;
      color: #38bdf8;
    }

    .mem-type {
      color: #94a3b8;
      font-size: 0.78rem;
    }

    .mem-bytes-badge {
      background: #1e293b;
      border: 1px solid #334155;
      padding: 0.15rem 0.5rem;
      border-radius: 4px;
      font-size: 0.72rem;
      color: #fbbf24;
      font-weight: 700;
    }

    .mem-hex-id {
      font-family: var(--font-code);
      font-size: 0.75rem;
      color: #64748b;
    }

    /* RETOS & BOTONES */
    .btn {
      padding: 0.6rem 1.25rem;
      border-radius: 8px;
      font-weight: 800;
      font-size: 0.86rem;
      cursor: pointer;
      border: none;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .btn-primary {
      background: linear-gradient(135deg, #0284c7, #0369a1);
      color: #fff;
      box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3);
    }

    .btn-primary:hover {
      transform: translateY(-1px);
      box-shadow: 0 6px 16px rgba(2, 132, 199, 0.5);
    }

    .btn-success {
      background: linear-gradient(135deg, #059669, #047857);
      color: #fff;
      box-shadow: 0 4px 12px rgba(5, 150, 105, 0.3);
    }

    .btn-success:hover {
      transform: translateY(-1px);
      box-shadow: 0 6px 16px rgba(5, 150, 105, 0.5);
    }

    .btn-secondary {
      background: #1e293b;
      color: #cbd5e1;
      border: 1px solid #334155;
    }

    .btn-secondary:hover {
      background: #334155;
      color: #fff;
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
      border-top: 1px solid var(--border-glass);
      padding-top: 1.25rem;
      margin-top: 0.5rem;
    }

    /* MODAL CERTIFICADO */
    .modal-backdrop {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 0, 0, 0.85);
      backdrop-filter: blur(8px);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 100;
    }

    .modal-backdrop.hidden { display: none; }

    .modal-panel {
      background: #0f172a;
      border: 1px solid var(--border-glass);
      border-radius: var(--radius);
      width: 90%;
      max-width: 860px;
      max-height: 90vh;
      display: flex;
      flex-direction: column;
      padding: 1.75rem;
      gap: 1rem;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
    }

    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .cert-view {
      flex: 1;
      background: #fff;
      border-radius: 8px;
      min-height: 300px;
      max-height: 400px;
      overflow: auto;
      border: 2px solid #d97706;
    }
  </style>
</head>
<body>
  <div class="app-wrapper">
    
    <!-- HEADER -->
    <header class="app-header">
      <div class="brand-container">
        <div class="brand-logo-badge">🐍</div>
        <div class="brand-titles">
          <h1>Wisrovi Academy</h1>
          <p>Virtual AI Tutor & RPG de Programación</p>
        </div>
      </div>

      <div class="gamification-bar">
        <div class="badge-pill badge-level" id="player-level-badge">
          <span>🌱</span>
          <span id="player-level-title">Nv. 1 Aprendiz</span>
        </div>

        <div class="xp-meter">
          <div class="xp-text">
            <span>XP: <strong id="player-xp-val">0</strong></span>
            <span id="xp-progress-percent">0%</span>
          </div>
          <div class="xp-track">
            <div class="xp-fill" id="player-xp-fill" style="width: 5%;"></div>
          </div>
        </div>

        <div class="badge-pill badge-streak" title="Racha de estudio">
          <span>🔥</span>
          <span id="player-streak">1 Días</span>
        </div>

        <button class="cert-btn" id="open-cert-btn">
          📜 Certificado
        </button>
      </div>
    </header>

    <!-- CUERPO PRINCIPAL -->
    <div class="main-body">
      
      <!-- SIDEBAR -->
      <aside class="sidebar">
        <div class="sidebar-title">
          <h2>🗺️ Hoja de Ruta (32 Clases)</h2>
          <span class="progress-tag" id="total-progress-pill">0% Hecho</span>
        </div>
        <div class="curriculum-tree" id="class-tree-container">
          <!-- Inyectado por JS -->
        </div>
      </aside>

      <!-- ESTUDIO CENTRAL -->
      <main class="studio">
        
        <!-- HERO CARD -->
        <div class="hero-card">
          <div class="hero-tags">
            <span class="tag-course" id="lesson-course-name">Curso 1: Fundamentos Básicos</span>
            <span class="tag-boss" id="lesson-boss-badge" style="display: none;">⚔️ Boss Battle</span>
          </div>
          <h2 class="hero-title" id="lesson-title">Cargando Clase...</h2>
          <div class="metaphor-box">
            <span>🌟</span>
            <span id="lesson-metaphor">Metáfora: «El Megáfono, las Cajas y el Semáforo»</span>
          </div>
        </div>

        <!-- PESTAÑAS PASO A PASO -->
        <nav class="step-tabs">
          <button class="tab-btn active" data-step="1">
            <span class="tab-badge">1</span> 💡 Concepto & Metáfora
          </button>
          <button class="tab-btn" data-step="2">
            <span class="tab-badge">2</span> 💻 Demostración
          </button>
          <button class="tab-btn" data-step="3">
            <span class="tab-badge">3</span> 🔬 Arenero & Memoria
          </button>
          <button class="tab-btn" data-step="4">
            <span class="tab-badge">4</span> 🏋️ Reto Evaluado
          </button>
        </nav>

        <!-- PASO 1: CONCEPTO -->
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
            </div>

            <div class="glass-card">
              <h3>🗺️ Arquitectura Visual de Flujo</h3>
              <div class="mermaid-canvas" id="mermaid-render-box"></div>
            </div>
          </div>
        </div>

        <!-- PASO 2: DEMOSTRACIÓN -->
        <div class="tab-pane" id="pane-step-2">
          <div class="glass-card">
            <div class="flex-between">
              <h3>💻 Código de Demostración Comentado</h3>
              <button class="btn btn-primary" id="run-demo-btn">▶️ Ejecutar Demo</button>
            </div>
            <textarea class="code-editor" id="demo-code-area" readonly spellcheck="false"></textarea>
            <div class="terminal-output" id="demo-terminal">&gt; Presiona 'Ejecutar Demo' para compilar.</div>
          </div>
        </div>

        <!-- PASO 3: ARENERO & MEMORIA -->
        <div class="tab-pane" id="pane-step-3">
          <div class="two-col-grid">
            <div class="glass-card">
              <div class="flex-between">
                <h3>🔬 Arenero de Experimentación</h3>
                <button class="btn btn-primary" id="run-sandbox-btn">⚡ Inspeccionar Memoria</button>
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
                  <p style="font-size: 0.85rem; color: #94a3b8; margin-top: 0.2rem;" id="challenge-prompt-text">Crea la función indicada.</p>
                </div>
                <button class="btn btn-success" id="eval-challenge-btn">🚀 Evaluar Reto (+150 XP)</button>
              </div>
              <textarea class="code-editor" id="challenge-code-area" spellcheck="false"></textarea>
              <div id="challenge-results-box" style="margin-top: 0.5rem;">
                <div style="color: #64748b; font-size: 0.85rem; font-style: italic;">Escribe tu solución y pulsa 'Evaluar Reto'.</div>
              </div>
            </div>

            <div class="glass-card">
              <h3>💡 Pistas Socráticas del Mentor</h3>
              <div id="hints-accordion" style="display: flex; flex-direction: column; gap: 0.4rem;"></div>
              <div style="background: rgba(2, 132, 199, 0.1); border: 1px solid #0284c7; padding: 0.75rem; border-radius: 8px; margin-top: auto;">
                <strong style="color: #38bdf8;">🏆 Recompensa:</strong>
                <p style="font-size: 0.82rem; color: #cbd5e1; margin-top: 0.2rem;">+150 XP &bull; Sello de acreditación &bull; Desbloqueo de siguiente clase.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- FOOTER DE NAVEGACIÓN -->
        <footer class="studio-footer">
          <button class="btn btn-secondary" id="prev-class-btn">⬅️ Clase Anterior</button>
          <button class="btn btn-primary" id="next-class-btn">Siguiente Clase ➡️</button>
        </footer>

      </main>
    </div>

    <!-- MODAL DE CERTIFICADO -->
    <div class="modal-backdrop hidden" id="cert-modal">
      <div class="modal-panel">
        <div class="modal-header">
          <h2>📜 Certificación Oficial de Acreditación</h2>
          <button style="background:none; border:none; color:#fff; font-size:1.5rem; cursor:pointer;" id="close-cert-btn">&times;</button>
        </div>
        <div style="display:flex; gap:0.5rem; align-items:center;">
          <label style="font-size:0.85rem; color:#94a3b8;">Nombre en el Diploma:</label>
          <input type="text" id="student-name-input" style="flex:1; padding:0.4rem 0.6rem; background:#060911; border:1px solid #334155; color:#fff; border-radius:6px;" value="Alejandro Martínez">
          <button class="btn btn-primary" id="refresh-cert-btn">Actualizar Vista</button>
        </div>
        <div class="cert-view" id="cert-preview-frame"></div>
        <div style="display:flex; justify-content:flex-end; gap:0.6rem;">
          <button class="btn btn-secondary" id="copy-badge-btn">📋 Copiar Badge GitHub</button>
          <button class="btn btn-success" id="download-cert-btn">📥 Descargar PDF Oficial</button>
        </div>
      </div>
    </div>

  </div>

  <!-- SCRIPT JS EMBEBIDO REACTIVO -->
  <script>
    document.addEventListener("DOMContentLoaded", () => {
      const state = {
        currentCourse: 1,
        currentClass: 1,
        profile: null,
        curriculum: [],
        classContent: null,
        currentStep: 1
      };

      if (window.mermaid) {
        mermaid.initialize({ startOnLoad: false, theme: "dark", securityLevel: "loose" });
      }

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
        tabBtns: document.querySelectorAll(".tab-btn"),
        tabPanes: document.querySelectorAll(".tab-pane"),
        theoryText: document.getElementById("theory-text"),
        mermaidBox: document.getElementById("mermaid-render-box"),
        demoCode: document.getElementById("demo-code-area"),
        demoTerm: document.getElementById("demo-terminal"),
        runDemoBtn: document.getElementById("run-demo-btn"),
        sandboxCode: document.getElementById("sandbox-code-area"),
        sandboxTerm: document.getElementById("sandbox-terminal"),
        runSandboxBtn: document.getElementById("run-sandbox-btn"),
        memoryCanvas: document.getElementById("memory-canvas"),
        challengePrompt: document.getElementById("challenge-prompt-text"),
        challengeCode: document.getElementById("challenge-code-area"),
        challengeResults: document.getElementById("challenge-results-box"),
        evalChallengeBtn: document.getElementById("eval-challenge-btn"),
        hintsAccordion: document.getElementById("hints-accordion"),
        prevBtn: document.getElementById("prev-class-btn"),
        nextBtn: document.getElementById("next-class-btn"),
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

      function renderTree() {
        dom.classTree.innerHTML = "";
        const courses = [
          { id: 1, name: "Curso 1: Fundamentos Básicos" },
          { id: 2, name: "Curso 2: Algoritmos y Estructuras" },
          { id: 3, name: "Curso 3: Agentes de IA" },
          { id: 4, name: "Curso 4: Proyecto Final Integrador" }
        ];

        courses.forEach(c => {
          const grp = document.createElement("div");
          grp.className = "course-section";
          grp.innerHTML = `<div class="course-header">${c.name}</div>`;

          const courseClasses = state.curriculum.filter(cls => cls.course_num === c.id);
          courseClasses.forEach(cls => {
            const item = document.createElement("div");
            const isActive = (cls.course_num === state.currentCourse && cls.class_num === state.currentClass);
            item.className = `class-item ${isActive ? 'active' : ''} ${cls.completed ? 'completed' : ''}`;
            const boss = cls.boss_battle ? "⚔️ " : "";
            item.innerHTML = `
              <span>${boss}S${cls.class_num.toString().padStart(2, '0')}: ${cls.title.split(':')[1] || cls.title}</span>
              <span class="item-status-icon">${cls.completed ? '✓' : '○'}</span>
            `;
            item.addEventListener("click", () => loadClass(cls.course_num, cls.class_num));
            grp.appendChild(item);
          });
          dom.classTree.appendChild(grp);
        });
      }

      async function loadClass(courseNum, classNum) {
        state.currentCourse = courseNum;
        state.currentClass = classNum;
        try {
          const res = await fetch(`/api/class/${courseNum}/${classNum}`);
          const data = await res.json();
          state.classContent = data;
          renderClass(data);
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
        dom.demoTerm.innerHTML = "&gt; Presiona 'Ejecutar Demo' para compilar.";

        dom.sandboxCode.value = data.playground_code;
        dom.sandboxTerm.innerHTML = "&gt; Modifica variables y pulsa 'Inspeccionar Memoria'.";
        dom.memoryCanvas.innerHTML = `<div class="empty-state">Ejecuta código para visualizar las variables en la memoria RAM.</div>`;

        dom.challengePrompt.textContent = data.challenge_prompt;
        dom.challengeCode.value = data.challenge_starter;
        dom.challengeResults.innerHTML = `<div style="color: #64748b; font-size: 0.85rem; font-style: italic;">Escribe tu solución y pulsa 'Evaluar Reto'.</div>`;

        dom.hintsAccordion.innerHTML = "";
        data.socratic_hints.forEach(h => {
          const d = document.createElement("div");
          d.style.cssText = "background: #1e293b; padding: 0.5rem 0.75rem; border-radius: 6px; font-size: 0.82rem; color: #cbd5e1;";
          d.textContent = h;
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

      function switchStep(num) {
        state.currentStep = num;
        dom.tabBtns.forEach(b => b.classList.toggle("active", parseInt(b.dataset.step) === num));
        dom.tabPanes.forEach(p => p.classList.toggle("active", p.id === `pane-step-${num}`));
      }

      function setupEvents() {
        dom.tabBtns.forEach(b => b.addEventListener("click", () => switchStep(parseInt(b.dataset.step))));

        dom.runDemoBtn.addEventListener("click", async () => {
          dom.demoTerm.innerHTML = "&gt; Ejecutando...";
          const res = await fetch("/api/run-code", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: dom.demoCode.value })
          });
          const data = await res.json();
          dom.demoTerm.innerHTML = `&gt; ${data.stdout || data.stderr || 'Ejecutado sin salida.'}`;
        });

        dom.runSandboxBtn.addEventListener("click", async () => {
          dom.sandboxTerm.innerHTML = "&gt; Analizando estado del Heap...";
          const res = await fetch("/api/run-code", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: dom.sandboxCode.value })
          });
          const data = await res.json();
          dom.sandboxTerm.innerHTML = `&gt; ${data.stdout || data.stderr || 'Ejecutado.'}`;
          renderMemory(data.memory_variables);
        });

        dom.evalChallengeBtn.addEventListener("click", async () => {
          dom.challengeResults.innerHTML = "<div style='color:#38bdf8;'>🧪 Ejecutando suite de pruebas automatizadas...</div>";
          const res = await fetch("/api/evaluate-challenge", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              course_num: state.currentCourse,
              class_num: state.currentClass,
              code: dom.challengeCode.value
            })
          });
          const data = await res.json();
          if (data.evaluation.passed) {
            if (window.confetti) confetti({ particleCount: 120, spread: 80, origin: { y: 0.6 } });
            dom.challengeResults.innerHTML = `
              <div style="background: rgba(5,150,105,0.2); border: 1px solid #059669; color: #6ee7b7; padding: 0.75rem; border-radius: 8px;">
                🎉 <strong>¡RETO SUPERADO CON ÉXITO! (+150 XP)</strong><br>
                Tu solución ha superado todas las aserciones de Pytest.
              </div>
            `;
            await fetchProfile();
            await fetchCurriculum();
          } else {
            dom.challengeResults.innerHTML = `
              <div style="background: rgba(220,38,38,0.2); border: 1px solid #dc2626; color: #fca5a5; padding: 0.75rem; border-radius: 8px;">
                ⚠️ <strong>La solución aún no cumple todas las condiciones:</strong><br>
                <p style="margin-top:0.3rem; font-size:0.85rem;">${data.evaluation.socratic_hint}</p>
              </div>
            `;
          }
        });

        dom.prevBtn.addEventListener("click", () => {
          if (state.currentClass > 1) loadClass(state.currentCourse, state.currentClass - 1);
          else if (state.currentCourse > 1) loadClass(state.currentCourse - 1, 8);
        });

        dom.nextBtn.addEventListener("click", () => {
          if (state.currentClass < 8) loadClass(state.currentCourse, state.currentClass + 1);
          else if (state.currentCourse < 4) loadClass(state.currentCourse + 1, 1);
        });

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
            <div style="display:flex; gap:0.5rem; align-items:center;">
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
