#!/usr/bin/env python3
"""
Embedded UI Frontend (Wisrovi Academy - Ultimate AI Tutor & RPG Studio v12.0 Master Diamond Edition).
100% Autocontenido e incluye soporte activo y completo para los 4 cursos y las 32 clases del programa,
Micro-Quizzes con recompensas de XP, Patrones Pythonic vs Antipatrones, Formateador de Código PEP 8,
Debugger visual de trazas, Inspector Dual Stack/Heap RAM 3.0, Paleta de Comandos y Certificación Oficial.
"""

def get_embedded_html() -> str:
    return """<!DOCTYPE html>
<html lang="es" data-theme="midnight">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wisrovi Academy &bull; Virtual AI Tutor &amp; RPG Studio</title>
  
  <!-- Google Fonts: Outfit, Inter y JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Outfit:wght@500;600;700;800;900&family=JetBrains+Mono:ital,wght@0,400;0,500;0,700;0,800;1,400&display=swap" rel="stylesheet">
  
  <!-- CDN Libraries: Mermaid & Canvas Confetti -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>

  <style>
    /* ==============================================================================
       WISROVI DESIGN SYSTEM v12.0 (DIAMOND EDITION)
       ============================================================================== */
    :root {
      --font-ui: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-display: 'Outfit', sans-serif;
      --font-code: 'JetBrains Mono', 'Fira Code', monospace;
      --radius-xs: 4px;
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 18px;
      --radius-xl: 24px;
      --transition-fast: 0.18s cubic-bezier(0.4, 0, 0.2, 1);
      --transition-bounce: 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    /* THEME: MIDNIGHT CYBER (Default) */
    html[data-theme="midnight"] {
      --bg-canvas: #02050e;
      --bg-surface: #070d1e;
      --bg-card: rgba(11, 19, 41, 0.94);
      --bg-card-hover: #142247;
      --bg-editor: #020612;
      --border-glass: rgba(56, 189, 248, 0.24);
      --border-accent: #0284c7;
      --border-glow: rgba(2, 132, 199, 0.55);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --primary: #0284c7;
      --primary-hover: #0369a1;
      --primary-glow: rgba(2, 132, 199, 0.45);
      --success: #10b981;
      --success-hover: #059669;
      --success-glow: rgba(16, 185, 129, 0.45);
      --accent-gold: #f59e0b;
      --accent-purple: #8b5cf6;
      --danger: #ef4444;
      --shadow-card: 0 18px 40px -10px rgba(0, 0, 0, 0.85);
      --bg-radial: radial-gradient(circle at 10% 8%, rgba(2, 132, 199, 0.22) 0%, transparent 45%),
                   radial-gradient(circle at 90% 10%, rgba(139, 92, 246, 0.2) 0%, transparent 50%),
                   radial-gradient(circle at 50% 92%, rgba(16, 185, 129, 0.15) 0%, transparent 55%);
    }

    /* THEME: OBSIDIAN OLED */
    html[data-theme="obsidian"] {
      --bg-canvas: #000000;
      --bg-surface: #09090b;
      --bg-card: rgba(18, 18, 22, 0.96);
      --bg-card-hover: #22222a;
      --bg-editor: #050507;
      --border-glass: rgba(255, 255, 255, 0.14);
      --border-accent: #e2e8f0;
      --border-glow: rgba(255, 255, 255, 0.25);
      --text-main: #ffffff;
      --text-muted: #a1a1aa;
      --text-dim: #71717a;
      --primary: #3b82f6;
      --primary-hover: #2563eb;
      --primary-glow: rgba(59, 130, 246, 0.4);
      --success: #22c55e;
      --success-hover: #16a34a;
      --success-glow: rgba(34, 197, 94, 0.4);
      --accent-gold: #eab308;
      --accent-purple: #a855f7;
      --danger: #f43f5e;
      --shadow-card: 0 18px 40px -10px rgba(0, 0, 0, 0.95);
      --bg-radial: radial-gradient(circle at 50% 0%, rgba(59, 130, 246, 0.12) 0%, transparent 60%);
    }

    /* THEME: EMERALD MATRIX */
    html[data-theme="emerald"] {
      --bg-canvas: #02110c;
      --bg-surface: #041d14;
      --bg-card: rgba(6, 32, 23, 0.94);
      --bg-card-hover: #0c4331;
      --bg-editor: #010a07;
      --border-glass: rgba(52, 211, 153, 0.28);
      --border-accent: #10b981;
      --border-glow: rgba(16, 185, 129, 0.55);
      --text-main: #ecfdf5;
      --text-muted: #a7f3d0;
      --text-dim: #6ee7b7;
      --primary: #059669;
      --primary-hover: #047857;
      --primary-glow: rgba(5, 150, 105, 0.5);
      --success: #10b981;
      --success-hover: #059669;
      --success-glow: rgba(16, 185, 129, 0.5);
      --accent-gold: #fbbf24;
      --accent-purple: #34d399;
      --danger: #f87171;
      --shadow-card: 0 18px 40px -10px rgba(0, 0, 0, 0.9);
      --bg-radial: radial-gradient(circle at 15% 15%, rgba(16, 185, 129, 0.22) 0%, transparent 50%),
                   radial-gradient(circle at 85% 85%, rgba(6, 95, 70, 0.25) 0%, transparent 60%);
    }

    /* THEME: SOLAR GOLD */
    html[data-theme="solar"] {
      --bg-canvas: #120b02;
      --bg-surface: #201305;
      --bg-card: rgba(38, 24, 8, 0.94);
      --bg-card-hover: #4d310e;
      --bg-editor: #0c0701;
      --border-glass: rgba(245, 158, 11, 0.28);
      --border-accent: #d97706;
      --border-glow: rgba(245, 158, 11, 0.55);
      --text-main: #fffbeb;
      --text-muted: #fde68a;
      --text-dim: #f59e0b;
      --primary: #d97706;
      --primary-hover: #b45309;
      --primary-glow: rgba(217, 119, 6, 0.5);
      --success: #10b981;
      --success-hover: #059669;
      --success-glow: rgba(16, 185, 129, 0.5);
      --accent-gold: #f59e0b;
      --accent-purple: #fb923c;
      --danger: #ef4444;
      --shadow-card: 0 18px 40px -10px rgba(0, 0, 0, 0.9);
      --bg-radial: radial-gradient(circle at 20% 10%, rgba(245, 158, 11, 0.22) 0%, transparent 50%),
                   radial-gradient(circle at 80% 90%, rgba(180, 83, 9, 0.25) 0%, transparent 60%);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    body {
      font-family: var(--font-ui);
      background-color: var(--bg-canvas);
      background-image: var(--bg-radial);
      background-attachment: fixed;
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      transition: background-color 0.3s ease, color 0.3s ease;
    }

    .app-wrapper {
      display: flex;
      flex-direction: column;
      min-height: 100vh;
    }

    /* --------------------------------------------------------------------------
       1. HEADER GLOBAL STICKY CON CONTROLES AVANZADOS
       -------------------------------------------------------------------------- */
    .app-header {
      background: rgba(5, 10, 22, 0.94);
      backdrop-filter: blur(24px);
      border-bottom: 1px solid var(--border-glass);
      padding: 0.75rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 4px 30px rgba(0, 0, 0, 0.75);
    }

    .brand-cluster {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .brand-logo-badge {
      width: 44px;
      height: 44px;
      background: linear-gradient(135deg, var(--primary), var(--accent-purple));
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.6rem;
      box-shadow: 0 0 20px var(--primary-glow);
      transition: transform var(--transition-bounce);
      cursor: pointer;
    }

    .brand-logo-badge:hover {
      transform: rotate(10deg) scale(1.1);
    }

    .brand-text h1 {
      font-family: var(--font-display);
      font-size: 1.35rem;
      font-weight: 900;
      letter-spacing: -0.4px;
      background: linear-gradient(90deg, #38bdf8, #818cf8, #34d399);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .brand-text p {
      font-size: 0.72rem;
      color: var(--text-muted);
      font-weight: 600;
    }

    .engine-status-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.35);
      padding: 0.22rem 0.65rem;
      border-radius: 999px;
      font-size: 0.72rem;
      font-weight: 800;
      color: #34d399;
    }

    .pulse-dot {
      width: 8px;
      height: 8px;
      background: #10b981;
      border-radius: 50%;
      box-shadow: 0 0 10px #10b981;
      animation: pulseGreen 2s infinite;
    }

    @keyframes pulseGreen {
      0% { transform: scale(0.9); opacity: 0.7; }
      50% { transform: scale(1.3); opacity: 1; }
      100% { transform: scale(0.9); opacity: 0.7; }
    }

    .gamification-controls {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .command-search-btn {
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid var(--border-glass);
      color: var(--text-muted);
      padding: 0.45rem 0.85rem;
      border-radius: var(--radius-sm);
      font-size: 0.78rem;
      display: flex;
      align-items: center;
      gap: 0.55rem;
      cursor: pointer;
      transition: all var(--transition-fast);
    }

    .command-search-btn:hover {
      background: #1e293b;
      color: #fff;
      border-color: var(--border-accent);
    }

    .theme-select {
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid var(--border-glass);
      color: var(--text-main);
      padding: 0.4rem 0.65rem;
      border-radius: var(--radius-sm);
      font-size: 0.76rem;
      font-weight: 700;
      cursor: pointer;
      outline: none;
    }

    .user-avatar-btn {
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid var(--border-glass);
      width: 40px;
      height: 40px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
      cursor: pointer;
      transition: transform var(--transition-bounce), border-color var(--transition-fast);
      box-shadow: var(--shadow-card);
    }

    .user-avatar-btn:hover {
      border-color: var(--border-accent);
      transform: scale(1.12);
    }

    .badge-pill {
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid var(--border-glass);
      padding: 0.4rem 0.85rem;
      border-radius: 999px;
      font-size: 0.78rem;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 0.45rem;
      box-shadow: var(--shadow-card);
    }

    .badge-level {
      border-color: rgba(56, 189, 248, 0.4);
      color: #38bdf8;
      background: rgba(2, 132, 199, 0.12);
    }

    .badge-streak {
      border-color: rgba(249, 115, 22, 0.4);
      color: #fb923c;
      background: rgba(249, 115, 22, 0.12);
    }

    .badge-timer {
      border-color: rgba(52, 211, 153, 0.4);
      color: #34d399;
      background: rgba(16, 185, 129, 0.12);
      font-family: var(--font-code);
    }

    .xp-meter-box {
      display: flex;
      flex-direction: column;
      gap: 0.2rem;
      width: 135px;
    }

    .xp-text-row {
      display: flex;
      justify-content: space-between;
      font-size: 0.7rem;
      color: var(--text-muted);
      font-weight: 700;
    }

    .xp-track {
      height: 6px;
      background: #1e293b;
      border-radius: 999px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.08);
      position: relative;
    }

    .xp-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--primary), #38bdf8, #34d399);
      border-radius: 999px;
      transition: width 0.6s cubic-bezier(0.34, 1.56, 0.64, 1);
    }

    .header-btn {
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid var(--border-glass);
      color: #cbd5e1;
      padding: 0.42rem 0.8rem;
      border-radius: var(--radius-sm);
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: all var(--transition-fast);
    }

    .header-btn:hover {
      background: #1e293b;
      color: #fff;
      border-color: var(--border-accent);
    }

    .cert-btn {
      background: linear-gradient(135deg, #78350f, #d97706);
      border: 1px solid #f59e0b;
      color: #fff;
      padding: 0.45rem 1.05rem;
      border-radius: var(--radius-md);
      font-size: 0.8rem;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.45rem;
      transition: all var(--transition-fast);
      box-shadow: 0 4px 15px rgba(217, 119, 6, 0.35);
    }

    .cert-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(217, 119, 6, 0.55);
    }

    /* --------------------------------------------------------------------------
       2. BARRA DE SELECCIÓN DE CURSO (COURSE TABS 1..4)
       -------------------------------------------------------------------------- */
    .course-tabs-bar {
      background: rgba(4, 8, 20, 0.95);
      border-bottom: 1px solid var(--border-glass);
      padding: 0.4rem 2rem;
      display: flex;
      gap: 0.6rem;
      align-items: center;
      overflow-x: auto;
    }

    .course-tab-btn {
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid var(--border-glass);
      color: #94a3b8;
      padding: 0.45rem 1rem;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: all var(--transition-fast);
      white-space: nowrap;
    }

    .course-tab-btn:hover {
      background: #1e293b;
      color: #fff;
    }

    .course-tab-btn.active {
      background: linear-gradient(135deg, rgba(2, 132, 199, 0.35), rgba(2, 132, 199, 0.15));
      border-color: var(--border-accent);
      color: #fff;
      box-shadow: 0 0 15px var(--primary-glow);
    }

    /* BREADCRUMBS */
    .breadcrumbs-bar {
      background: rgba(6, 11, 24, 0.85);
      border-bottom: 1px solid var(--border-glass);
      padding: 0.45rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.78rem;
      color: var(--text-muted);
    }

    .breadcrumbs-list {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .toggle-sidebar-btn {
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid var(--border-glass);
      color: var(--text-muted);
      padding: 0.22rem 0.5rem;
      border-radius: var(--radius-xs);
      cursor: pointer;
      font-size: 0.76rem;
      margin-right: 0.3rem;
      transition: all var(--transition-fast);
    }

    .toggle-sidebar-btn:hover {
      color: #fff;
      background: #1e293b;
    }

    .breadcrumb-item {
      color: #7dd3fc;
      font-weight: 600;
    }

    .breadcrumb-sep {
      color: var(--text-dim);
    }

    /* --------------------------------------------------------------------------
       3. CONTENEDOR PRINCIPAL (SIDEBAR + ESTUDIO)
       -------------------------------------------------------------------------- */
    .main-workspace {
      display: flex;
      flex: 1;
      max-width: 1780px;
      margin: 0 auto;
      width: 100%;
      position: relative;
    }

    /* SIDEBAR CURRICULAR */
    .sidebar {
      width: 350px;
      background: rgba(6, 11, 24, 0.88);
      backdrop-filter: blur(16px);
      border-right: 1px solid var(--border-glass);
      display: flex;
      flex-direction: column;
      transition: margin-left 0.3s cubic-bezier(0.4, 0, 0.2, 1), width 0.3s ease;
      z-index: 50;
    }

    .sidebar.collapsed {
      margin-left: -350px;
    }

    .sidebar-header {
      padding: 1.1rem 1.25rem;
      border-bottom: 1px solid var(--border-glass);
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .sidebar-title-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .sidebar-title-row h2 {
      font-family: var(--font-display);
      font-size: 0.92rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      color: var(--text-muted);
    }

    .progress-tag {
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid #10b981;
      color: #34d399;
      padding: 0.2rem 0.65rem;
      border-radius: 999px;
      font-size: 0.74rem;
      font-weight: 800;
      box-shadow: 0 0 10px rgba(16, 185, 129, 0.2);
    }

    .sidebar-search-box {
      position: relative;
    }

    .sidebar-search-input {
      width: 100%;
      padding: 0.4rem 0.75rem;
      background: #060a14;
      border: 1px solid var(--border-glass);
      border-radius: var(--radius-sm);
      color: var(--text-main);
      font-size: 0.78rem;
      outline: none;
      transition: border-color var(--transition-fast);
    }

    .sidebar-search-input:focus {
      border-color: var(--border-accent);
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
      color: #7dd3fc;
      padding: 0.4rem 0.6rem;
      margin-bottom: 0.35rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(56, 189, 248, 0.15);
    }

    .class-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.62rem 0.85rem;
      border-radius: var(--radius-md);
      font-size: 0.82rem;
      font-weight: 600;
      color: #94a3b8;
      cursor: pointer;
      margin-bottom: 0.3rem;
      border: 1px solid transparent;
      transition: all var(--transition-fast);
    }

    .class-item:hover:not(.locked) {
      background: rgba(30, 41, 59, 0.85);
      color: #fff;
      transform: translateX(3px);
    }

    .class-item.active {
      background: linear-gradient(90deg, rgba(2, 132, 199, 0.35), rgba(2, 132, 199, 0.1));
      border-color: var(--border-accent);
      color: #fff;
      font-weight: 700;
      box-shadow: 0 0 16px rgba(2, 132, 199, 0.25);
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

    /* ESTUDIO CENTRAL */
    .studio {
      flex: 1;
      display: flex;
      flex-direction: column;
      padding: 1.5rem 2.5rem 3rem 2.5rem;
      gap: 1.3rem;
      overflow-x: hidden;
    }

    /* HERO CARD DE LA CLASE */
    .hero-card {
      background: linear-gradient(135deg, rgba(12, 19, 38, 0.95) 0%, rgba(26, 36, 62, 0.75) 100%);
      border: 1px solid var(--border-glass);
      border-radius: var(--radius-lg);
      padding: 1.35rem 1.75rem;
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

    .tag-mode {
      font-size: 0.72rem;
      font-weight: 800;
      padding: 0.18rem 0.65rem;
      border-radius: 6px;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
    }

    .tag-review {
      background: rgba(16, 185, 129, 0.22);
      border: 1px solid #10b981;
      color: #34d399;
      box-shadow: 0 0 12px rgba(16, 185, 129, 0.3);
    }

    .tag-active {
      background: rgba(2, 132, 199, 0.22);
      border: 1px solid #0284c7;
      color: #38bdf8;
      box-shadow: 0 0 12px rgba(2, 132, 199, 0.3);
    }

    .tag-boss {
      background: linear-gradient(90deg, #991b1b, #dc2626);
      color: #fff;
      font-size: 0.72rem;
      font-weight: 900;
      padding: 0.18rem 0.6rem;
      border-radius: 6px;
      box-shadow: 0 0 14px rgba(220, 38, 38, 0.5);
    }

    .hero-title {
      font-family: var(--font-display);
      font-size: 1.55rem;
      font-weight: 900;
      color: var(--text-main);
      letter-spacing: -0.4px;
    }

    .metaphor-box {
      background: rgba(2, 132, 199, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.35);
      border-radius: var(--radius-md);
      padding: 0.65rem 1.15rem;
      font-size: 0.88rem;
      color: #7dd3fc;
      font-style: italic;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.85rem;
      flex-wrap: wrap;
    }

    .voice-controls-group {
      display: flex;
      align-items: center;
      gap: 0.45rem;
    }

    .listen-btn {
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid #38bdf8;
      color: #38bdf8;
      padding: 0.28rem 0.7rem;
      border-radius: var(--radius-sm);
      font-size: 0.74rem;
      font-weight: 700;
      cursor: pointer;
      transition: all var(--transition-fast);
    }

    .listen-btn:hover {
      background: #0284c7;
      color: #fff;
    }

    .speed-select {
      background: #0f172a;
      border: 1px solid #334155;
      color: #94a3b8;
      padding: 0.22rem 0.45rem;
      border-radius: 4px;
      font-size: 0.7rem;
      font-weight: 700;
    }

    /* STEPPER GATES */
    .stepper-container {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 0.75rem;
      background: rgba(10, 16, 30, 0.75);
      padding: 0.6rem;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-glass);
    }

    .step-gate-pill {
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-sm);
      padding: 0.65rem 0.85rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: all var(--transition-fast);
    }

    .step-gate-pill:hover {
      background: rgba(30, 41, 59, 0.8);
    }

    .step-gate-pill.active {
      background: linear-gradient(135deg, rgba(2, 132, 199, 0.35), rgba(2, 132, 199, 0.15));
      border-color: var(--border-accent);
      box-shadow: 0 0 15px rgba(2, 132, 199, 0.3);
    }

    .step-gate-pill.done {
      border-color: rgba(16, 185, 129, 0.6);
      background: rgba(16, 185, 129, 0.12);
    }

    .step-gate-info {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.84rem;
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
      background: rgba(16, 185, 129, 0.3);
      color: #34d399;
    }

    /* PANELES DE CONTENIDO */
    .tab-pane {
      display: none;
      flex-direction: column;
      gap: 1.2rem;
      animation: fadeIn 0.28s ease;
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
      gap: 1.35rem;
    }

    .glass-card {
      background: var(--bg-card);
      backdrop-filter: blur(12px);
      border: 1px solid var(--border-glass);
      border-radius: var(--radius-lg);
      padding: 1.35rem;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      gap: 0.95rem;
    }

    .glass-card h3 {
      font-family: var(--font-display);
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .theory-desc {
      font-size: 0.92rem;
      line-height: 1.68;
      color: #cbd5e1;
    }

    .mentor-box {
      background: rgba(139, 92, 246, 0.12);
      border-left: 4px solid #8b5cf6;
      padding: 0.9rem 1.15rem;
      border-radius: 0 10px 10px 0;
      display: flex;
      gap: 0.85rem;
      font-size: 0.86rem;
      color: #ddd6fe;
      align-items: center;
    }

    .mentor-avatar {
      font-size: 1.7rem;
    }

    .mermaid-canvas {
      background: #030610;
      border: 1px solid var(--border-glass);
      border-radius: var(--radius-md);
      padding: 1.2rem;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 290px;
      overflow: auto;
    }

    /* MICRO-QUIZ CARD */
    .quiz-card {
      background: rgba(6, 15, 33, 0.95);
      border: 1px solid #38bdf8;
      border-radius: var(--radius-md);
      padding: 1.1rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .quiz-question-title {
      font-size: 0.9rem;
      font-weight: 800;
      color: #38bdf8;
    }

    .quiz-options-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.5rem;
    }

    .quiz-opt-btn {
      background: #0b1528;
      border: 1px solid #1e293b;
      color: #cbd5e1;
      padding: 0.55rem 0.85rem;
      border-radius: var(--radius-sm);
      font-size: 0.82rem;
      cursor: pointer;
      text-align: left;
      transition: all var(--transition-fast);
    }

    .quiz-opt-btn:hover {
      background: #1e293b;
      color: #fff;
      border-color: #38bdf8;
    }

    .quiz-opt-btn.correct {
      background: rgba(16, 185, 129, 0.25) !important;
      border-color: #10b981 !important;
      color: #6ee7b7 !important;
      font-weight: 800;
    }

    .quiz-opt-btn.wrong {
      background: rgba(239, 68, 68, 0.25) !important;
      border-color: #ef4444 !important;
      color: #fca5a5 !important;
    }

    /* PYTHONIC VS ANTIPATTERN CARD */
    .pythonic-diff-card {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.75rem;
      background: #020612;
      border: 1px solid var(--border-glass);
      border-radius: var(--radius-md);
      padding: 0.85rem;
    }

    .diff-box {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }

    .diff-tag-bad {
      color: #f87171;
      font-size: 0.74rem;
      font-weight: 800;
      text-transform: uppercase;
    }

    .diff-tag-good {
      color: #34d399;
      font-size: 0.74rem;
      font-weight: 800;
      text-transform: uppercase;
    }

    .diff-code-pre {
      background: #040817;
      border: 1px solid rgba(255, 255, 255, 0.06);
      padding: 0.6rem;
      border-radius: 6px;
      font-family: var(--font-code);
      font-size: 0.78rem;
      color: #cbd5e1;
      line-height: 1.45;
    }

    /* --------------------------------------------------------------------------
       4. TOOLBAR Y EDITOR DE CÓDIGO CON LÍNEAS
       -------------------------------------------------------------------------- */
    .editor-wrapper {
      display: flex;
      flex-direction: column;
      border: 1px solid var(--border-glass);
      border-radius: var(--radius-md);
      overflow: hidden;
      background: var(--bg-editor);
    }

    .editor-toolbar {
      background: rgba(15, 23, 42, 0.95);
      border-bottom: 1px solid var(--border-glass);
      padding: 0.45rem 0.85rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.76rem;
      color: var(--text-muted);
    }

    .editor-actions {
      display: flex;
      gap: 0.4rem;
      align-items: center;
    }

    .snippet-select {
      background: #1e293b;
      border: 1px solid #334155;
      color: #cbd5e1;
      padding: 0.22rem 0.5rem;
      border-radius: 4px;
      font-size: 0.72rem;
      font-weight: 700;
    }

    .tool-btn {
      background: #1e293b;
      border: 1px solid #334155;
      color: #cbd5e1;
      padding: 0.22rem 0.55rem;
      border-radius: 4px;
      font-size: 0.72rem;
      font-weight: 700;
      cursor: pointer;
      transition: all var(--transition-fast);
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
    }

    .tool-btn:hover {
      background: #334155;
      color: #fff;
    }

    .tool-btn.primary-tool {
      background: var(--primary);
      border-color: #38bdf8;
      color: #fff;
    }

    .editor-body-with-lines {
      display: flex;
      position: relative;
      background: var(--bg-editor);
    }

    .line-numbers-gutter {
      width: 42px;
      padding: 0.95rem 0.4rem;
      text-align: right;
      font-family: var(--font-code);
      font-size: 0.86rem;
      color: #475569;
      user-select: none;
      background: rgba(2, 6, 18, 0.95);
      border-right: 1px solid rgba(255, 255, 255, 0.06);
      line-height: 1.55;
      overflow: hidden;
    }

    .code-editor {
      flex: 1;
      height: 240px;
      background: transparent;
      border: none;
      color: #38bdf8;
      font-family: var(--font-code);
      font-size: 0.9rem;
      line-height: 1.55;
      padding: 0.95rem 1rem;
      resize: vertical;
      outline: none;
      tab-size: 4;
      white-space: pre;
      overflow-wrap: normal;
      overflow-x: auto;
    }

    .terminal-output {
      background: #02040a;
      border: 1px solid var(--border-glass);
      border-radius: var(--radius-md);
      padding: 0.85rem 1.1rem;
      font-family: var(--font-code);
      font-size: 0.84rem;
      color: #4ade80;
      min-height: 80px;
      max-height: 200px;
      overflow-y: auto;
      white-space: pre-wrap;
    }

    /* --------------------------------------------------------------------------
       5. VISUALIZADOR DE MEMORIA RAM DUAL (STACK & HEAP 3.0)
       -------------------------------------------------------------------------- */
    .memory-board-dual {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.75rem;
      background: #030610;
      border: 1px solid var(--border-glass);
      border-radius: var(--radius-md);
      padding: 0.85rem;
      min-height: 270px;
      max-height: 330px;
      overflow-y: auto;
    }

    .mem-column {
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .mem-column-header {
      font-size: 0.74rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      color: #7dd3fc;
      padding-bottom: 0.3rem;
      border-bottom: 1px dashed rgba(56, 189, 248, 0.25);
      display: flex;
      justify-content: space-between;
    }

    .empty-state {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100%;
      color: #64748b;
      font-size: 0.86rem;
      font-style: italic;
      grid-column: span 2;
    }

    .mem-card {
      background: rgba(15, 23, 42, 0.95);
      border: 1px solid var(--border-glass);
      border-left: 4px solid var(--border-accent);
      border-radius: var(--radius-sm);
      padding: 0.6rem 0.85rem;
      display: flex;
      flex-direction: column;
      gap: 0.3rem;
      font-size: 0.84rem;
      transition: all var(--transition-fast);
      position: relative;
    }

    .mem-card:hover {
      transform: translateX(3px);
      box-shadow: 0 4px 15px rgba(2, 132, 199, 0.25);
    }

    .mem-card.heap-card {
      border-left-color: #8b5cf6;
    }

    .mem-top-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .mem-name {
      font-weight: 800;
      color: #38bdf8;
      font-family: var(--font-code);
    }

    .mem-type {
      color: #94a3b8;
      font-size: 0.76rem;
      font-family: var(--font-code);
    }

    .mem-val-row {
      font-family: var(--font-code);
      font-size: 0.82rem;
      color: #f1f5f9;
      word-break: break-all;
    }

    .mem-meta-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.72rem;
    }

    .mem-bytes-badge {
      background: #1e293b;
      border: 1px solid #334155;
      padding: 0.15rem 0.45rem;
      border-radius: 4px;
      font-size: 0.7rem;
      color: #fbbf24;
      font-weight: 800;
      font-family: var(--font-code);
    }

    .mem-hex-id {
      font-family: var(--font-code);
      font-size: 0.72rem;
      color: #64748b;
    }

    /* BOTONES */
    .btn {
      padding: 0.6rem 1.25rem;
      border-radius: var(--radius-md);
      font-weight: 800;
      font-size: 0.85rem;
      cursor: pointer;
      border: none;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all var(--transition-fast);
    }

    .btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
      transform: none !important;
      box-shadow: none !important;
    }

    .btn-primary {
      background: linear-gradient(135deg, var(--primary), var(--primary-hover));
      color: #fff;
      box-shadow: 0 4px 15px var(--primary-glow);
    }

    .btn-primary:hover:not(:disabled) {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(2, 132, 199, 0.55);
    }

    .btn-success {
      background: linear-gradient(135deg, #10b981, #059669);
      color: #fff;
      box-shadow: 0 4px 15px var(--success-glow);
    }

    .btn-success:hover:not(:disabled) {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(16, 185, 129, 0.55);
    }

    .btn-secondary {
      background: #1e293b;
      color: #cbd5e1;
      border: 1px solid #334155;
    }

    .btn-secondary:hover:not(:disabled) {
      background: #334155;
      color: #fff;
    }

    .flex-between {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    /* FOOTER DE ESTUDIO */
    .studio-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid var(--border-glass);
      padding-top: 1.35rem;
      margin-top: 0.5rem;
    }

    .class-status-summary {
      font-size: 0.85rem;
      color: var(--text-muted);
      font-weight: 700;
    }

    /* --------------------------------------------------------------------------
       6. ASISTENTE FLOTANTE INTERACTIVO (WISROVI AI MENTOR)
       -------------------------------------------------------------------------- */
    .floating-mentor {
      position: fixed;
      bottom: 2rem;
      right: 2.2rem;
      display: flex;
      align-items: flex-end;
      gap: 0.85rem;
      z-index: 150;
    }

    .mentor-speech-bubble {
      background: rgba(15, 23, 42, 0.96);
      border: 1px solid var(--border-accent);
      border-radius: var(--radius-md) var(--radius-md) 0 var(--radius-md);
      padding: 0.8rem 1.1rem;
      max-width: 320px;
      font-size: 0.82rem;
      color: #e2e8f0;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.6);
      line-height: 1.48;
      animation: popIn 0.28s ease;
    }

    @keyframes popIn {
      from { opacity: 0; transform: scale(0.8); }
      to { opacity: 1; transform: scale(1); }
    }

    .floating-avatar-btn {
      width: 50px;
      height: 50px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--primary), var(--accent-purple));
      border: 2px solid #38bdf8;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.7rem;
      cursor: pointer;
      box-shadow: 0 0 25px var(--primary-glow);
      transition: transform var(--transition-bounce);
    }

    .floating-avatar-btn:hover {
      transform: scale(1.15) rotate(5deg);
    }

    /* --------------------------------------------------------------------------
       7. FOOTER INSTITUCIONAL COMPLETO
       -------------------------------------------------------------------------- */
    .app-footer {
      background: rgba(3, 7, 16, 0.98);
      border-top: 1px solid var(--border-glass);
      padding: 2.5rem 2.5rem 1.8rem 2.5rem;
      margin-top: auto;
      display: flex;
      flex-direction: column;
      gap: 1.6rem;
    }

    .footer-grid {
      display: grid;
      grid-template-columns: 2fr 1fr 1fr;
      gap: 2.2rem;
    }

    .footer-brand h4 {
      font-family: var(--font-display);
      font-size: 1.1rem;
      font-weight: 900;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .footer-brand p {
      font-size: 0.84rem;
      color: #94a3b8;
      line-height: 1.6;
      margin-top: 0.5rem;
      max-width: 520px;
    }

    .footer-col h5 {
      font-family: var(--font-display);
      font-size: 0.86rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.6px;
      color: #7dd3fc;
      margin-bottom: 0.8rem;
    }

    .footer-links {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
      font-size: 0.82rem;
    }

    .footer-links a {
      color: #94a3b8;
      text-decoration: none;
      transition: color var(--transition-fast);
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
    }

    .footer-links a:hover {
      color: #38bdf8;
    }

    .footer-bottom {
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding-top: 1.2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.76rem;
      color: #64748b;
    }

    /* --------------------------------------------------------------------------
       8. MODALES
       -------------------------------------------------------------------------- */
    .modal-backdrop {
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(0, 0, 0, 0.88);
      backdrop-filter: blur(12px);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 200;
      padding: 1rem;
    }

    .modal-backdrop.hidden { display: none; }

    .modal-panel {
      background: #0d1629;
      border: 1px solid var(--border-glass);
      border-radius: var(--radius-lg);
      width: 90%;
      max-width: 860px;
      max-height: 90vh;
      display: flex;
      flex-direction: column;
      padding: 1.75rem;
      gap: 1rem;
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.85);
      animation: modalSlide 0.25s ease;
    }

    @keyframes modalSlide {
      from { opacity: 0; transform: translateY(12px) scale(0.98); }
      to { opacity: 1; transform: translateY(0) scale(1); }
    }

    .modal-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .modal-header h2 {
      font-family: var(--font-display);
      font-size: 1.25rem;
      font-weight: 800;
    }

    .cert-view {
      flex: 1;
      background: #fff;
      border-radius: 10px;
      min-height: 320px;
      max-height: 420px;
      overflow: auto;
      border: 2px solid #d97706;
    }

    .chat-history {
      background: #060a14;
      border: 1px solid var(--border-glass);
      border-radius: var(--radius-md);
      padding: 1rem;
      height: 280px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .chat-msg {
      padding: 0.65rem 0.95rem;
      border-radius: var(--radius-sm);
      font-size: 0.84rem;
      line-height: 1.5;
      max-width: 85%;
    }

    .chat-msg.mentor {
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid var(--border-glass);
      border-left: 3px solid var(--border-accent);
      color: #e2e8f0;
      align-self: flex-start;
    }

    .chat-msg.student {
      background: var(--primary);
      color: #fff;
      align-self: flex-end;
    }

    .shortcuts-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.65rem;
    }

    .shortcut-row {
      background: #080e1e;
      border: 1px solid var(--border-glass);
      padding: 0.5rem 0.8rem;
      border-radius: var(--radius-sm);
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.82rem;
    }

    kbd {
      background: #020617;
      border: 1px solid #334155;
      padding: 2px 6px;
      border-radius: 4px;
      font-family: var(--font-code);
      font-size: 0.72rem;
      color: #38bdf8;
    }

    /* PRESENTER & PROJECTOR MODE STYLES */
    body.projector-mode .studio {
      font-size: 1.08rem;
    }
    body.projector-mode .hero-title {
      font-size: 2.1rem;
    }
    body.projector-mode .theory-content {
      font-size: 1.15rem;
      line-height: 1.7;
    }
    body.projector-mode textarea {
      font-size: 1.12rem !important;
      line-height: 1.55 !important;
    }
    body.projector-mode .code-terminal {
      font-size: 1.02rem;
    }

    .tag-presenter {
      background: rgba(168, 85, 247, 0.25);
      border: 1px solid #a855f7;
      color: #d8b4fe;
      box-shadow: 0 0 14px rgba(168, 85, 247, 0.4);
    }

    /* CLASSROOM TIMER MODAL */
    .timer-huge-display {
      font-family: var(--font-code);
      font-size: 4.8rem;
      font-weight: 900;
      color: #38bdf8;
      text-shadow: 0 0 35px rgba(56, 189, 248, 0.65);
      text-align: center;
      margin: 1.2rem 0;
      letter-spacing: 3px;
    }
    .timer-presets-row {
      display: flex;
      justify-content: center;
      gap: 0.5rem;
      flex-wrap: wrap;
      margin-bottom: 1.2rem;
    }
    .timer-preset-btn {
      background: #060b18;
      border: 1px solid #334155;
      color: #94a3b8;
      padding: 0.35rem 0.85rem;
      border-radius: 6px;
      cursor: pointer;
      font-weight: 700;
      font-size: 0.82rem;
      transition: all var(--transition-fast);
    }
    .timer-preset-btn:hover, .timer-preset-btn.active {
      border-color: #38bdf8;
      color: #38bdf8;
      background: rgba(2, 132, 199, 0.2);
    }

    /* SPEAKER NOTES MODAL */
    .speaker-notes-section {
      background: #080f20;
      border: 1px solid rgba(168, 85, 247, 0.3);
      border-radius: 8px;
      padding: 1rem;
      margin-bottom: 0.85rem;
    }
    .speaker-notes-title {
      font-size: 0.88rem;
      font-weight: 800;
      color: #c084fc;
      margin-bottom: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    /* SPLIT-SCREEN EMBEDDED WEB DOCS */
    .docs-split-panel {
      width: 480px;
      min-width: 360px;
      max-width: 55vw;
      background: #020612;
      border-right: 1px solid var(--border-glass);
      display: flex;
      flex-direction: column;
      height: calc(100vh - 125px);
      transition: width var(--transition-fast);
      position: relative;
      z-index: 10;
      flex-shrink: 0;
    }
    .docs-split-panel.hidden {
      display: none !important;
    }
    .docs-panel-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0.5rem 0.85rem;
      background: #060d1e;
      border-bottom: 1px solid var(--border-glass);
    }
    .docs-panel-title {
      font-size: 0.82rem;
      font-weight: 800;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }
    .action-mini-btn {
      background: #0b1426;
      border: 1px solid #334155;
      color: #94a3b8;
      width: 26px;
      height: 26px;
      border-radius: 4px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.8rem;
      transition: all var(--transition-fast);
    }
    .action-mini-btn:hover {
      border-color: #38bdf8;
      color: #38bdf8;
      background: rgba(2, 132, 199, 0.2);
    }
    .docs-frame-wrapper {
      flex: 1;
      width: 100%;
      height: 100%;
      background: #020612;
      position: relative;
    }
    .docs-frame-wrapper iframe {
      width: 100%;
      height: 100%;
      border: none;
      background: #0b0f19;
    }

    .docs-resize-handle {
      position: absolute;
      top: 0;
      right: -4px;
      width: 8px;
      height: 100%;
      cursor: col-resize;
      background: transparent;
      z-index: 20;
      transition: background 0.15s ease;
    }
    .docs-resize-handle:hover, .docs-resize-handle.active {
      background: #38bdf8;
      box-shadow: 0 0 10px #38bdf8;
    }

    /* SLIDE DECK FULLSCREEN PRESENTATION */
    .slide-deck-container {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      background: #020612;
      z-index: 9999;
      display: flex;
      flex-direction: column;
      color: #fff;
    }
    .slide-deck-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0.75rem 1.5rem;
      background: #080f24;
      border-bottom: 1px solid var(--border-glass);
    }
    .slide-deck-body {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 2rem;
      overflow-y: auto;
    }
    .slide-content-card {
      max-width: 1050px;
      width: 100%;
      background: #0b142c;
      border: 1px solid var(--border-glass);
      border-radius: 16px;
      padding: 2.2rem;
      box-shadow: 0 0 50px rgba(2, 132, 199, 0.2);
    }
    .slide-deck-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0.75rem 1.5rem;
      background: #080f24;
      border-top: 1px solid var(--border-glass);
    }

    @media (max-width: 1024px) {
      .two-col-grid { grid-template-columns: 1fr; }
      .stepper-container { grid-template-columns: repeat(2, 1fr); }
      .footer-grid { grid-template-columns: 1fr; }
      .memory-board-dual { grid-template-columns: 1fr; }
      .pythonic-diff-card { grid-template-columns: 1fr; }
      .quiz-options-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
  <div class="app-wrapper">
    
    <!-- 1. HEADER GLOBAL STICKY CON NAVEGACIÓN Y CONTROLES -->
    <header class="app-header">
      <div class="brand-cluster">
        <div class="brand-logo-badge" title="Wisrovi Python Academy">🐍</div>
        <div class="brand-text">
          <h1>Wisrovi Academy</h1>
          <p>Virtual AI Tutor &bull; Master Edition (32 Clases &bull; 4 Cursos)</p>
        </div>
        <div class="engine-status-pill">
          <div class="pulse-dot"></div>
          <span>Motor Activo</span>
        </div>
      </div>

      <div class="gamification-controls">
        <button class="command-search-btn" id="cmd-k-btn" title="Buscar Clase o Concepto (Ctrl+K)">
          <span>🔍 Buscar...</span>
          <kbd>Ctrl K</kbd>
        </button>

        <select class="theme-select" id="theme-selector" title="Cambiar Tema Visual">
          <option value="midnight">🌌 Midnight</option>
          <option value="obsidian">🕳️ Obsidian</option>
          <option value="emerald">🟢 Matrix</option>
          <option value="solar">🌅 Solar</option>
        </select>

        <button class="user-avatar-btn" id="avatar-toggle-btn" title="Perfil y Ajustes">👨‍💻</button>

        <div class="badge-pill badge-level" id="player-level-badge">
          <span>🌱</span>
          <span id="player-level-title">Nv. 1 Aprendiz</span>
        </div>

        <div class="xp-meter-box">
          <div class="xp-text-row">
            <span>XP: <strong id="player-xp-val" style="color: #38bdf8;">0</strong></span>
            <span id="xp-progress-percent">0%</span>
          </div>
          <div class="xp-track">
            <div class="xp-fill" id="player-xp-fill" style="width: 5%;"></div>
          </div>
        </div>

        <div class="badge-pill badge-streak" title="Racha de días de estudio continuo">
          <span>🔥</span>
          <span id="player-streak">1 Días</span>
        </div>

        <div class="badge-pill badge-timer" title="Tiempo de pedaleo activo en la sesión">
          <span>⏱️</span>
          <span id="session-timer">00:00</span>
        </div>

        <button class="header-btn" id="achievements-btn" title="Ver Trofeos e Insignias">
          🏆 Logros
        </button>

        <button class="header-btn" id="toggle-mode-btn" style="background: rgba(168, 85, 247, 0.2); border: 1px solid #a855f7; color: #d8b4fe; font-weight: 800;" title="Alternar entre Modo Estudiante y Modo Presentador Docente">
          <span id="mode-btn-icon">👨‍🏫</span> <span id="mode-btn-text">Modo Presentador</span>
        </button>

        <button class="header-btn tutor-only" id="projector-mode-btn" style="display:none; background: rgba(2, 132, 199, 0.2); border: 1px solid #38bdf8; color: #7dd3fc;" title="Activar Pantalla Completa / Proyector de Gran Formato">
          📺 Proyector
        </button>

        <button class="header-btn tutor-only" id="speaker-notes-btn" style="display:none; background: rgba(234, 179, 8, 0.2); border: 1px solid #eab308; color: #fde047;" title="Ver Notas Pedagógicas del Mentor y Preguntas de Clase">
          📝 Notas Docente
        </button>

        <button class="header-btn tutor-only" id="classroom-timer-btn" style="display:none; background: rgba(16, 185, 129, 0.2); border: 1px solid #10b981; color: #6ee7b7;" title="Temporizador de Reto para el Aula">
          ⏱️ Temporizador
        </button>

        <button class="header-btn tutor-only" id="slide-deck-btn" style="display:none; background: rgba(168, 85, 247, 0.2); border: 1px solid #a855f7; color: #d8b4fe;" title="Abrir Modo Diapositivas para Ponencias / Streaming (F)">
          📽️ Diapositivas
        </button>

        <button class="header-btn" id="sound-toggle-btn" title="Alternar Sonido Sintetizado">
          <span id="sound-icon">🔊</span> Sonido
        </button>

        <button class="header-btn" id="shortcuts-btn" title="Atajos de Teclado (?)">
          ⌨️ Atajos
        </button>

        <button class="header-btn" id="toggle-docs-drawer-btn" style="background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); color: #38bdf8; font-weight: 800;" title="Abrir Documentación Oficial Web en Pantalla Dividida (Alt+D)">
          <span id="docs-drawer-icon">📖</span> <span id="docs-drawer-text">Doc Web (Split)</span>
        </button>

        <button class="cert-btn" id="open-cert-btn" title="Ver Diplomas y Certificaciones">
          📜 Diplomas
        </button>

        <button class="btn" id="header-linkedin-btn" style="background:#0a66c2; color:#fff; border:none; font-weight:800; font-size:0.82rem; padding:0.35rem 0.75rem; border-radius:6px; display:flex; align-items:center; gap:0.35rem; box-shadow:0 0 12px rgba(10,102,194,0.4); cursor:pointer;" title="Publicar tu Acreditación en LinkedIn">
          <span>🚀</span> Publicar en LinkedIn
        </button>
      </div>
    </header>

    <!-- 2. SELECTOR DE CURSO DIRECTO (TABS C1..C4) -->
    <nav class="course-tabs-bar" id="course-tabs-bar">
      <button class="course-tab-btn active" data-course="1">🟢 C1: Fundamentos (8)</button>
      <button class="course-tab-btn" data-course="2">⚡ C2: Algoritmos &amp; Big-O (8)</button>
      <button class="course-tab-btn" data-course="3">🤖 C3: Agentes de IA &amp; RAG (8)</button>
      <button class="course-tab-btn" data-course="4">🏆 C4: Proyecto Full-Stack (8)</button>
    </nav>

    <!-- 3. BARRA DE BREADCRUMBS Y ATAJOS -->
    <div class="breadcrumbs-bar">
      <div class="breadcrumbs-list">
        <button class="toggle-sidebar-btn" id="toggle-sidebar-btn" title="Ocultar / Mostrar Barra Lateral (Ctrl+B)">☰</button>
        <span>Wisrovi Academy</span>
        <span class="breadcrumb-sep">&gt;</span>
        <span class="breadcrumb-item" id="crumb-course">Curso 1: Fundamentos Básicos</span>
        <span class="breadcrumb-sep">&gt;</span>
        <span class="breadcrumb-item" id="crumb-class">Clase 01: Primer Vistazo</span>
        <span class="breadcrumb-sep">&gt;</span>
        <span style="color: #34d399;" id="crumb-step">Paso 1: Concepto</span>
      </div>
      <div style="font-size: 0.76rem; color: #94a3b8; display: flex; align-items: center; gap: 0.75rem;">
        <span>💡 Atajo: <kbd>Ctrl + Enter</kbd> Ejecutar</span>
        <span>|</span>
        <span><kbd>Alt + D</kbd> Doc Split</span>
        <span>|</span>
        <span><kbd>F</kbd> Diapositivas</span>
        <span>|</span>
        <span><kbd>Ctrl + B</kbd> Sidebar</span>
      </div>
    </div>

    <!-- 4. CUERPO PRINCIPAL (SIDEBAR + DOCS SPLIT + STUDIO) -->
    <div class="main-workspace">
      
      <!-- SIDEBAR CURRICULAR -->
      <aside class="sidebar" id="app-sidebar">
        <div class="sidebar-header">
          <div class="sidebar-title-row">
            <h2>🗺️ Hoja de Ruta</h2>
            <span class="progress-tag" id="total-progress-pill">0% Hecho</span>
          </div>
          <div class="sidebar-search-box">
            <input type="text" id="sidebar-filter-input" class="sidebar-search-input" placeholder="Filtrar 32 clases o temas...">
          </div>
        </div>
        <div class="curriculum-tree" id="class-tree-container">
          <!-- Inyectado dinámicamente por JS -->
        </div>
      </aside>

      <!-- PANEL DE DOCUMENTACIÓN OFICIAL WEB EMBEBIDA (SPLIT-SCREEN) -->
      <aside class="docs-split-panel hidden" id="docs-split-panel">
        <div class="docs-panel-header">
          <div class="docs-panel-title">
            <span>📖 Doc Web Oficial</span>
            <span id="docs-frame-class-badge" style="font-size:0.72rem; color:#38bdf8; font-weight:700; background:rgba(56,189,248,0.15); padding:2px 6px; border-radius:4px;">C1-S01</span>
          </div>
          <div style="display:flex; gap:0.35rem; align-items:center;">
            <button class="action-mini-btn" id="reload-docs-frame-btn" title="Recargar Documentación">🔄</button>
            <button class="action-mini-btn" id="open-docs-ext-btn" title="Abrir en pestaña externa">↗️</button>
            <button class="action-mini-btn" id="close-docs-drawer-btn" title="Cerrar Panel Dividido">&times;</button>
          </div>
        </div>
        <div class="docs-frame-wrapper">
          <iframe id="docs-iframe" src="https://academy_python.wisrovi.dev/curso-01/clase-01/" title="Documentación Oficial Wisrovi"></iframe>
        </div>
        <div class="docs-resize-handle" id="docs-resize-handle" title="Arrastra horizontalmente para ajustar el ancho"></div>
      </aside>

      <!-- ESTUDIO CENTRAL -->
      <main class="studio">
        
        <!-- HERO CARD DE LA CLASE -->
        <div class="hero-card">
          <div class="hero-tags">
            <span class="tag-course" id="lesson-course-name">Curso 1: Fundamentos Básicos</span>
            <span class="tag-mode tag-active" id="lesson-mode-badge">🚀 Lección Activa</span>
            <span class="tag-boss" id="lesson-boss-badge" style="display: none;">⚔️ Boss Battle</span>
          </div>
          <h2 class="hero-title" id="lesson-title">Cargando Clase...</h2>
          <div class="metaphor-box">
            <div style="display: flex; align-items: center; gap: 0.5rem;">
              <span>🌟</span>
              <span id="lesson-metaphor">Metáfora: «El Megáfono, las Cajas y el Semáforo»</span>
            </div>
            <div class="voice-controls-group">
              <select class="speed-select" id="voice-speed-select" title="Velocidad de voz">
                <option value="0.85">0.85x</option>
                <option value="1.0" selected>1.0x</option>
                <option value="1.2">1.2x</option>
                <option value="1.5">1.5x</option>
              </select>
              <button class="listen-btn" id="listen-metaphor-btn">🔊 Escuchar al Mentor</button>
            </div>
          </div>
        </div>

        <!-- STEPPER GATES (4 PASOS OBLIGATORIOS) -->
        <nav class="stepper-container">
          <div class="step-gate-pill active" id="gate-step-1" data-step="1">
            <div class="step-gate-info">
              <span>💡</span> 1. Concepto &amp; Quiz
            </div>
            <span class="step-gate-status" id="status-step-1">Pendiente</span>
          </div>

          <div class="step-gate-pill" id="gate-step-2" data-step="2">
            <div class="step-gate-info">
              <span>💻</span> 2. Demo &amp; Pythonic
            </div>
            <span class="step-gate-status" id="status-step-2">Pendiente</span>
          </div>

          <div class="step-gate-pill" id="gate-step-3" data-step="3">
            <div class="step-gate-info">
              <span>🔬</span> 3. Arenero &amp; RAM
            </div>
            <span class="step-gate-status" id="status-step-3">Pendiente</span>
          </div>

          <div class="step-gate-pill" id="gate-step-4" data-step="4">
            <div class="step-gate-info">
              <span>🏋️</span> 4. Reto Evaluado
            </div>
            <span class="step-gate-status" id="status-step-4">Pendiente</span>
          </div>
        </nav>

        <!-- PASO 1: CONCEPTO & MERMAID & MICRO-QUIZ -->
        <div class="tab-pane active" id="pane-step-1">
          <div class="two-col-grid">
            <div class="glass-card">
              <h3>💡 Fundamentación Teórica</h3>
              <p class="theory-desc" id="theory-text">Cargando fundamentación...</p>
              
              <!-- MICRO-QUIZ INTERACTIVO -->
              <div class="quiz-card" id="quiz-container">
                <div class="flex-between">
                  <span class="quiz-question-title" id="quiz-question-text">❓ Micro-Quiz Conceptual (+25 XP)</span>
                  <span style="font-size:0.72rem; color:#34d399; font-weight:800;" id="quiz-status-badge">Auto-Evaluación</span>
                </div>
                <div class="quiz-options-grid" id="quiz-options-grid"></div>
                <div id="quiz-feedback-box" style="font-size:0.8rem; color:#cbd5e1; display:none; padding:0.4rem; border-radius:4px;"></div>
              </div>

              <div class="mentor-box">
                <div class="mentor-avatar">👨‍🏫</div>
                <div>
                  <strong>Consejo de Arquitectura (Wisrovi):</strong>
                  <p id="mentor-advice">Piensa en los datos como objetos tangibles en la memoria RAM antes de escribir código.</p>
                </div>
              </div>
              
              <button class="btn btn-success" id="confirm-concept-btn" style="margin-top: auto;">
                ✅ Confirmar Concepto y Avanzar (Paso 1)
              </button>
            </div>

            <div class="glass-card">
              <div class="flex-between">
                <h3>🗺️ Arquitectura Visual de Flujo</h3>
                <button class="tool-btn" id="expand-mermaid-btn">🔍 Zoom Completo</button>
              </div>
              <div class="mermaid-canvas" id="mermaid-render-box"></div>
            </div>
          </div>
        </div>

        <!-- PASO 2: DEMOSTRACIÓN INTERACTIVA & COMPARACIÓN PYTHONIC -->
        <div class="tab-pane" id="pane-step-2">
          <div class="glass-card">
            <div class="flex-between">
              <h3>💻 Código de Demostración Comentado</h3>
              <div style="display:flex; gap:0.5rem; align-items:center;">
                <span id="demo-runtime-badge" style="font-size:0.75rem; color:#94a3b8; font-family:var(--font-code);"></span>
                <button class="btn btn-primary" id="run-demo-btn">▶️ Ejecutar Demo (Completar Paso 2)</button>
              </div>
            </div>
            
            <div class="editor-wrapper">
              <div class="editor-toolbar">
                <span>🐍 Python 3 &bull; Modo Lectura / Ejecución</span>
                <div class="editor-actions">
                  <button class="tool-btn" id="copy-demo-btn">📋 Copiar Código</button>
                </div>
              </div>
              <div class="editor-body-with-lines">
                <div class="line-numbers-gutter" id="demo-lines">1</div>
                <textarea class="code-editor" id="demo-code-area" readonly spellcheck="false"></textarea>
              </div>
            </div>

            <div class="terminal-output" id="demo-terminal">&gt; Presiona 'Ejecutar Demo' o usa Ctrl+Enter para compilar y validar.</div>

            <!-- PATRÓN PYTHONIC VS ANTIPATRÓN -->
            <div class="pythonic-diff-card" id="pythonic-diff-container">
              <div class="diff-box">
                <span class="diff-tag-bad">❌ Antipatrón / Estilo No-Pythonic</span>
                <pre class="diff-code-pre" id="antipattern-code">if x == True: pass</pre>
              </div>
              <div class="diff-box">
                <span class="diff-tag-good">✨ Patrón Idiomático (PEP 8 Pythonic)</span>
                <pre class="diff-code-pre" id="pythonic-code">if x: pass</pre>
              </div>
            </div>
          </div>
        </div>

        <!-- PASO 3: ARENERO & VISUALIZADOR DE MEMORIA 3.0 -->
        <div class="tab-pane" id="pane-step-3">
          <div class="two-col-grid">
            <div class="glass-card">
              <div class="flex-between">
                <h3>🔬 Arenero de Experimentación</h3>
                <div style="display:flex; gap:0.4rem;">
                  <button class="tool-btn primary-tool" id="format-sandbox-btn">✨ Formatear (PEP 8)</button>
                  <button class="btn btn-primary" id="run-sandbox-btn">⚡ Inspeccionar RAM</button>
                </div>
              </div>

              <div class="editor-wrapper">
                <div class="editor-toolbar">
                  <span>Modifica variables para inspeccionar su dirección y tamaño</span>
                  <div class="editor-actions">
                    <select class="snippet-select" id="sandbox-snippets-select" title="Cargar fragmento rápido">
                      <option value="">⚡ Snippets...</option>
                      <option value="types">Tipos y Casting</option>
                      <option value="id_check">Direcciones id()</option>
                      <option value="fstrings">Formato f-strings</option>
                      <option value="loops">Bucles y Comprensiones</option>
                    </select>
                    <button class="tool-btn" id="reset-sandbox-btn">🔄 Restaurar</button>
                    <button class="tool-btn" id="clear-sandbox-btn">🧹 Limpiar</button>
                  </div>
                </div>
                <div class="editor-body-with-lines">
                  <div class="line-numbers-gutter" id="sandbox-lines">1</div>
                  <textarea class="code-editor" id="sandbox-code-area" spellcheck="false"></textarea>
                </div>
              </div>

              <div class="terminal-output" id="sandbox-terminal">&gt; Modifica variables y pulsa 'Inspeccionar RAM'.</div>
            </div>

            <div class="glass-card">
              <div class="flex-between">
                <h3>🧠 Visualizador Dual: Stack &amp; Heap RAM 3.0</h3>
                <span style="font-size: 0.74rem; color: #fbbf24; font-weight: 800;" id="mem-total-count">0 Variables</span>
              </div>
              <div class="memory-board-dual" id="memory-canvas">
                <div class="empty-state">Ejecuta código para visualizar las variables en la memoria RAM.</div>
              </div>
            </div>
          </div>
        </div>

        <!-- PASO 4: RETO EVALUADO & AUTO-FORMATTER -->
        <div class="tab-pane" id="pane-step-4">
          <div class="two-col-grid">
            <div class="glass-card">
              <div class="flex-between">
                <div>
                  <h3>🏋️ Desafío Práctico de la Clase</h3>
                  <p style="font-size: 0.85rem; color: #94a3b8; margin-top: 0.2rem;" id="challenge-prompt-text">Crea la función indicada.</p>
                </div>
                <div style="display:flex; gap:0.4rem;">
                  <button class="tool-btn primary-tool" id="format-challenge-btn">✨ Formatear</button>
                  <button class="btn btn-success" id="eval-challenge-btn">🚀 Evaluar Reto (+150 XP)</button>
                </div>
              </div>

              <div class="editor-wrapper">
                <div class="editor-toolbar">
                  <span id="diff-status-label" style="color: #fb923c; font-weight: 700;">⚠️ Modifica el código antes de evaluar</span>
                  <div class="editor-actions">
                    <button class="tool-btn" id="save-reto-disk-btn" style="color: #38bdf8; border-color: rgba(56,189,248,0.4);" title="Guardar directamente en ejercicios/reto.py">💾 Guardar en Disco</button>
                    <button class="tool-btn" id="download-solution-btn">📥 Descargar .py</button>
                    <button class="tool-btn" id="reset-challenge-btn">🔄 Restaurar</button>
                  </div>
                </div>
                <div class="editor-body-with-lines">
                  <div class="line-numbers-gutter" id="challenge-lines">1</div>
                  <textarea class="code-editor" id="challenge-code-area" spellcheck="false"></textarea>
                </div>
              </div>

              <div id="challenge-results-box" style="margin-top: 0.5rem;">
                <div style="color: #64748b; font-size: 0.85rem; font-style: italic;">Modifica la plantilla con tu solución y pulsa 'Evaluar Reto'.</div>
              </div>
            </div>

            <div class="glass-card">
              <div class="flex-between">
                <h3>💡 Pistas Socráticas del Mentor</h3>
                <button class="tool-btn" id="ask-mentor-modal-btn">💬 Preguntar al Mentor</button>
              </div>
              <div id="hints-accordion" style="display: flex; flex-direction: column; gap: 0.5rem;"></div>
              <div style="background: rgba(2, 132, 199, 0.12); border: 1px solid var(--border-accent); padding: 0.85rem; border-radius: var(--radius-md); margin-top: auto;">
                <strong style="color: #38bdf8;">🏆 Recompensa:</strong>
                <p style="font-size: 0.82rem; color: #cbd5e1; margin-top: 0.25rem;">+150 XP &bull; Sello de acreditación &bull; Desbloqueo de siguiente clase.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- FOOTER DE NAVEGACIÓN -->
        <footer class="studio-footer">
          <button class="btn btn-secondary" id="prev-class-btn">⬅️ Clase Anterior</button>
          <div class="class-status-summary" id="class-status-summary">
            🔒 Completa los 4 pasos para desbloquear la siguiente clase.
          </div>
          <button class="btn btn-primary" id="next-class-btn" disabled>Siguiente Clase ➡️</button>
        </footer>

      </main>
    </div>

    <!-- 5. ASISTENTE FLOTANTE INTERACTIVO (WISROVI AI MENTOR) -->
    <div class="floating-mentor">
      <div class="mentor-speech-bubble" id="floating-speech-bubble">
        👋 ¡Hola! Soy tu <strong>Mentor Virtual Wisrovi</strong>. Explora los 4 cursos y completa los retos prácticos.
      </div>
      <div class="floating-avatar-btn" id="floating-mentor-avatar" title="Hablar con el Mentor">👨‍🏫</div>
    </div>

    <!-- 6. FOOTER INSTITUCIONAL COMPLETO -->
    <footer class="app-footer">
      <div class="footer-grid">
        <div class="footer-brand">
          <h4>🐍 Wisrovi Academy &bull; Python Masterclass</h4>
          <p>
            Programa Integral de Formación en Python: De Cero Absoluto a la Arquitectura de Agentes de Inteligencia Artificial.
            Diseñado bajo el modelo pedagógico del <strong>Aprendizaje en Espiral *(Spiral Learning)*</strong> y <strong>La Regla de la Bicicleta *(70%+ Práctica Activa)*</strong>.
          </p>
        </div>

        <div class="footer-col">
          <h5>👤 Dirección Académica</h5>
          <ul class="footer-links">
            <li><strong style="color: #fff;">William Rodríguez (Wisrovi)</strong></li>
            <li><span>Principal Software Engineer &amp; AI Architect</span></li>
            <li><a href="https://wisrovi.dev" target="_blank">🌐 Sitio Web: wisrovi.dev</a></li>
            <li><a href="https://github.com/wisrovi" target="_blank">🐙 GitHub: @wisrovi</a></li>
            <li><a href="https://www.linkedin.com/in/wisrovi-rodriguez/" target="_blank">💼 LinkedIn Oficial</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h5>📚 Recursos del Ecosistema</h5>
          <ul class="footer-links">
            <li><a href="https://academy_python.wisrovi.dev/" target="_blank">📖 Plataforma Web Docs</a></li>
            <li><a href="https://pypi.org/project/wisrovi-python/" target="_blank">📦 PyPI: wisrovi-python</a></li>
            <li><a href="https://codespaces.new/wisrovi/wisrovi-python" target="_blank">🚀 Abrir en Codespaces</a></li>
            <li><a href="https://github.com/wisrovi/wisrovi-python" target="_blank">⭐ Repositorio en GitHub</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <span>&copy; 2026 William Rodríguez (Wisrovi). Distribuido bajo Licencia de Código Abierto MIT.</span>
        <span>Badajoz, España &bull; Versión 2.1.0 &bull; Ecosistema Educativo de Nivel Mundial</span>
      </div>
    </footer>

    <!-- MODAL DE CERTIFICADOS MULTI-CURSO -->
    <div class="modal-backdrop hidden" id="cert-modal">
      <div class="modal-panel">
        <div class="modal-header">
          <h2>📜 Certificación Oficial de Acreditación</h2>
          <button style="background:none; border:none; color:#fff; font-size:1.6rem; cursor:pointer;" id="close-cert-btn">&times;</button>
        </div>
        <div style="display:grid; grid-template-columns: 2fr 1fr 1fr; gap:0.6rem; align-items:center;">
          <div>
            <label style="font-size:0.75rem; color:#94a3b8;">Nombre en el Diploma:</label>
            <input type="text" id="student-name-input" style="width:100%; padding:0.4rem 0.65rem; background:#060911; border:1px solid #334155; color:#fff; border-radius:6px; font-weight:700;" value="Estudiante Wisrovi">
          </div>
          <div>
            <label style="font-size:0.75rem; color:#94a3b8;">Programa o Clase a Certificar:</label>
            <select id="cert-course-select" style="width:100%; padding:0.4rem 0.65rem; background:#060911; border:1px solid #334155; color:#fff; border-radius:6px; font-weight:700;">
              <option value="master" selected>🏆 Master Diploma del Programa (160h)</option>
              <option value="1">📘 Curso 1: Fundamentos Básicos (40h)</option>
              <option value="2">🚀 Curso 2: Algoritmos Avanzados (40h)</option>
              <option value="3">🤖 Curso 3: Agentes de IA (40h)</option>
              <option value="4">🛠️ Curso 4: Proyecto Final (40h)</option>
              <option value="current">🎓 Micro-Diploma de la Clase Actual</option>
            </select>
          </div>
          <button class="btn btn-primary" id="refresh-cert-btn" style="height:35px; align-self:flex-end;">Actualizar Vista</button>
        </div>
        <div class="cert-view" id="cert-preview-frame"></div>
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.6rem;">
          <div style="display:flex; gap:0.5rem;">
            <button class="btn btn-secondary" id="copy-badge-btn">📋 Copiar Badge GitHub</button>
            <button class="btn" id="download-cert-png-btn" style="background:#059669; color:#fff; border:none;">🖼️ Descargar PNG</button>
          </div>
          <div style="display:flex; gap:0.5rem;">
            <button class="btn" id="cert-modal-linkedin-btn" style="background:#0a66c2; color:#fff; border:none; font-weight:800; display:flex; align-items:center; gap:0.35rem; cursor:pointer;">
              <span>🚀</span> Publicar en LinkedIn
            </button>
            <button class="btn btn-success" id="download-cert-btn">📥 Descargar PDF Oficial</button>
          </div>
        </div>
      </div>
    </div>

    <!-- MODAL CELEBRACIÓN DE DIPLOMA DE CLASE -->
    <div class="modal-backdrop hidden" id="class-cert-modal" style="z-index: 12000;">
      <div class="modal-panel" style="max-width: 880px; border: 2px solid #d97706; box-shadow: 0 0 50px rgba(217, 119, 6, 0.45); background: #0b1120;">
        <div class="modal-header" style="border-bottom: 1px solid rgba(217, 119, 6, 0.35); padding-bottom: 0.75rem;">
          <div style="display:flex; align-items:center; gap:0.65rem;">
            <span style="font-size:2rem;">🎉</span>
            <div>
              <h2 style="margin:0; font-size:1.35rem; color:#fbbf24;" id="class-cert-modal-title">¡Felicitaciones! Has obtenido tu Micro-Diploma Oficial</h2>
              <p style="margin:0; font-size:0.82rem; color:#94a3b8;" id="class-cert-modal-subtitle">Acreditación de competencia técnica verificada por Wisrovi Academy</p>
            </div>
          </div>
          <button style="background:none; border:none; color:#fff; font-size:1.8rem; cursor:pointer;" id="close-class-cert-btn">&times;</button>
        </div>

        <!-- BARRA DE PASOS GUIADOS -->
        <div style="display:grid; grid-template-columns: 1fr 1fr 1fr; gap:0.5rem; margin: 0.6rem 0; font-size: 0.75rem; text-align: center;">
          <div style="background: rgba(56, 189, 248, 0.15); border: 1px solid #38bdf8; border-radius: 6px; padding: 0.4rem; color: #7dd3fc;">
            <strong>1. Personaliza tu Nombre</strong>
          </div>
          <div style="background: rgba(217, 119, 6, 0.15); border: 1px solid #d97706; border-radius: 6px; padding: 0.4rem; color: #fde68a;">
            <strong>2. Revisa tu Diploma</strong>
          </div>
          <div style="background: rgba(10, 102, 194, 0.25); border: 1px solid #0a66c2; border-radius: 6px; padding: 0.4rem; color: #93c5fd;">
            <strong>3. Publica en LinkedIn (Texto + PNG)</strong>
          </div>
        </div>

        <div style="display:flex; gap:0.6rem; align-items:center; margin-bottom: 0.6rem;">
          <div style="flex:1;">
            <label style="font-size:0.75rem; color:#94a3b8; font-weight:700;">Nombre completo para tu Diploma:</label>
            <input type="text" id="class-cert-student-name" style="width:100%; padding:0.45rem 0.75rem; background:#060911; border:1px solid #38bdf8; color:#38bdf8; border-radius:6px; font-weight:800; font-size:0.95rem;" value="Estudiante Wisrovi">
          </div>
          <button class="btn btn-primary" id="update-class-cert-btn" style="height:38px; align-self:flex-end;">🔄 Actualizar Diploma</button>
        </div>

        <div class="cert-view" id="class-cert-preview-frame" style="max-height: 340px; overflow-y:auto; border-radius: 8px; border: 1px solid #334155; margin-bottom: 0.6rem;"></div>

        <!-- CENTRO DE PUBLICACIÓN EN LINKEDIN Y REDES -->
        <div style="background: rgba(15, 23, 42, 0.95); border: 1px solid #1e293b; border-radius: 8px; padding: 0.85rem;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 0.45rem; flex-wrap:wrap; gap:0.4rem;">
            <div style="display:flex; align-items:center; gap:0.4rem;">
              <span style="font-size:1.1rem;">💼</span>
              <strong style="color:#60a5fa; font-size:0.85rem;">Texto oficial de tu publicación para LinkedIn:</strong>
            </div>
            <div style="display:flex; gap:0.4rem; align-items:center;">
              <button class="btn" id="open-linkedin-top-btn" style="background:#0a66c2; color:#fff; border:none; font-size:0.75rem; font-weight:800; padding:0.25rem 0.65rem; border-radius:4px; cursor:pointer;">🚀 Publicar en LinkedIn</button>
              <button class="btn btn-secondary" id="copy-linkedin-post-btn" style="font-size:0.75rem; padding:0.25rem 0.6rem;">📋 Copiar Texto</button>
              <button class="btn" id="download-class-png-quick-btn" style="background:#059669; color:#fff; border:none; font-size:0.75rem; padding:0.25rem 0.6rem; border-radius:4px;">🖼️ Descargar PNG</button>
            </div>
          </div>
          <textarea id="class-cert-linkedin-text" style="width:100%; height:75px; background:#020612; border:1px solid #334155; border-radius:6px; color:#cbd5e1; font-size:0.78rem; padding:0.45rem; resize:vertical; font-family:inherit; line-height:1.35;"></textarea>
          
          <!-- BANNER GUÍA DE PUBLICACIÓN LINKEDIN -->
          <div id="linkedin-share-guide-toast" class="hidden" style="margin-top:0.5rem; background:rgba(10,102,194,0.18); border:1px solid #0a66c2; border-radius:6px; padding:0.55rem 0.75rem; font-size:0.78rem; color:#bfdbfe; line-height:1.4;">
            ✨ <strong>¡Todo listo para publicar en LinkedIn!</strong><br>
            1. 📋 Hemos copiado el texto a tu portapapeles (pégalo con <kbd style="background:#1e293b; padding:1px 4px; border-radius:3px;">Ctrl+V</kbd> en la ventana que se abrió).<br>
            2. 🖼️ Hemos descargado tu Diploma en formato PNG a tu equipo para que lo adjuntes como imagen.<br>
            3. 👤 Etiqueta a tu mentor <a href="https://es.linkedin.com/in/wisrovi-rodriguez" target="_blank" style="color:#38bdf8; text-decoration:underline; font-weight:700;">William Rodríguez (Wisrovi)</a> en el post.
          </div>

          <!-- MENTOR ATTRIBUTION BAR -->
          <div style="margin-top: 0.5rem; display:flex; justify-content:space-between; align-items:center; font-size:0.78rem; color:#94a3b8; border-top:1px solid #1e293b; padding-top:0.45rem; flex-wrap:wrap; gap:0.4rem;">
            <span>👨‍🏫 Mentor Oficial: <a href="https://es.linkedin.com/in/wisrovi-rodriguez" target="_blank" style="color:#38bdf8; font-weight:700; text-decoration:underline;">William Rodríguez (Wisrovi) en LinkedIn ↗</a></span>
            <div style="display:flex; gap:0.4rem; align-items:center;">
              <button class="btn" id="share-linkedin-inline-btn" style="font-size:0.78rem; padding:0.25rem 0.65rem; background:#0a66c2; color:#fff; border:none; font-weight:800; border-radius:4px; display:inline-flex; align-items:center; gap:0.35rem; cursor:pointer; box-shadow:0 0 10px rgba(10,102,194,0.4);"><span>💼</span> Compartir en LinkedIn</button>
              <button class="btn btn-secondary" id="share-twitter-btn" style="font-size:0.72rem; padding:0.2rem 0.5rem; background:#000; color:#fff; border:1px solid #334155;">𝕏 Compartir</button>
              <button class="btn btn-secondary" id="share-whatsapp-btn" style="font-size:0.72rem; padding:0.2rem 0.5rem; background:#128c7e; color:#fff; border:none;">💬 WhatsApp</button>
            </div>
          </div>
        </div>

        <!-- BOTONERA INFERIOR PRINCIPAL -->
        <div style="display:flex; justify-content:space-between; align-items:center; margin-top: 0.75rem; flex-wrap: wrap; gap: 0.5rem;">
          <div style="display:flex; gap:0.5rem;">
            <button class="btn btn-primary" id="download-class-pdf-btn" style="background:#0284c7; border:none; font-weight:700; display:flex; align-items:center; gap:0.4rem;">
              <span>📄</span> Descargar PDF Oficial (LaTeX)
            </button>
            <button class="btn btn-success" id="download-class-png-btn" style="background:#059669; border:none; font-weight:700; display:flex; align-items:center; gap:0.4rem;">
              <span>🖼️</span> Descargar PNG
            </button>
          </div>
          <div style="display:flex; gap:0.5rem;">
            <button class="btn" id="share-linkedin-direct-btn" style="background:#0a66c2; color:#fff; border:none; font-weight:800; font-size:0.92rem; padding:0.5rem 1rem; border-radius:6px; display:flex; align-items:center; gap:0.5rem; box-shadow:0 0 20px rgba(10,102,194,0.45); cursor:pointer;">
              <span>🚀</span> Publicar en LinkedIn (Texto + Imagen)
            </button>
            <button class="btn btn-secondary" id="next-class-cert-btn" style="background:#334155; color:#fff; border:none; font-weight:700;">
              ➡️ Siguiente Lección
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- MODAL DE TROFEOS Y LOGROS -->
    <div class="modal-backdrop hidden" id="achievements-modal">
      <div class="modal-panel" style="max-width: 650px;">
        <div class="modal-header">
          <h2>🏆 Vitrina de Trofeos e Insignias</h2>
          <button style="background:none; border:none; color:#fff; font-size:1.6rem; cursor:pointer;" id="close-achievements-btn">&times;</button>
        </div>
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 0.85rem;" id="achievements-grid"></div>
      </div>
    </div>

    <!-- MODAL DE COMMAND PALETTE (CTRL+K) -->
    <div class="modal-backdrop hidden" id="cmd-k-modal">
      <div class="modal-panel" style="max-width: 550px; padding: 1.25rem;">
        <input type="text" id="cmd-k-input" placeholder="Escribe para buscar clases en los 4 cursos..." style="width:100%; padding:0.75rem 1rem; background:#020612; border:1px solid var(--border-accent); border-radius:8px; color:#fff; font-size:0.95rem; outline:none;">
        <div id="cmd-k-results" style="display:flex; flex-direction:column; gap:0.4rem; max-height:280px; overflow-y:auto; margin-top:0.75rem;"></div>
      </div>
    </div>

    <!-- MODAL DE CONSULTA AL MENTOR (SOCRÁTICO) -->
    <div class="modal-backdrop hidden" id="ask-mentor-modal">
      <div class="modal-panel" style="max-width: 650px;">
        <div class="modal-header">
          <h2>💬 Pregunta al Mentor Virtual (Wisrovi)</h2>
          <button style="background:none; border:none; color:#fff; font-size:1.6rem; cursor:pointer;" id="close-ask-mentor-btn">&times;</button>
        </div>
        <div class="chat-history" id="mentor-chat-history">
          <div class="chat-msg mentor">
            👋 Hola. ¿En qué parte del concepto, error o lógica de esta clase necesitas orientación socrática?
          </div>
        </div>
        <div style="display:flex; gap:0.6rem;">
          <input type="text" id="mentor-chat-input" placeholder="Pregunta sobre Big-O, Pydantic, FastAPI, memoria o el reto..." style="flex:1; padding:0.6rem 0.85rem; background:#020612; border:1px solid #334155; border-radius:8px; color:#fff; font-size:0.86rem; outline:none;">
          <button class="btn btn-primary" id="send-mentor-chat-btn">Enviar</button>
        </div>
      </div>
    </div>

    <!-- MODAL DE PERFIL Y AJUSTES -->
    <div class="modal-backdrop hidden" id="profile-modal">
      <div class="modal-panel" style="max-width: 520px;">
        <div class="modal-header">
          <h2>👤 Perfil del Estudiante &amp; Ajustes</h2>
          <button style="background:none; border:none; color:#fff; font-size:1.6rem; cursor:pointer;" id="close-profile-btn">&times;</button>
        </div>
        <div style="display:flex; flex-direction:column; gap:0.85rem;">
          <div>
            <label style="font-size:0.78rem; color:#94a3b8;">Avatar:</label>
            <div style="display:flex; gap:0.5rem; margin-top:0.35rem;" id="avatar-picker-row"></div>
          </div>
          <div>
            <label style="font-size:0.78rem; color:#94a3b8;">Nombre Completo:</label>
            <input type="text" id="profile-name-input" style="width:100%; padding:0.5rem 0.75rem; background:#060a14; border:1px solid #334155; color:#fff; border-radius:6px; font-weight:700; margin-top:0.25rem;">
          </div>
          <div>
            <label style="font-size:0.78rem; color:#94a3b8;">Correo Electrónico:</label>
            <input type="email" id="profile-email-input" style="width:100%; padding:0.5rem 0.75rem; background:#060a14; border:1px solid #334155; color:#fff; border-radius:6px; margin-top:0.25rem;">
          </div>
          <div style="display:flex; justify-content:space-between; margin-top:0.5rem;">
            <button class="btn btn-secondary" id="reset-progress-btn" style="color:#f87171; border-color:rgba(239,68,68,0.3);">⚠️ Reiniciar Progreso</button>
            <button class="btn btn-primary" id="save-profile-btn">Guardar Cambios</button>
          </div>
        </div>
      </div>
    </div>

    <!-- MODAL DE ATAJOS DE TECLADO -->
    <div class="modal-backdrop hidden" id="shortcuts-modal">
      <div class="modal-panel" style="max-width: 550px;">
        <div class="modal-header">
          <h2>⌨️ Atajos de Teclado y Productividad</h2>
          <button style="background:none; border:none; color:#fff; font-size:1.6rem; cursor:pointer;" id="close-shortcuts-btn">&times;</button>
        </div>
        <div class="shortcuts-grid">
          <div class="shortcut-row"><span>Ejecutar / Evaluar Código</span><kbd>Ctrl + Enter</kbd></div>
          <div class="shortcut-row"><span>Abrir Buscador de 32 Clases</span><kbd>Ctrl + K</kbd></div>
          <div class="shortcut-row"><span>Ocultar / Mostrar Sidebar</span><kbd>Ctrl + B</kbd></div>
          <div class="shortcut-row"><span>Abrir / Cerrar Doc Web (Split)</span><kbd>Alt + D</kbd></div>
          <div class="shortcut-row"><span>Ir al Paso 1 (Concepto)</span><kbd>Alt + 1</kbd></div>
          <div class="shortcut-row"><span>Ir al Paso 2 (Demo)</span><kbd>Alt + 2</kbd></div>
          <div class="shortcut-row"><span>Ir al Paso 3 (Arenero)</span><kbd>Alt + 3</kbd></div>
          <div class="shortcut-row"><span>Ir al Paso 4 (Reto)</span><kbd>Alt + 4</kbd></div>
          <div class="shortcut-row"><span>Cerrar Modales</span><kbd>Escape</kbd></div>
        </div>
      </div>
    </div>

    <!-- MODAL DE NOTAS DEL INSTRUCTOR (SPEAKER NOTES) -->
    <div class="modal-backdrop hidden" id="speaker-notes-modal">
      <div class="modal-panel" style="max-width: 680px;">
        <div class="modal-header">
          <h2>📝 Guía Pedagógica &amp; Notas del Mentor (Clase en Vivo)</h2>
          <button style="background:none; border:none; color:#fff; font-size:1.6rem; cursor:pointer;" id="close-speaker-notes-btn">&times;</button>
        </div>
        <div id="speaker-notes-body" style="display:flex; flex-direction:column; gap:0.75rem; max-height:480px; overflow-y:auto;">
          <!-- Inyectado dinámicamente -->
        </div>
      </div>
    </div>

    <!-- MODAL DE TEMPORIZADOR DE AULA PARA RETOS -->
    <div class="modal-backdrop hidden" id="classroom-timer-modal">
      <div class="modal-panel" style="max-width: 620px; text-align:center;">
        <div class="modal-header">
          <h2>⏱️ Temporizador de Reto de Aula</h2>
          <button style="background:none; border:none; color:#fff; font-size:1.6rem; cursor:pointer;" id="close-classroom-timer-btn">&times;</button>
        </div>
        <div id="timer-challenge-title" style="font-size:1.1rem; font-weight:800; color:#cbd5e1; margin-top:0.4rem;">Reto de la Clase</div>
        <div class="timer-huge-display" id="classroom-timer-display">10:00</div>
        <div class="timer-presets-row">
          <button class="timer-preset-btn" data-secs="180">3 min (Speed)</button>
          <button class="timer-preset-btn" data-secs="300">5 min (Sprint)</button>
          <button class="timer-preset-btn active" data-secs="600">10 min (Focus)</button>
          <button class="timer-preset-btn" data-secs="900">15 min (Standard)</button>
          <button class="timer-preset-btn" data-secs="1200">20 min (Deep)</button>
        </div>
        <div style="display:flex; justify-content:center; gap:0.75rem;">
          <button class="btn btn-primary" id="timer-toggle-btn" style="min-width:110px;">▶️ Iniciar</button>
          <button class="btn btn-secondary" id="timer-reset-btn">🔄 Reiniciar</button>
        </div>
      </div>
    <!-- MODAL DE DIAPOSITIVAS DE PRESENTACIÓN EN VIVO (SLIDE DECK) -->
    <div class="modal-backdrop hidden" id="slide-deck-modal">
      <div class="slide-deck-container">
        <div class="slide-deck-header">
          <div style="display:flex; align-items:center; gap:0.75rem;">
            <span style="font-size:1.4rem;">📽️</span>
            <div>
              <div id="slide-deck-title" style="font-weight:800; font-size:1.1rem; color:#38bdf8;">Curso 1 - Clase 01</div>
              <div id="slide-deck-meta" style="font-size:0.75rem; color:#94a3b8;">Diapositiva <span id="slide-current-num">1</span> de 5 &bull; Wisrovi Master Lecture Deck</div>
            </div>
          </div>
          <div style="display:flex; gap:0.5rem; align-items:center;">
            <button class="btn btn-secondary" id="slide-fs-btn" style="padding:0.35rem 0.75rem; font-size:0.8rem;">⛶ Pantalla Completa</button>
            <button style="background:none; border:none; color:#fff; font-size:1.8rem; cursor:pointer;" id="close-slide-deck-btn">&times;</button>
          </div>
        </div>
        
        <div class="slide-deck-body" id="slide-deck-body">
          <!-- Slide inyectada dinámicamente -->
        </div>

        <div class="slide-deck-footer">
          <button class="btn btn-secondary" id="slide-prev-btn" style="min-width:110px;">◀️ Anterior</button>
          <div style="font-size:0.82rem; color:#94a3b8;">Navegación: <kbd>←</kbd> y <kbd>→</kbd> del teclado o <kbd>Espacio</kbd></div>
          <button class="btn btn-primary" id="slide-next-btn" style="min-width:110px;">Siguiente ▶️</button>
        </div>
      </div>
    </div>

  </div>

  <!-- SCRIPT JS REACTIVO AUTOCONTENIDO v12.0 -->
  <script>
    document.addEventListener("DOMContentLoaded", () => {
      const state = {
        currentCourse: 1,
        currentClass: 1,
        profile: null,
        curriculum: [],
        classContent: null,
        currentStep: 1,
        soundEnabled: true,
        stepsCompleted: { 1: false, 2: false, 3: false, 4: false },
        starterChallengeCode: "",
        starterSandboxCode: "",
        starterDemoCode: "",
        elapsedSeconds: 0,
        sidebarCollapsed: false,
        isTutorMode: false,
        isProjectorMode: false,
        timerInterval: null,
        timerSecondsRemaining: 600,
        timerIsRunning: false,
        docsDrawerOpen: false,
        currentSlide: 1,
        totalSlides: 5
      };

      // Sintetizador Web Audio API nativo
      let audioCtx = null;
      function initAudio() {
        if (!audioCtx) {
          audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }
      }

      function playTone(freq, type, duration, gainVal = 0.08) {
        if (!state.soundEnabled) return;
        try {
          initAudio();
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

      function soundClick() { playTone(440, 'sine', 0.06, 0.04); }
      function soundChime() { playTone(587.33, 'triangle', 0.12, 0.06); setTimeout(() => playTone(880, 'sine', 0.22, 0.06), 90); }
      function soundVictory() {
        [523.25, 659.25, 783.99, 1046.50].forEach((f, idx) => {
          setTimeout(() => playTone(f, 'triangle', 0.32, 0.08), idx * 110);
        });
      }
      function soundError() { playTone(220, 'sawtooth', 0.18, 0.08); }

      // Inicializar Mermaid
      if (window.mermaid) {
        mermaid.initialize({ startOnLoad: false, theme: "dark", securityLevel: "loose" });
      }

      // Temporizador de sesión
      setInterval(() => {
        state.elapsedSeconds++;
        const m = Math.floor(state.elapsedSeconds / 60).toString().padStart(2, '0');
        const s = (state.elapsedSeconds % 60).toString().padStart(2, '0');
        const timerElem = document.getElementById("session-timer");
        if (timerElem) timerElem.textContent = `${m}:${s}`;
      }, 1000);

      const dom = {
        themeSelector: document.getElementById("theme-selector"),
        avatarBtn: document.getElementById("avatar-toggle-btn"),
        levelTitle: document.getElementById("player-level-title"),
        xpVal: document.getElementById("player-xp-val"),
        xpPercent: document.getElementById("xp-progress-percent"),
        xpFill: document.getElementById("player-xp-fill"),
        streak: document.getElementById("player-streak"),
        progressPill: document.getElementById("total-progress-pill"),
        classTree: document.getElementById("class-tree-container"),
        courseTabsBar: document.getElementById("course-tabs-bar"),
        courseName: document.getElementById("lesson-course-name"),
        modeBadge: document.getElementById("lesson-mode-badge"),
        bossBadge: document.getElementById("lesson-boss-badge"),
        lessonTitle: document.getElementById("lesson-title"),
        metaphor: document.getElementById("lesson-metaphor"),
        listenMetaphorBtn: document.getElementById("listen-metaphor-btn"),
        voiceSpeedSelect: document.getElementById("voice-speed-select"),
        soundToggleBtn: document.getElementById("sound-toggle-btn"),
        soundIcon: document.getElementById("sound-icon"),
        shortcutsBtn: document.getElementById("shortcuts-btn"),
        shortcutsModal: document.getElementById("shortcuts-modal"),
        closeShortcutsBtn: document.getElementById("close-shortcuts-btn"),
        floatingSpeech: document.getElementById("floating-speech-bubble"),
        floatingMentorAvatar: document.getElementById("floating-mentor-avatar"),
        
        // Presenter & Tutor Controls
        toggleModeBtn: document.getElementById("toggle-mode-btn"),
        modeBtnIcon: document.getElementById("mode-btn-icon"),
        modeBtnText: document.getElementById("mode-btn-text"),
        projectorModeBtn: document.getElementById("projector-mode-btn"),
        speakerNotesBtn: document.getElementById("speaker-notes-btn"),
        speakerNotesModal: document.getElementById("speaker-notes-modal"),
        closeSpeakerNotesBtn: document.getElementById("close-speaker-notes-btn"),
        speakerNotesBody: document.getElementById("speaker-notes-body"),
        classroomTimerBtn: document.getElementById("classroom-timer-btn"),
        classroomTimerModal: document.getElementById("classroom-timer-modal"),
        closeClassroomTimerBtn: document.getElementById("close-classroom-timer-btn"),
        classroomTimerDisplay: document.getElementById("classroom-timer-display"),
        timerToggleBtn: document.getElementById("timer-toggle-btn"),
        timerResetBtn: document.getElementById("timer-reset-btn"),
        timerChallengeTitle: document.getElementById("timer-challenge-title"),

        // Sidebar & Search
        appSidebar: document.getElementById("app-sidebar"),
        toggleSidebarBtn: document.getElementById("toggle-sidebar-btn"),
        sidebarFilterInput: document.getElementById("sidebar-filter-input"),

        // Command Palette
        cmdKBtn: document.getElementById("cmd-k-btn"),
        cmdKModal: document.getElementById("cmd-k-modal"),
        cmdKInput: document.getElementById("cmd-k-input"),
        cmdKResults: document.getElementById("cmd-k-results"),

        // Breadcrumbs
        crumbCourse: document.getElementById("crumb-course"),
        crumbClass: document.getElementById("crumb-class"),
        crumbStep: document.getElementById("crumb-step"),

        // Stepper gates
        gatePills: document.querySelectorAll(".step-gate-pill"),
        tabPanes: document.querySelectorAll(".tab-pane"),
        
        // Paso 1: Quiz & Concept
        theoryText: document.getElementById("theory-text"),
        quizQuestionText: document.getElementById("quiz-question-text"),
        quizOptionsGrid: document.getElementById("quiz-options-grid"),
        quizFeedbackBox: document.getElementById("quiz-feedback-box"),
        quizStatusBadge: document.getElementById("quiz-status-badge"),
        mermaidBox: document.getElementById("mermaid-render-box"),
        expandMermaidBtn: document.getElementById("expand-mermaid-btn"),
        confirmConceptBtn: document.getElementById("confirm-concept-btn"),

        // Paso 2: Demo & Pythonic Diff
        demoCode: document.getElementById("demo-code-area"),
        demoLines: document.getElementById("demo-lines"),
        demoTerm: document.getElementById("demo-terminal"),
        demoRuntimeBadge: document.getElementById("demo-runtime-badge"),
        antipatternCode: document.getElementById("antipattern-code"),
        pythonicCode: document.getElementById("pythonic-code"),
        runDemoBtn: document.getElementById("run-demo-btn"),
        copyDemoBtn: document.getElementById("copy-demo-btn"),

        // Paso 3: Arenero & RAM
        sandboxCode: document.getElementById("sandbox-code-area"),
        sandboxLines: document.getElementById("sandbox-lines"),
        sandboxTerm: document.getElementById("sandbox-terminal"),
        sandboxSnippetsSelect: document.getElementById("sandbox-snippets-select"),
        formatSandboxBtn: document.getElementById("format-sandbox-btn"),
        runSandboxBtn: document.getElementById("run-sandbox-btn"),
        resetSandboxBtn: document.getElementById("reset-sandbox-btn"),
        clearSandboxBtn: document.getElementById("clear-sandbox-btn"),
        memoryCanvas: document.getElementById("memory-canvas"),
        memTotalCount: document.getElementById("mem-total-count"),

        // Paso 4: Reto & Formatter
        challengePrompt: document.getElementById("challenge-prompt-text"),
        challengeCode: document.getElementById("challenge-code-area"),
        challengeLines: document.getElementById("challenge-lines"),
        challengeResults: document.getElementById("challenge-results-box"),
        formatChallengeBtn: document.getElementById("format-challenge-btn"),
        evalChallengeBtn: document.getElementById("eval-challenge-btn"),
        resetChallengeBtn: document.getElementById("reset-challenge-btn"),
        downloadSolutionBtn: document.getElementById("download-solution-btn"),
        diffStatusLabel: document.getElementById("diff-status-label"),
        hintsAccordion: document.getElementById("hints-accordion"),
        askMentorModalBtn: document.getElementById("ask-mentor-modal-btn"),

        // Footer
        prevBtn: document.getElementById("prev-class-btn"),
        nextBtn: document.getElementById("next-class-btn"),
        classStatusSummary: document.getElementById("class-status-summary"),

        // Certificado, Logros, Chat & Perfil
        certModal: document.getElementById("cert-modal"),
        openCertBtn: document.getElementById("open-cert-btn"),
        headerLinkedinBtn: document.getElementById("header-linkedin-btn"),
        certModalLinkedinBtn: document.getElementById("cert-modal-linkedin-btn"),
        closeCertBtn: document.getElementById("close-cert-btn"),
        studentNameInput: document.getElementById("student-name-input"),
        certCourseSelect: document.getElementById("cert-course-select"),
        certPreviewFrame: document.getElementById("cert-preview-frame"),
        refreshCertBtn: document.getElementById("refresh-cert-btn"),
        copyBadgeBtn: document.getElementById("copy-badge-btn"),
        downloadCertBtn: document.getElementById("download-cert-btn"),
        downloadCertPngBtn: document.getElementById("download-cert-png-btn"),

        // Class Diploma Modal
        classCertModal: document.getElementById("class-cert-modal"),
        closeClassCertBtn: document.getElementById("close-class-cert-btn"),
        classCertStudentName: document.getElementById("class-cert-student-name"),
        updateClassCertBtn: document.getElementById("update-class-cert-btn"),
        classCertPreviewFrame: document.getElementById("class-cert-preview-frame"),
        classCertLinkedinText: document.getElementById("class-cert-linkedin-text"),
        copyLinkedinPostBtn: document.getElementById("copy-linkedin-post-btn"),
        downloadClassPngQuickBtn: document.getElementById("download-class-png-quick-btn"),
        linkedinShareGuideToast: document.getElementById("linkedin-share-guide-toast"),
        shareTwitterBtn: document.getElementById("share-twitter-btn"),
        shareWhatsappBtn: document.getElementById("share-whatsapp-btn"),
        downloadClassPdfBtn: document.getElementById("download-class-pdf-btn"),
        downloadClassPngBtn: document.getElementById("download-class-png-btn"),
        shareLinkedinDirectBtn: document.getElementById("share-linkedin-direct-btn"),
        shareLinkedinInlineBtn: document.getElementById("share-linkedin-inline-btn"),
        openLinkedinTopBtn: document.getElementById("open-linkedin-top-btn"),
        nextClassCertBtn: document.getElementById("next-class-cert-btn"),

        achievementsBtn: document.getElementById("achievements-btn"),
        achievementsModal: document.getElementById("achievements-modal"),
        closeAchievementsBtn: document.getElementById("close-achievements-btn"),
        achievementsGrid: document.getElementById("achievements-grid"),
        askMentorModal: document.getElementById("ask-mentor-modal"),
        closeAskMentorBtn: document.getElementById("close-ask-mentor-btn"),
        mentorChatHistory: document.getElementById("mentor-chat-history"),
        mentorChatInput: document.getElementById("mentor-chat-input"),
        sendMentorChatBtn: document.getElementById("send-mentor-chat-btn"),
        profileModal: document.getElementById("profile-modal"),
        closeProfileBtn: document.getElementById("close-profile-btn"),
        avatarPickerRow: document.getElementById("avatar-picker-row"),
        profileNameInput: document.getElementById("profile-name-input"),
        profileEmailInput: document.getElementById("profile-email-input"),
        saveProfileBtn: document.getElementById("save-profile-btn"),
        resetProgressBtn: document.getElementById("reset-progress-btn"),

        // Embedded Docs Split Panel
        toggleDocsDrawerBtn: document.getElementById("toggle-docs-drawer-btn"),
        docsSplitPanel: document.getElementById("docs-split-panel"),
        docsIframe: document.getElementById("docs-iframe"),
        docsFrameClassBadge: document.getElementById("docs-frame-class-badge"),
        reloadDocsFrameBtn: document.getElementById("reload-docs-frame-btn"),
        openDocsExtBtn: document.getElementById("open-docs-ext-btn"),
        closeDocsDrawerBtn: document.getElementById("close-docs-drawer-btn"),
        docsResizeHandle: document.getElementById("docs-resize-handle"),

        // Slide Deck & Reto Disk
        saveRetoDiskBtn: document.getElementById("save-reto-disk-btn"),
        slideDeckBtn: document.getElementById("slide-deck-btn"),
        slideDeckModal: document.getElementById("slide-deck-modal"),
        closeSlideDeckBtn: document.getElementById("close-slide-deck-btn"),
        slideDeckBody: document.getElementById("slide-deck-body"),
        slideDeckTitle: document.getElementById("slide-deck-title"),
        slideCurrentNum: document.getElementById("slide-current-num"),
        slidePrevBtn: document.getElementById("slide-prev-btn"),
        slideNextBtn: document.getElementById("slide-next-btn"),
        slideFsBtn: document.getElementById("slide-fs-btn")
      };

      function updateLineNumbers(textarea, gutter) {
        if (!textarea || !gutter) return;
        const lines = textarea.value.split("\\n").length;
        gutter.innerHTML = Array.from({ length: lines }, (_, i) => i + 1).join("<br>");
      }

      function setupEditorEnhancements(textarea, gutter) {
        if (!textarea) return;
        updateLineNumbers(textarea, gutter);
        textarea.addEventListener("input", () => updateLineNumbers(textarea, gutter));
        textarea.addEventListener("scroll", () => {
          if (gutter) gutter.scrollTop = textarea.scrollTop;
        });
        textarea.addEventListener("keydown", (e) => {
          if (e.key === "Tab") {
            e.preventDefault();
            const start = textarea.selectionStart;
            const end = textarea.selectionEnd;
            textarea.value = textarea.value.substring(0, start) + "    " + textarea.value.substring(end);
            textarea.selectionStart = textarea.selectionEnd = start + 4;
            updateLineNumbers(textarea, gutter);
          }
        });
      }

      async function initApp() {
        setupEvents();
        setupEditorEnhancements(dom.demoCode, dom.demoLines);
        setupEditorEnhancements(dom.sandboxCode, dom.sandboxLines);
        setupEditorEnhancements(dom.challengeCode, dom.challengeLines);
        
        // Detectar Query Params para Integración Híbrida y Modo Tutor
        const urlParams = new URLSearchParams(window.location.search);
        const isTutorUrl = urlParams.get('mode') === 'tutor' || 
                           urlParams.get('mode') === 'presenter' || 
                           window.location.pathname === '/tutor' || 
                           window.location.pathname === '/presenter';
                           
        if (isTutorUrl) {
          setTutorMode(true);
        }

        await fetchProfile();
        await fetchCurriculum();

        const urlCourse = urlParams.get('course');
        const urlClass = urlParams.get('class') || urlParams.get('class_num');
        const targetCourse = urlCourse ? parseInt(urlCourse) : ((state.profile && state.profile.current_course) ? state.profile.current_course : 1);
        const targetClass = urlClass ? parseInt(urlClass) : ((state.profile && state.profile.current_class) ? state.profile.current_class : 1);

        await loadClass(targetCourse, targetClass);
      }

      function setTutorMode(enable) {
        state.isTutorMode = enable;
        document.querySelectorAll(".tutor-only").forEach(el => {
          el.style.display = enable ? "inline-flex" : "none";
        });
        if (dom.toggleModeBtn) {
          if (enable) {
            dom.toggleModeBtn.style.background = "rgba(2, 132, 199, 0.25)";
            dom.toggleModeBtn.style.borderColor = "#38bdf8";
            dom.toggleModeBtn.style.color = "#7dd3fc";
            dom.modeBtnIcon.textContent = "👨‍💻";
            dom.modeBtnText.textContent = "Modo Estudiante";
            setMentorSpeech("👑 **Modo Presentador Activo:** Tienes acceso maestro a las 32 clases sin restricciones para impartir tu clase magistral en vivo.");
          } else {
            dom.toggleModeBtn.style.background = "rgba(168, 85, 247, 0.2)";
            dom.toggleModeBtn.style.borderColor = "#a855f7";
            dom.toggleModeBtn.style.color = "#d8b4fe";
            dom.modeBtnIcon.textContent = "👨‍🏫";
            dom.modeBtnText.textContent = "Modo Presentador";
            setMentorSpeech("Modo Estudiante activo. Completa cada paso y supera los retos para ganar XP.");
          }
        }
        renderTree();
        if (state.classContent) {
          renderClass(state.classContent);
        }
      }

      function toggleProjectorMode() {
        state.isProjectorMode = !state.isProjectorMode;
        document.body.classList.toggle("projector-mode", state.isProjectorMode);
        dom.projectorModeBtn.style.borderColor = state.isProjectorMode ? "#34d399" : "#38bdf8";
        dom.projectorModeBtn.textContent = state.isProjectorMode ? "📺 Normal" : "📺 Proyector";
        soundClick();
      }

      function toggleDocsDrawer(forceState = null) {
        state.docsDrawerOpen = (forceState !== null) ? forceState : !state.docsDrawerOpen;
        if (dom.docsSplitPanel) {
          dom.docsSplitPanel.classList.toggle("hidden", !state.docsDrawerOpen);
        }
        if (dom.toggleDocsDrawerBtn) {
          dom.toggleDocsDrawerBtn.style.background = state.docsDrawerOpen ? "rgba(56, 189, 248, 0.35)" : "rgba(56, 189, 248, 0.15)";
          dom.toggleDocsDrawerBtn.style.borderColor = state.docsDrawerOpen ? "#38bdf8" : "rgba(56, 189, 248, 0.4)";
        }
        syncDocsIframe();
        soundClick();
      }

      function syncDocsIframe() {
        if (!dom.docsIframe) return;
        const cStr = state.currentCourse.toString().padStart(2, '0');
        const sStr = state.currentClass.toString().padStart(2, '0');
        const targetUrl = `https://academy_python.wisrovi.dev/curso-${cStr}/clase-${sStr}/`;
        if (dom.docsIframe.src !== targetUrl && state.docsDrawerOpen) {
          dom.docsIframe.src = targetUrl;
        }
        if (dom.docsFrameClassBadge) {
          dom.docsFrameClassBadge.textContent = `C${state.currentCourse}-S${sStr}`;
        }
      }

      function updateTimerDisplay() {
        const mins = Math.floor(state.timerSecondsRemaining / 60);
        const secs = state.timerSecondsRemaining % 60;
        dom.classroomTimerDisplay.textContent = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
      }

      function startClassroomTimer() {
        if (state.timerIsRunning) return;
        state.timerIsRunning = true;
        dom.timerToggleBtn.textContent = "⏸️ Pausar";
        dom.timerToggleBtn.className = "btn btn-secondary";
        soundClick();
        
        state.timerInterval = setInterval(() => {
          if (state.timerSecondsRemaining > 0) {
            state.timerSecondsRemaining--;
            updateTimerDisplay();
            if (state.timerSecondsRemaining === 0) {
              clearInterval(state.timerInterval);
              state.timerIsRunning = false;
              dom.timerToggleBtn.textContent = "▶️ Iniciar";
              dom.timerToggleBtn.className = "btn btn-primary";
              soundVictory();
              if (window.confetti) confetti({ particleCount: 200, spread: 120, origin: { y: 0.5 } });
              alert("⏱️ ¡TIEMPO CONCLUIDO! El plazo para el reto de aula ha finalizado.");
            }
          }
        }, 1000);
      }

      function pauseClassroomTimer() {
        if (!state.timerIsRunning) return;
        clearInterval(state.timerInterval);
        state.timerIsRunning = false;
        dom.timerToggleBtn.textContent = "▶️ Reanudar";
        dom.timerToggleBtn.className = "btn btn-primary";
        soundClick();
      }

      function resetClassroomTimer(secs = 600) {
        pauseClassroomTimer();
        state.timerSecondsRemaining = secs;
        updateTimerDisplay();
        dom.timerToggleBtn.textContent = "▶️ Iniciar";
        dom.timerToggleBtn.className = "btn btn-primary";
      }

      async function fetchProfile() {
        try {
          const res = await fetch("/api/progress");
          const data = await res.json();
          state.profile = data;
          updateProfileUI();
        } catch (e) { console.error(e); }
      }

      function updateProfileUI() {
        if (!state.profile) return;
        const p = state.profile;
        dom.levelTitle.textContent = `Nv. ${p.level} ${p.level_title.split(' ')[1] || 'Aprendiz'}`;
        dom.xpVal.textContent = p.xp;
        dom.streak.textContent = `${p.streak_days} Días`;
        dom.avatarBtn.textContent = p.avatar || "👨‍💻";
        if (dom.studentNameInput) dom.studentNameInput.value = p.name;
        if (dom.profileNameInput) dom.profileNameInput.value = p.name;
        if (dom.profileEmailInput) dom.profileEmailInput.value = p.email;
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
          dom.progressPill.textContent = `${data.progress_percent}% Completado (${data.completed_count}/32)`;
          renderTree();
        } catch (e) { console.error(e); }
      }

      function isClassUnlocked(courseNum, classNum) {
        if (state.isTutorMode) return true; // ¡Acceso Maestro Total en Modo Presentador!
        const key = `${courseNum}-${classNum}`;
        if (courseNum === 1 && classNum === 1) return true;
        const completed = new Set(state.profile ? state.profile.completed_classes : []);
        if (completed.has(key)) return true; // Lección ya completada: siempre accesible para repasar y practicar!
        if (classNum > 1) {
          return completed.has(`${courseNum}-${classNum - 1}`);
        }
        if (classNum === 1 && courseNum > 1) {
          return completed.has(`${courseNum - 1}-8`);
        }
        return false;
      }

      function isCourseUnlocked(courseNum) {
        if (state.isTutorMode) return true; // ¡Todos los cursos desbloqueados para el docente!
        if (courseNum === 1) return true;
        const completed = new Set(state.profile ? state.profile.completed_classes : []);
        return completed.has(`${courseNum - 1}-8`);
      }

      function renderTree(filterQuery = "") {
        dom.classTree.innerHTML = "";
        const courses = [
          { id: 1, name: "Curso 1: Fundamentos Básicos" },
          { id: 2, name: "Curso 2: Algoritmos & Estructuras" },
          { id: 3, name: "Curso 3: Agentes de Inteligencia Artificial" },
          { id: 4, name: "Curso 4: Proyecto Integrador Full-Stack" }
        ];

        const q = filterQuery.toLowerCase().trim();

        courses.forEach(c => {
          const courseUnlocked = isCourseUnlocked(c.id);
          let courseClasses = state.curriculum.filter(cls => cls.course_num === c.id);
          if (q) {
            courseClasses = courseClasses.filter(cls => cls.title.toLowerCase().includes(q) || (cls.key && cls.key.includes(q)));
          }
          if (q && courseClasses.length === 0) return;

          const grp = document.createElement("div");
          grp.className = "course-section";
          const lockHeaderTag = courseUnlocked ? "" : " <span style='font-size:0.68rem; color:#f87171; font-weight:700;'>🔒 Bloqueado</span>";
          grp.innerHTML = `<div class="course-header"><span>${c.name}</span>${lockHeaderTag}</div>`;

          courseClasses.forEach(cls => {
            const item = document.createElement("div");
            const isActive = (cls.course_num === state.currentCourse && cls.class_num === state.currentClass);
            const unlocked = isClassUnlocked(cls.course_num, cls.class_num);
            const isCompleted = state.profile && state.profile.completed_classes && state.profile.completed_classes.includes(cls.key);
            
            item.className = `class-item ${isActive ? 'active' : ''} ${isCompleted ? 'completed' : ''} ${!unlocked ? 'locked' : ''}`;
            const boss = cls.boss_battle ? "⚔️ " : "";
            
            let statusTag = "🔒 Bloqueada";
            if (state.isTutorMode) {
              statusTag = "👑 Docente";
            } else if (isCompleted) {
              statusTag = "✓ Repasar";
            } else if (unlocked) {
              statusTag = "🚀 Activa";
            }
            
            item.innerHTML = `
              <span>${boss}S${cls.class_num.toString().padStart(2, '0')}: ${cls.title.split(':')[1] || cls.title}</span>
              <span class="item-status-icon" style="font-size:0.68rem;">${statusTag}</span>
            `;

            if (unlocked) {
              item.addEventListener("click", () => {
                soundClick();
                loadClass(cls.course_num, cls.class_num);
              });
            } else {
              item.addEventListener("click", () => {
                soundError();
                const prevDesc = cls.class_num > 1 
                  ? `Clase 0${cls.class_num - 1} del Curso ${cls.course_num}` 
                  : `Clase 08 del Curso ${cls.course_num - 1}`;
                alert(`🔒 Lección Bloqueada:\n\nNo puedes adelantar clases sin haber superado las anteriores.\nPara acceder a la Clase 0${cls.class_num}, primero debes completar y superar la ${prevDesc}.`);
              });
            }

            grp.appendChild(item);
          });
          dom.classTree.appendChild(grp);
        });

        // Actualizar visual de los Course Tabs
        document.querySelectorAll(".course-tab-btn").forEach(btn => {
          const cId = parseInt(btn.dataset.course);
          const cUnlocked = isCourseUnlocked(cId);
          if (!cUnlocked) {
            btn.style.opacity = "0.5";
            btn.title = `🔒 Curso ${cId} Bloqueado. Completa el Curso ${cId - 1} primero.`;
          } else {
            btn.style.opacity = "1";
            btn.title = `Curso ${cId} Disponible`;
          }
        });
      }

      async function loadClass(courseNum, classNum) {
        state.currentCourse = courseNum;
        state.currentClass = classNum;
        state.classStartTime = Date.now();
        
        // Actualizar tabs superiores
        document.querySelectorAll(".course-tab-btn").forEach(btn => {
          btn.classList.toggle("active", parseInt(btn.dataset.course) === courseNum);
        });

        const key = `${courseNum}-${classNum}`;
        const isDone = state.profile && state.profile.completed_classes && state.profile.completed_classes.includes(key);
        state.stepsCompleted = { 1: isDone || state.isTutorMode, 2: isDone || state.isTutorMode, 3: isDone || state.isTutorMode, 4: isDone || state.isTutorMode };

        try {
          const url = state.isTutorMode ? `/api/tutor/class/${courseNum}/${classNum}` : `/api/class/${courseNum}/${classNum}`;
          const res = await fetch(url);
          const data = await res.json();
          state.classContent = data;
          renderClass(data);
          updateStepperUI();
          renderTree();
          syncDocsIframe();
          switchStep(1);
          if (state.isTutorMode) {
            setMentorSpeech(`👑 **Modo Presentador:** Impartiendo **Curso ${courseNum} - Clase 0${classNum}**. Usa el live coding o abre las Notas Docente.`);
          } else if (isDone) {
            setMentorSpeech(`🔄 **Modo Repaso:** Estás practicando la **Clase C${courseNum}-S0${classNum}**. Puedes volver a ejecutar ejemplos, inspeccionar memoria y reevaluar retos sin límites.`);
          } else {
            setMentorSpeech(`Estás en el **Curso ${courseNum} - Clase 0${classNum}**. Analiza el concepto y responde el Micro-Quiz para ganar XP.`);
          }
        } catch (e) { console.error(e); }
      }

      function setMentorSpeech(text) {
        dom.floatingSpeech.innerHTML = `👨‍🏫 ${text}`;
      }

      function renderClass(data) {
        const key = `${data.course_num}-${data.class_num}`;
        const isCompleted = state.profile && state.profile.completed_classes && state.profile.completed_classes.includes(key);

        dom.courseName.textContent = data.course_name;
        dom.crumbCourse.textContent = data.course_name;
        dom.lessonTitle.textContent = data.title;
        dom.crumbClass.textContent = `Clase 0${data.class_num}`;
        dom.metaphor.textContent = `Metáfora Central: «${data.metaphor}»`;
        dom.bossBadge.style.display = data.boss_battle ? "inline-block" : "none";

        if (dom.modeBadge) {
          if (state.isTutorMode) {
            dom.modeBadge.className = "tag-mode tag-presenter";
            dom.modeBadge.textContent = "👑 Modo Presentador / Docente en Vivo";
          } else if (isCompleted) {
            dom.modeBadge.className = "tag-mode tag-review";
            dom.modeBadge.textContent = "🔄 Modo Repaso (Lección Superada)";
          } else {
            dom.modeBadge.className = "tag-mode tag-active";
            dom.modeBadge.textContent = "🚀 Lección Activa en Curso";
          }
        }

        // Renderizar Speaker Notes para el docente
        if (dom.speakerNotesBody) {
          const notes = data.speaker_notes || {
            metaphor_story: `Presenta la metáfora: «${data.metaphor}». Conecta los conceptos con ejemplos tangibles antes de abrir el código.`,
            interactive_questions: [
              `¿Cómo visualizan el flujo en memoria para «${data.title}»?`,
              "¿Por qué es preferible usar tipado estricto frente a tipado dinámico implícito?",
              "¿Qué caso borde creen que rompería este algoritmo si no validamos las entradas?"
            ],
            common_pitfalls: (data.pythonic_tip && data.pythonic_tip.antipattern) ? data.pythonic_tip.antipattern : "Escribir código sin validar las aserciones de entrada."
          };
          
          dom.speakerNotesBody.innerHTML = `
            <div class="speaker-notes-section">
              <div class="speaker-notes-title">📖 Narrativa de la Metáfora Central</div>
              <p style="font-size:0.86rem; color:#e2e8f0; line-height:1.5;">${notes.metaphor_story}</p>
            </div>
            <div class="speaker-notes-section">
              <div class="speaker-notes-title">❓ Preguntas Socráticas para Lanzar a la Clase</div>
              <ul style="padding-left:1.2rem; font-size:0.84rem; color:#cbd5e1; display:flex; flex-direction:column; gap:0.4rem;">
                ${notes.interactive_questions.map(q => `<li>${q}</li>`).join("")}
              </ul>
            </div>
            <div class="speaker-notes-section" style="border-color: rgba(239, 68, 68, 0.4);">
              <div class="speaker-notes-title" style="color: #f87171;">⚠️ Antipatrón / Trampa Común a Advertir</div>
              <pre style="background:#020612; padding:0.5rem; border-radius:4px; font-family:var(--font-code); font-size:0.8rem; color:#fca5a5; overflow-x:auto;">${notes.common_pitfalls}</pre>
            </div>
          `;
        }

        if (dom.timerChallengeTitle) {
          dom.timerChallengeTitle.textContent = `${data.title} - Reto Práctico`;
        }

        dom.theoryText.innerHTML = data.theory.replace(/\\n/g, "<br>");
        renderMermaid(data.mermaid);

        // Render Micro-Quiz
        renderQuiz(data);

        // Render Pythonic Tips
        renderPythonicTip(data);

        state.starterDemoCode = data.demo_code;
        dom.demoCode.value = data.demo_code;
        updateLineNumbers(dom.demoCode, dom.demoLines);
        dom.demoTerm.innerHTML = "&gt; Presiona 'Ejecutar Demo' o usa Ctrl+Enter para compilar y validar el paso 2.";
        dom.demoRuntimeBadge.textContent = "";

        state.starterSandboxCode = data.playground_code;
        dom.sandboxCode.value = data.playground_code;
        updateLineNumbers(dom.sandboxCode, dom.sandboxLines);
        dom.sandboxTerm.innerHTML = "&gt; Modifica variables y pulsa 'Inspeccionar RAM' para el paso 3.";
        dom.memoryCanvas.innerHTML = `<div class="empty-state">Ejecuta código para visualizar las variables en la memoria RAM.</div>`;
        dom.memTotalCount.textContent = "0 Variables";

        dom.challengePrompt.textContent = data.challenge_prompt;
        state.starterChallengeCode = data.challenge_starter;
        dom.challengeCode.value = data.challenge_starter;
        updateLineNumbers(dom.challengeCode, dom.challengeLines);
        updateDiffStatus();
        if (data.is_completed) {
          dom.challengeResults.innerHTML = `
            <div style="background: rgba(16,185,129,0.18); border: 1px solid #10b981; color: #6ee7b7; padding: 0.75rem 1rem; border-radius: 8px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem;">
              <div>
                🎉 <strong>¡Lección Superada con Éxito!</strong>
                <div style="font-size:0.8rem; color:#a7f3d0; margin-top:0.2rem;">Tu micro-diploma oficial está listo para compartir en LinkedIn.</div>
              </div>
              <button class="btn" id="open-class-cert-from-challenge-btn" style="background:#0a66c2; color:#fff; border:none; font-weight:800; font-size:0.85rem; padding:0.45rem 0.9rem; border-radius:6px; display:inline-flex; align-items:center; gap:0.4rem; cursor:pointer; box-shadow:0 0 12px rgba(10,102,194,0.5);">
                <span>🚀</span> Publicar en LinkedIn
              </button>
            </div>
          `;
          setTimeout(() => {
            const b = document.getElementById("open-class-cert-from-challenge-btn");
            if (b) b.addEventListener("click", () => openClassCertForCurrent());
          }, 50);
        } else {
          dom.challengeResults.innerHTML = `<div style="color: #64748b; font-size: 0.85rem; font-style: italic;">Modifica la plantilla y pulsa 'Evaluar Reto'.</div>`;
        }

        // Cargar borrador persistente de localStorage si existe
        try {
          const draftKey = `wisrovi_draft_${state.currentCourse}_${state.currentClass}`;
          const savedDraft = localStorage.getItem(draftKey);
          if (savedDraft) {
            const draft = JSON.parse(savedDraft);
            if (draft.challenge) {
              dom.challengeCode.value = draft.challenge;
              updateLineNumbers(dom.challengeCode, dom.challengeLines);
              updateDiffStatus();
            }
          }
        } catch (e) {}

        dom.hintsAccordion.innerHTML = "";
        data.socratic_hints.forEach((h, idx) => {
          const d = document.createElement("details");
          d.style.cssText = "background: rgba(15, 23, 42, 0.9); border: 1px solid var(--border-glass); border-radius: 8px; padding: 0.6rem 0.85rem; font-size: 0.84rem; color: #cbd5e1; cursor: pointer;";
          d.innerHTML = `<summary style="font-weight: 700; color: #38bdf8;">💡 Pista ${idx + 1}</summary><p style="margin-top: 0.4rem;">${h}</p>`;
          dom.hintsAccordion.appendChild(d);
        });
      }

      function renderQuiz(data) {
        dom.quizOptionsGrid.innerHTML = "";
        dom.quizFeedbackBox.style.display = "none";
        
        // Quizzes predeterminados por clase
        const qText = `¿Cuál es el propósito central de la ${data.title.split(':')[0]}?`;
        dom.quizQuestionText.textContent = `❓ Auto-Evaluación Conceptual (+25 XP): ${data.metaphor.split('(')[0]}`;
        
        const defaultOptions = [
          { text: "Optimizar el flujo y cumplir contratos de tipado", correct: true, exp: "Exacto: la arquitectura limpia se basa en tipado y diseño modular." },
          { text: "Ejecutar bucles infinitos sin control", correct: false, exp: "Incorrecto: los bucles deben tener condiciones deterministas." },
          { text: "Descartar los errores sin analizarlos", correct: false, exp: "Incorrecto: las excepciones deben gestionarse adecuadamente." },
          { text: "Duplicar variables sin considerar el Heap", correct: false, exp: "Incorrecto: el uso eficiente de memoria es clave." }
        ];

        defaultOptions.forEach((opt, idx) => {
          const btn = document.createElement("button");
          btn.className = "quiz-opt-btn";
          btn.textContent = `${['A', 'B', 'C', 'D'][idx]}) ${opt.text}`;
          btn.addEventListener("click", () => {
            if (opt.correct) {
              btn.classList.add("correct");
              dom.quizFeedbackBox.style.display = "block";
              dom.quizFeedbackBox.style.background = "rgba(16,185,129,0.2)";
              dom.quizFeedbackBox.innerHTML = `✅ <strong>¡Correcto (+25 XP)!</strong> ${opt.exp}`;
              soundChime();
            } else {
              btn.classList.add("wrong");
              dom.quizFeedbackBox.style.display = "block";
              dom.quizFeedbackBox.style.background = "rgba(239,68,68,0.2)";
              dom.quizFeedbackBox.innerHTML = `❌ <strong>Respuesta Incorrecta:</strong> ${opt.exp}`;
              soundError();
            }
          });
          dom.quizOptionsGrid.appendChild(btn);
        });
      }

      function renderPythonicTip(data) {
        if (data.pythonic_tip && data.pythonic_tip.antipattern && data.pythonic_tip.pythonic) {
          dom.antipatternCode.textContent = data.pythonic_tip.antipattern;
          dom.pythonicCode.textContent = data.pythonic_tip.pythonic;
        } else if (data.course_num === 1) {
          dom.antipatternCode.textContent = `if condicion == True:\n    return 'valido'\nelse:\n    return 'invalido'`;
          dom.pythonicCode.textContent = `return 'valido' if condicion else 'invalido'`;
        } else if (data.course_num === 2) {
          dom.antipatternCode.textContent = `cola = []\ncola.append(x)\natendido = cola.pop(0)  # O(N) Ineficiente`;
          dom.pythonicCode.textContent = `from collections import deque\ncola = deque([x])\natendido = cola.popleft()  # O(1) Óptimo`;
        } else if (data.course_num === 3) {
          dom.antipatternCode.textContent = `raw_dict = {'score': '95'}\n# Acceso inseguro sin esquema`;
          dom.pythonicCode.textContent = `class Item(BaseModel):\n    score: float\nitem = Item.model_validate_json(payload)`;
        } else {
          dom.antipatternCode.textContent = `# Módulo gigante monolítico\ndef todo_en_uno(): pass`;
          dom.pythonicCode.textContent = `# Capas limpias: API -> Services -> Models\nfrom fastapi import Depends, APIRouter`;
        }
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

      function updateDiffStatus() {
        const isModified = dom.challengeCode.value.trim() !== state.starterChallengeCode.trim();
        if (isModified) {
          dom.diffStatusLabel.textContent = "✓ Código modificado (Listo para evaluar)";
          dom.diffStatusLabel.style.color = "#34d399";
        } else {
          dom.diffStatusLabel.textContent = "⚠️ Modifica el código antes de evaluar";
          dom.diffStatusLabel.style.color = "#fb923c";
        }
      }

      function updateStepperUI() {
        const key = `${state.currentCourse}-${state.currentClass}`;
        const isClassAlreadyCompleted = state.profile && state.profile.completed_classes && state.profile.completed_classes.includes(key);

        dom.gatePills.forEach(pill => {
          const s = parseInt(pill.dataset.step);
          const isDone = state.stepsCompleted[s] || isClassAlreadyCompleted;
          pill.classList.toggle("done", isDone);
          const statusElem = document.getElementById(`status-step-${s}`);
          if (statusElem) {
            statusElem.textContent = isDone ? "✓ Hecho" : "Pendiente";
          }
        });

        const allDone = state.isTutorMode || Object.values(state.stepsCompleted).every(Boolean) || isClassAlreadyCompleted;
        dom.nextBtn.disabled = !allDone;
        if (state.isTutorMode) {
          dom.classStatusSummary.innerHTML = "<span style='color:#c084fc; font-weight:800;'>👑 Modo Presentador / Docente en Vivo: Acceso Maestro sin bloqueos. Navega libremente entre las 32 clases.</span>";
        } else if (isClassAlreadyCompleted) {
          dom.classStatusSummary.innerHTML = "<span style='color:#34d399; font-weight:800;'>🔄 Modo Repaso y Práctica: Clase superada previamente. Puedes repasar libremente o avanzar.</span>";
        } else if (allDone) {
          dom.classStatusSummary.innerHTML = "<span style='color:#34d399; font-weight:800;'>🎉 ¡Clase completada! Puedes avanzar a la siguiente lección.</span>";
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
        
        const stepLabels = { 1: "Paso 1: Concepto & Quiz", 2: "Paso 2: Demo & Pythonic", 3: "Paso 3: Arenero & RAM", 4: "Paso 4: Reto Evaluado" };
        dom.crumbStep.textContent = stepLabels[num] || `Paso ${num}`;

        const msgs = {
          1: "Analiza el concepto y responde el Micro-Quiz para asegurar tu comprensión.",
          2: "Presiona 'Ejecutar Demo' o usa Ctrl+Enter y revisa los patrones idiomáticos.",
          3: "Experimenta libremente en el Arenero y dale clic a 'Formatear (PEP 8)' si lo deseas.",
          4: "Escribe tu solución, supera las pruebas unitarias y gana +150 XP."
        };
        if (msgs[num]) setMentorSpeech(msgs[num]);
      }

      async function autoFormatCode(textarea, gutter) {
        soundClick();
        try {
          const res = await fetch("/api/format-code", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: textarea.value })
          });
          const data = await res.json();
          if (data.success) {
            textarea.value = data.formatted_code;
            updateLineNumbers(textarea, gutter);
            soundChime();
          } else {
            alert(`⚠️ Error de sintaxis al formatear: ${data.error}`);
          }
        } catch (e) { console.error(e); }
      }

      function setupEvents() {
        // Theme selector
        dom.themeSelector.addEventListener("change", (e) => {
          document.documentElement.setAttribute("data-theme", e.target.value);
        });

        // Course Tab buttons
        document.querySelectorAll(".course-tab-btn").forEach(btn => {
          btn.addEventListener("click", () => {
            const c = parseInt(btn.dataset.course);
            if (!isCourseUnlocked(c)) {
              soundError();
              alert(`🔒 Curso ${c} Bloqueado:\n\nPara acceder a este módulo, primero debes completar las 8 clases del Curso ${c - 1}.`);
              return;
            }
            soundClick();
            loadClass(c, 1);
          });
        });

        // Sidebar toggle & filter
        dom.toggleSidebarBtn.addEventListener("click", () => {
          state.sidebarCollapsed = !state.sidebarCollapsed;
          dom.appSidebar.classList.toggle("collapsed", state.sidebarCollapsed);
        });

        dom.sidebarFilterInput.addEventListener("input", (e) => {
          renderTree(e.target.value);
        });

        dom.gatePills.forEach(pill => {
          pill.addEventListener("click", () => switchStep(parseInt(pill.dataset.step)));
        });

        // Auto-Formatters
        dom.formatSandboxBtn.addEventListener("click", () => autoFormatCode(dom.sandboxCode, dom.sandboxLines));
        dom.formatChallengeBtn.addEventListener("click", () => autoFormatCode(dom.challengeCode, dom.challengeLines));

        // Paso 1
        dom.confirmConceptBtn.addEventListener("click", () => {
          state.stepsCompleted[1] = true;
          soundChime();
          updateStepperUI();
          switchStep(2);
        });

        // Paso 2
        dom.runDemoBtn.addEventListener("click", async () => {
          soundClick();
          dom.demoTerm.innerHTML = "&gt; Compilando y ejecutando demo...";
          const t0 = performance.now();
          const res = await fetch("/api/run-code", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: dom.demoCode.value })
          });
          const data = await res.json();
          const elapsed = Math.round(performance.now() - t0);
          dom.demoRuntimeBadge.textContent = `⚡ ${elapsed}ms`;
          dom.demoTerm.innerHTML = `&gt; ${data.stdout || data.stderr || 'Demo ejecutado con éxito.'}`;
          state.stepsCompleted[2] = true;
          soundChime();
          updateStepperUI();
        });

        dom.copyDemoBtn.addEventListener("click", () => {
          navigator.clipboard.writeText(dom.demoCode.value);
          alert("¡Código de demostración copiado al portapapeles!");
        });

        // Paso 3
        dom.runSandboxBtn.addEventListener("click", async () => {
          soundClick();
          dom.sandboxTerm.innerHTML = "&gt; Inspeccionando estado del Heap y Stack en RAM...";
          const res = await fetch("/api/run-code", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: dom.sandboxCode.value })
          });
          const data = await res.json();
          dom.sandboxTerm.innerHTML = `&gt; ${data.stdout || data.stderr || 'Ejecutado.'}`;
          renderMemoryDual(data.memory_variables);
          state.stepsCompleted[3] = true;
          soundChime();
          updateStepperUI();
        });

        dom.resetSandboxBtn.addEventListener("click", () => {
          dom.sandboxCode.value = state.starterSandboxCode;
          updateLineNumbers(dom.sandboxCode, dom.sandboxLines);
          dom.sandboxTerm.innerHTML = "&gt; Código del arenero restaurado.";
        });

        dom.clearSandboxBtn.addEventListener("click", () => {
          dom.sandboxCode.value = "";
          updateLineNumbers(dom.sandboxCode, dom.sandboxLines);
          dom.sandboxTerm.innerHTML = "&gt; Arenero limpio. Escribe tu código desde cero.";
        });

        // Snippets select
        dom.sandboxSnippetsSelect.addEventListener("change", (e) => {
          const val = e.target.value;
          if (val === "types") {
            dom.sandboxCode.value = `# Tipos y Casting\nnumero_str = '42'\nnumero_int = int(numero_str)\nprecio = 99.99\nes_activo = True`;
          } else if (val === "id_check") {
            dom.sandboxCode.value = `# Comprobar inmutabilidad e id()\nx = 100\nprint('ID inicial:', id(x))\nx = x + 1\nprint('Nuevo ID (nueva caja):', id(x))`;
          } else if (val === "fstrings") {
            dom.sandboxCode.value = `# Formato f-strings profesional\nusuario = 'Wisrovi'\npuntos = 1500\nprint(f'Ingeniero {usuario:^12} | Score: {puntos:06d}')`;
          } else if (val === "loops") {
            dom.sandboxCode.value = `# Bucles y filtrado\nvalores = [12, 45, 68, 23, 90]\npares = [v for v in valores if v % 2 == 0]\nprint('Pares encontrados:', pares)`;
          }
          updateLineNumbers(dom.sandboxCode, dom.sandboxLines);
          dom.sandboxSnippetsSelect.value = "";
        });

        // Paso 4
        dom.challengeCode.addEventListener("input", () => updateDiffStatus());

        dom.resetChallengeBtn.addEventListener("click", () => {
          dom.challengeCode.value = state.starterChallengeCode;
          updateLineNumbers(dom.challengeCode, dom.challengeLines);
          updateDiffStatus();
          dom.challengeResults.innerHTML = `<div style="color: #64748b; font-size: 0.85rem; font-style: italic;">Plantilla restaurada.</div>`;
        });

        dom.downloadSolutionBtn.addEventListener("click", () => {
          const blob = new Blob([dom.challengeCode.value], { type: "text/x-python" });
          const url = URL.createObjectURL(blob);
          const a = document.createElement("a");
          a.href = url;
          a.download = `reto_curso_${state.currentCourse}_clase_${state.currentClass.toString().padStart(2, '0')}.py`;
          a.click();
          URL.revokeObjectURL(url);
        });

        dom.evalChallengeBtn.addEventListener("click", async () => {
          soundClick();
          const currentCode = dom.challengeCode.value.trim();
          
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
          const elapsedSecs = state.classStartTime ? Math.round((Date.now() - state.classStartTime) / 1000) : 180;
          const res = await fetch("/api/evaluate-challenge", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              course_num: state.currentCourse,
              class_num: state.currentClass,
              code: currentCode,
              elapsed_seconds: elapsedSecs
            })
          });
          const data = await res.json();

          if (data.evaluation.passed) {
            state.stepsCompleted[4] = true;
            soundVictory();
            if (window.confetti) confetti({ particleCount: 160, spread: 95, origin: { y: 0.6 } });
            
            const r = data.reward || {};
            const totalGained = r.total_xp || 150;
            const speedTier = r.speed_tier || "⏳ Estándar";
            const bonusText = r.speed_bonus > 0 ? ` (+${r.speed_bonus} XP bonificación por velocidad)` : (r.speed_bonus < 0 ? ` (${r.speed_bonus} XP penalización por lentitud)` : "");
            
            dom.challengeResults.innerHTML = `
              <div style="background: rgba(16,185,129,0.25); border: 1px solid #10b981; color: #6ee7b7; padding: 0.85rem; border-radius: 8px; box-shadow: 0 0 20px rgba(16,185,129,0.3);">
                🎉 <strong>¡RETO SUPERADO CON ÉXITO! (+${totalGained} XP)</strong><br>
                <div style="font-size:0.84rem; margin-top:0.4rem; color:#a7f3d0; line-height: 1.4;">
                  ⏱️ <strong>Tiempo:</strong> ${Math.floor(elapsedSecs / 60)}m ${elapsedSecs % 60}s &bull; <strong>Ritmo:</strong> ${speedTier}${bonusText}<br>
                  Tu solución ha superado el 100% de las pruebas y contratos de tipado para la Clase 0${state.currentClass}.
                </div>
              </div>
            `;
            await fetchProfile();
            await fetchCurriculum();
            updateStepperUI();

            if (data.class_certificate) {
              setTimeout(() => {
                openClassCertModal(data.class_certificate);
              }, 800);
            }
          } else {
            soundError();
            dom.challengeResults.innerHTML = `
              <div style="background: rgba(220,38,38,0.25); border: 1px solid #dc2626; color: #fca5a5; padding: 0.85rem; border-radius: 8px;">
                ⚠️ <strong>La solución aún no cumple todas las aserciones:</strong><br>
                <p style="margin-top:0.35rem; font-size:0.86rem;">${data.evaluation.socratic_hint || data.evaluation.output}</p>
              </div>
            `;
          }
        });

        // Atajos de teclado
        document.addEventListener("keydown", (e) => {
          if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
            e.preventDefault();
            if (state.currentStep === 2) dom.runDemoBtn.click();
            else if (state.currentStep === 3) dom.runSandboxBtn.click();
            else if (state.currentStep === 4) dom.evalChallengeBtn.click();
          }
          if ((e.ctrlKey || e.metaKey) && (e.key === "k" || e.key === "K")) {
            e.preventDefault();
            openCommandPalette();
          }
          if ((e.ctrlKey || e.metaKey) && (e.key === "b" || e.key === "B")) {
            e.preventDefault();
            dom.toggleSidebarBtn.click();
          }
          if ((e.key === "f" || e.key === "F") && !["TEXTAREA", "INPUT"].includes(e.target.tagName)) {
            if (state.isTutorMode && dom.slideDeckModal && dom.slideDeckModal.classList.contains("hidden")) {
              e.preventDefault();
              openSlideDeck();
            }
          }
          if (dom.slideDeckModal && !dom.slideDeckModal.classList.contains("hidden")) {
            if (e.key === "ArrowRight" || e.key === " ") {
              e.preventDefault();
              if (state.currentSlide < state.totalSlides) {
                state.currentSlide++;
                renderSlideDeck();
                soundClick();
              }
            } else if (e.key === "ArrowLeft") {
              e.preventDefault();
              if (state.currentSlide > 1) {
                state.currentSlide--;
                renderSlideDeck();
                soundClick();
              }
            }
          }
          if (e.altKey && e.key === "ArrowRight") {
            e.preventDefault();
            dom.nextBtn.click();
          }
          if (e.altKey && e.key === "ArrowLeft") {
            e.preventDefault();
            dom.prevBtn.click();
          }
          if (e.altKey && ["1", "2", "3", "4"].includes(e.key)) {
            e.preventDefault();
            switchStep(parseInt(e.key));
          }
          if (e.altKey && (e.key === "d" || e.key === "D")) {
            e.preventDefault();
            toggleDocsDrawer();
          }
          if (e.key === "Escape") {
            document.querySelectorAll(".modal-backdrop").forEach(m => m.classList.add("hidden"));
          }
        });

        // Resizer para el panel de documentación dividida
        if (dom.docsResizeHandle && dom.docsSplitPanel) {
          let isResizing = false;
          dom.docsResizeHandle.addEventListener("mousedown", (e) => {
            isResizing = true;
            dom.docsResizeHandle.classList.add("active");
            document.body.style.cursor = "col-resize";
            document.body.style.userSelect = "none";
          });

          window.addEventListener("mousemove", (e) => {
            if (!isResizing) return;
            const newWidth = Math.max(280, Math.min(window.innerWidth * 0.75, e.clientX));
            dom.docsSplitPanel.style.width = `${newWidth}px`;
            dom.docsSplitPanel.style.maxWidth = `${newWidth}px`;
          });

          window.addEventListener("mouseup", () => {
            if (isResizing) {
              isResizing = false;
              dom.docsResizeHandle.classList.remove("active");
              document.body.style.cursor = "";
              document.body.style.userSelect = "";
            }
          });
        }

        // Guardar reto directamente en archivo local (ejercicios/reto.py)
        if (dom.saveRetoDiskBtn) {
          dom.saveRetoDiskBtn.addEventListener("click", async () => {
            soundClick();
            try {
              const res = await fetch("/api/save-solution", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                  course_num: state.currentCourse,
                  class_num: state.currentClass,
                  code: dom.challengeCode.value
                })
              });
              const data = await res.json();
              if (data.success) {
                soundChime();
                alert(`💾 ${data.message}`);
              } else {
                alert(`⚠️ ${data.message || 'No se pudo guardar el archivo localmente'}`);
              }
            } catch (e) {
              console.error(e);
              alert("Error al conectar con la API local para guardar solución.");
            }
          });
        }

        // Controles del Modo Diapositivas (Slide Deck)
        if (dom.slideDeckBtn) {
          dom.slideDeckBtn.addEventListener("click", () => openSlideDeck());
        }
        if (dom.closeSlideDeckBtn) {
          dom.closeSlideDeckBtn.addEventListener("click", () => dom.slideDeckModal.classList.add("hidden"));
        }
        if (dom.slidePrevBtn) {
          dom.slidePrevBtn.addEventListener("click", () => {
            if (state.currentSlide > 1) {
              state.currentSlide--;
              renderSlideDeck();
              soundClick();
            }
          });
        }
        if (dom.slideNextBtn) {
          dom.slideNextBtn.addEventListener("click", () => {
            if (state.currentSlide < state.totalSlides) {
              state.currentSlide++;
              renderSlideDeck();
              soundClick();
            }
          });
        }
        if (dom.slideFsBtn) {
          dom.slideFsBtn.addEventListener("click", () => {
            if (!document.fullscreenElement) {
              dom.slideDeckModal.requestFullscreen().catch(err => console.warn(err));
            } else {
              document.exitFullscreen().catch(err => console.warn(err));
            }
          });
        }

        // Controles de Documentación Oficial Web Embebida (Split View)
        if (dom.toggleDocsDrawerBtn) {
          dom.toggleDocsDrawerBtn.addEventListener("click", () => toggleDocsDrawer());
        }
        if (dom.closeDocsDrawerBtn) {
          dom.closeDocsDrawerBtn.addEventListener("click", () => toggleDocsDrawer(false));
        }
        if (dom.reloadDocsFrameBtn) {
          dom.reloadDocsFrameBtn.addEventListener("click", () => {
            if (dom.docsIframe) {
              const cur = dom.docsIframe.src;
              dom.docsIframe.src = "";
              setTimeout(() => { dom.docsIframe.src = cur; }, 60);
            }
            soundClick();
          });
        }
        if (dom.openDocsExtBtn) {
          dom.openDocsExtBtn.addEventListener("click", () => {
            if (dom.docsIframe) window.open(dom.docsIframe.src, "_blank");
          });
        }

        // Escuchar con voz
        dom.listenMetaphorBtn.addEventListener("click", () => {
          if ('speechSynthesis' in window && state.classContent) {
            window.speechSynthesis.cancel();
            const text = `${state.classContent.title}. Metáfora central: ${state.classContent.metaphor}. ${state.classContent.theory}`;
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.lang = 'es-ES';
            utterance.rate = parseFloat(dom.voiceSpeedSelect.value || "1.0");
            window.speechSynthesis.speak(utterance);
          } else {
            alert("Tu navegador no soporta síntesis de voz.");
          }
        });

        // Alternar Modo Estudiante / Modo Presentador Docente
        if (dom.toggleModeBtn) {
          dom.toggleModeBtn.addEventListener("click", () => {
            soundClick();
            setTutorMode(!state.isTutorMode);
          });
        }

        // Guardado automático de borradores en LocalStorage
        function saveLocalDraft() {
          if (!state.currentCourse || !state.currentClass) return;
          try {
            const draftKey = `wisrovi_draft_${state.currentCourse}_${state.currentClass}`;
            localStorage.setItem(draftKey, JSON.stringify({
              challenge: dom.challengeCode.value,
              demo: dom.demoCode.value,
              sandbox: dom.sandboxCode.value
            }));
          } catch (e) {}
        }
        dom.demoCode.addEventListener("input", saveLocalDraft);
        dom.sandboxCode.addEventListener("input", saveLocalDraft);
        dom.challengeCode.addEventListener("input", saveLocalDraft);

        // Modo Proyector
        if (dom.projectorModeBtn) {
          dom.projectorModeBtn.addEventListener("click", () => toggleProjectorMode());
        }

        // Notas del Docente (Speaker Notes)
        if (dom.speakerNotesBtn) {
          dom.speakerNotesBtn.addEventListener("click", () => {
            soundClick();
            dom.speakerNotesModal.classList.remove("hidden");
          });
        }
        if (dom.closeSpeakerNotesBtn) {
          dom.closeSpeakerNotesBtn.addEventListener("click", () => {
            dom.speakerNotesModal.classList.add("hidden");
          });
        }

        // Temporizador de Aula
        if (dom.classroomTimerBtn) {
          dom.classroomTimerBtn.addEventListener("click", () => {
            soundClick();
            dom.classroomTimerModal.classList.remove("hidden");
          });
        }
        if (dom.closeClassroomTimerBtn) {
          dom.closeClassroomTimerBtn.addEventListener("click", () => {
            dom.classroomTimerModal.classList.add("hidden");
          });
        }
        if (dom.timerToggleBtn) {
          dom.timerToggleBtn.addEventListener("click", () => {
            if (state.timerIsRunning) pauseClassroomTimer();
            else startClassroomTimer();
          });
        }
        if (dom.timerResetBtn) {
          dom.timerResetBtn.addEventListener("click", () => {
            soundClick();
            resetClassroomTimer(600);
          });
        }
        document.querySelectorAll(".timer-preset-btn").forEach(btn => {
          btn.addEventListener("click", () => {
            document.querySelectorAll(".timer-preset-btn").forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            const secs = parseInt(btn.dataset.secs || "600");
            soundClick();
            resetClassroomTimer(secs);
          });
        });

        // Alternar sonido
        dom.soundToggleBtn.addEventListener("click", () => {
          state.soundEnabled = !state.soundEnabled;
          dom.soundIcon.textContent = state.soundEnabled ? "🔊" : "🔇";
          dom.soundToggleBtn.style.borderColor = state.soundEnabled ? "var(--border-accent)" : "#64748b";
        });

        // Modal de atajos
        dom.shortcutsBtn.addEventListener("click", () => dom.shortcutsModal.classList.remove("hidden"));
        dom.closeShortcutsBtn.addEventListener("click", () => dom.shortcutsModal.classList.add("hidden"));

        // Avatar selector & Perfil
        const avatars = ["👨‍💻", "👩‍💻", "🧙‍♂️", "🤖", "🚀", "⚡", "🥋", "🐍"];
        dom.avatarPickerRow.innerHTML = "";
        avatars.forEach(av => {
          const btn = document.createElement("button");
          btn.style.cssText = "font-size: 1.5rem; background: #0c1426; border: 1px solid #334155; border-radius: 6px; padding: 0.3rem 0.5rem; cursor: pointer;";
          btn.textContent = av;
          btn.addEventListener("click", () => {
            dom.avatarBtn.textContent = av;
            btn.style.borderColor = "#38bdf8";
          });
          dom.avatarPickerRow.appendChild(btn);
        });

        dom.avatarBtn.addEventListener("click", () => dom.profileModal.classList.remove("hidden"));
        dom.closeProfileBtn.addEventListener("click", () => dom.profileModal.classList.add("hidden"));

        dom.saveProfileBtn.addEventListener("click", async () => {
          const newName = dom.profileNameInput.value.trim();
          const newEmail = dom.profileEmailInput.value.trim();
          if (newName) {
            await fetch("/api/progress", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ name: newName, email: newEmail })
            });
            await fetchProfile();
            dom.profileModal.classList.add("hidden");
            soundChime();
          }
        });

        dom.resetProgressBtn.addEventListener("click", async () => {
          if (confirm("¿Estás seguro de que deseas reiniciar todo tu progreso de XP y las 32 clases?")) {
            await fetch("/api/progress/reset", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ confirm: true })
            });
            await fetchProfile();
            await fetchCurriculum();
            loadClass(1, 1);
            dom.profileModal.classList.add("hidden");
            alert("Progreso reiniciado.");
          }
        });

        // Navegación secuencial de clases
        dom.prevBtn.addEventListener("click", () => {
          if (state.currentClass > 1) {
            loadClass(state.currentCourse, state.currentClass - 1);
          } else if (state.currentCourse > 1) {
            loadClass(state.currentCourse - 1, 8);
          }
        });

        dom.nextBtn.addEventListener("click", () => {
          if (dom.nextBtn.disabled) return;
          if (state.currentClass < 8) {
            const nextCls = state.currentClass + 1;
            if (isClassUnlocked(state.currentCourse, nextCls)) {
              loadClass(state.currentCourse, nextCls);
            } else {
              soundError();
              alert(`🔒 Completa el Reto del Paso 4 para desbloquear la Clase 0${nextCls}.`);
            }
          } else if (state.currentCourse < 4) {
            const nextC = state.currentCourse + 1;
            if (isCourseUnlocked(nextC)) {
              soundVictory();
              alert(`🎉 ¡FELICITACIONES! Has completado el Curso ${state.currentCourse}. Desbloqueando Curso ${nextC}...`);
              loadClass(nextC, 1);
            } else {
              soundError();
              alert(`🔒 Debes superar todas las 8 clases del Curso ${state.currentCourse} para desbloquear el Curso ${nextC}.`);
            }
          } else {
            soundVictory();
            if (window.confetti) confetti({ particleCount: 300, spread: 180, origin: { y: 0.4 } });
            alert(`🏆 ¡HAS ALCANZADO LA CIMA! Has completado las 32 clases del Programa Integral de Formación en Python: De Cero a Agentes de IA.\n\nGenerando tu Diploma Maestro de 160 Horas...`);
            openCert();
          }
        });

        // Certificados y Publicación en LinkedIn
        dom.openCertBtn.addEventListener("click", () => openCert());
        if (dom.headerLinkedinBtn) {
          dom.headerLinkedinBtn.addEventListener("click", () => openClassCertForCurrent());
        }
        if (dom.certModalLinkedinBtn) {
          dom.certModalLinkedinBtn.addEventListener("click", () => {
            dom.certModal.classList.add("hidden");
            openClassCertForCurrent();
          });
        }
        dom.closeCertBtn.addEventListener("click", () => dom.certModal.classList.add("hidden"));
        dom.refreshCertBtn.addEventListener("click", () => openCert());
        dom.certCourseSelect.addEventListener("change", () => openCert());

        dom.downloadCertBtn.addEventListener("click", () => {
          const name = dom.studentNameInput.value || "estudiante";
          window.open(`/api/certificate/download?student_name=${encodeURIComponent(name)}`, "_blank");
        });

        if (dom.downloadCertPngBtn) {
          dom.downloadCertPngBtn.addEventListener("click", () => {
            const name = dom.studentNameInput.value || "estudiante";
            window.open(`/api/certificate/class/download?course_num=${state.currentCourse}&class_num=${state.currentClass}&student_name=${encodeURIComponent(name)}&export_format=png`, "_blank");
          });
        }

        // Eventos del Modal de Diploma de Clase
        if (dom.closeClassCertBtn) {
          dom.closeClassCertBtn.addEventListener("click", () => dom.classCertModal.classList.add("hidden"));
        }

        if (dom.updateClassCertBtn) {
          dom.updateClassCertBtn.addEventListener("click", async () => {
            const updatedName = dom.classCertStudentName.value.trim() || "Estudiante Wisrovi";
            const res = await fetch("/api/certificate/class/preview", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({
                course_num: state.currentCourse,
                class_num: state.currentClass,
                student_name: updatedName
              })
            });
            const data = await res.json();
            if (data.success) {
              dom.classCertPreviewFrame.innerHTML = data.data.html;
              dom.classCertLinkedinText.value = data.data.linkedin_text;
            }
          });
        }

        if (dom.copyLinkedinPostBtn) {
          dom.copyLinkedinPostBtn.addEventListener("click", () => {
            if (dom.classCertLinkedinText) {
              navigator.clipboard.writeText(dom.classCertLinkedinText.value);
              const prevText = dom.copyLinkedinPostBtn.textContent;
              dom.copyLinkedinPostBtn.textContent = "✅ ¡Copiado!";
              setTimeout(() => { dom.copyLinkedinPostBtn.textContent = prevText; }, 2500);
            }
          });
        }

        if (dom.downloadClassPngQuickBtn) {
          dom.downloadClassPngQuickBtn.addEventListener("click", () => {
            const name = dom.classCertStudentName.value.trim() || "Estudiante Wisrovi";
            window.open(`/api/certificate/class/download?course_num=${state.currentCourse}&class_num=${state.currentClass}&student_name=${encodeURIComponent(name)}&export_format=png`, "_blank");
          });
        }

        const publishToLinkedIn = async () => {
          const name = dom.classCertStudentName ? dom.classCertStudentName.value.trim() : "Estudiante Wisrovi";
          const textToCopy = dom.classCertLinkedinText ? dom.classCertLinkedinText.value : "";
          
          // 1. Copiar texto al portapapeles
          if (textToCopy) {
            try {
              await navigator.clipboard.writeText(textToCopy);
            } catch (e) {
              console.warn("Clipboard access:", e);
            }
          }

          // 2. Descargar automáticamente la imagen PNG del diploma para adjuntar
          const pngDownloadUrl = `/api/certificate/class/download?course_num=${state.currentCourse}&class_num=${state.currentClass}&student_name=${encodeURIComponent(name)}&export_format=png`;
          const a = document.createElement("a");
          a.href = pngDownloadUrl;
          a.download = `Diploma_Wisrovi_C${state.currentCourse}_Clase${state.currentClass.toString().padStart(2, '0')}.png`;
          document.body.appendChild(a);
          a.click();
          document.body.removeChild(a);

          // 3. Abrir LinkedIn Feed para crear la publicación
          const linkedinUrl = "https://www.linkedin.com/feed/?shareActive=true";
          window.open(linkedinUrl, "_blank");

          // 4. Mostrar banner guía al estudiante
          if (dom.linkedinShareGuideToast) {
            dom.linkedinShareGuideToast.classList.remove("hidden");
          }
        };

        if (dom.shareLinkedinDirectBtn) dom.shareLinkedinDirectBtn.addEventListener("click", publishToLinkedIn);
        if (dom.shareLinkedinInlineBtn) dom.shareLinkedinInlineBtn.addEventListener("click", publishToLinkedIn);
        if (dom.openLinkedinTopBtn) dom.openLinkedinTopBtn.addEventListener("click", publishToLinkedIn);

        if (dom.shareTwitterBtn) {
          dom.shareTwitterBtn.addEventListener("click", () => {
            const text = `🎓 ¡Acabo de superar la Clase 0${state.currentClass} de Python con William Rodríguez (@wisrovi)! https://academy_python.wisrovi.dev/ #Python #AI`;
            window.open(`https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}`, "_blank");
          });
        }

        if (dom.shareWhatsappBtn) {
          dom.shareWhatsappBtn.addEventListener("click", () => {
            const text = dom.classCertLinkedinText ? dom.classCertLinkedinText.value : `🎓 ¡Acabo de superar la Clase 0${state.currentClass} de Python en Wisrovi Academy! https://academy_python.wisrovi.dev/`;
            window.open(`https://api.whatsapp.com/send?text=${encodeURIComponent(text)}`, "_blank");
          });
        }

        if (dom.downloadClassPdfBtn) {
          dom.downloadClassPdfBtn.addEventListener("click", () => {
            const name = dom.classCertStudentName.value.trim() || "Estudiante Wisrovi";
            window.open(`/api/certificate/class/download?course_num=${state.currentCourse}&class_num=${state.currentClass}&student_name=${encodeURIComponent(name)}&export_format=pdf`, "_blank");
          });
        }

        if (dom.downloadClassPngBtn) {
          dom.downloadClassPngBtn.addEventListener("click", () => {
            const name = dom.classCertStudentName.value.trim() || "Estudiante Wisrovi";
            window.open(`/api/certificate/class/download?course_num=${state.currentCourse}&class_num=${state.currentClass}&student_name=${encodeURIComponent(name)}&export_format=png`, "_blank");
          });
        }

        if (dom.nextClassCertBtn) {
          dom.nextClassCertBtn.addEventListener("click", () => {
            dom.classCertModal.classList.add("hidden");
            if (dom.nextBtn && !dom.nextBtn.disabled) {
              dom.nextBtn.click();
            }
          });
        }

        dom.copyBadgeBtn.addEventListener("click", () => {
          const badge = `[![Wisrovi Certified](https://img.shields.io/badge/Wisrovi%20Academy-Certified%20AI%20Engineer-gold.svg)](https://academy_python.wisrovi.dev)`;
          navigator.clipboard.writeText(badge);
          alert("¡Badge Markdown copiado al portapapeles!");
        });

        // Logros
        dom.achievementsBtn.addEventListener("click", () => openAchievements());
        dom.closeAchievementsBtn.addEventListener("click", () => dom.achievementsModal.classList.add("hidden"));

        // Command Palette
        dom.cmdKBtn.addEventListener("click", () => openCommandPalette());
        dom.cmdKModal.addEventListener("click", (e) => {
          if (e.target === dom.cmdKModal) dom.cmdKModal.classList.add("hidden");
        });
        dom.cmdKInput.addEventListener("input", (e) => filterCommandPalette(e.target.value));

        // Mascot click & Preguntar al Mentor
        dom.floatingMentorAvatar.addEventListener("click", () => {
          soundChime();
          dom.askMentorModal.classList.remove("hidden");
        });

        dom.askMentorModalBtn.addEventListener("click", () => {
          dom.askMentorModal.classList.remove("hidden");
        });

        dom.closeAskMentorBtn.addEventListener("click", () => {
          dom.askMentorModal.classList.add("hidden");
        });

        dom.sendMentorChatBtn.addEventListener("click", () => handleMentorChat());
        dom.mentorChatInput.addEventListener("keydown", (e) => {
          if (e.key === "Enter") handleMentorChat();
        });
      }

      async function handleMentorChat() {
        const q = dom.mentorChatInput.value.trim();
        if (!q) return;
        
        const userMsg = document.createElement("div");
        userMsg.className = "chat-msg student";
        userMsg.textContent = q;
        dom.mentorChatHistory.appendChild(userMsg);
        dom.mentorChatInput.value = "";
        dom.mentorChatHistory.scrollTop = dom.mentorChatHistory.scrollHeight;

        try {
          const res = await fetch("/api/ask-mentor", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              course_num: state.currentCourse,
              class_num: state.currentClass,
              question: q,
              code: dom.challengeCode.value
            })
          });
          const data = await res.json();
          
          const mentorMsg = document.createElement("div");
          mentorMsg.className = "chat-msg mentor";
          mentorMsg.innerHTML = data.reply;
          dom.mentorChatHistory.appendChild(mentorMsg);
          dom.mentorChatHistory.scrollTop = dom.mentorChatHistory.scrollHeight;
          soundChime();
        } catch (e) {
          console.error(e);
        }
      }

      function openCommandPalette() {
        dom.cmdKModal.classList.remove("hidden");
        dom.cmdKInput.value = "";
        dom.cmdKInput.focus();
        filterCommandPalette("");
      }

      function filterCommandPalette(query) {
        dom.cmdKResults.innerHTML = "";
        const q = query.toLowerCase();
        
        const actions = [
          { name: "📜 Ver / Generar Certificados Oficiales", run: () => { dom.cmdKModal.classList.add("hidden"); openCert(); } },
          { name: "🏆 Abrir Vitrina de Logros y Trofeos", run: () => { dom.cmdKModal.classList.add("hidden"); openAchievements(); } },
          { name: "💬 Preguntar al Mentor Wisrovi", run: () => { dom.cmdKModal.classList.add("hidden"); dom.askMentorModal.classList.remove("hidden"); } },
          { name: "🔊 Alternar Efectos Sonoros (Mute)", run: () => { dom.cmdKModal.classList.add("hidden"); dom.soundToggleBtn.click(); } }
        ];

        state.curriculum.forEach(cls => {
          actions.push({
            name: `C${cls.course_num}-S0${cls.class_num}: ${cls.title}`,
            run: () => {
              dom.cmdKModal.classList.add("hidden");
              loadClass(cls.course_num, cls.class_num);
            }
          });
        });

        actions.filter(a => a.name.toLowerCase().includes(q)).forEach(a => {
          const item = document.createElement("div");
          item.style.cssText = "padding:0.55rem 0.85rem; background:#0f172a; border-radius:6px; font-size:0.84rem; color:#cbd5e1; cursor:pointer; display:flex; align-items:center; gap:0.5rem; transition:background var(--transition-fast);";
          item.innerHTML = `<span>▶️</span> <span>${a.name}</span>`;
          item.addEventListener("mouseenter", () => item.style.background = "#1e293b");
          item.addEventListener("mouseleave", () => item.style.background = "#0f172a");
          item.addEventListener("click", a.run);
          dom.cmdKResults.appendChild(item);
        });
      }

      function renderMemoryDual(vars) {
        if (!vars || vars.length === 0) {
          dom.memoryCanvas.innerHTML = `<div class="empty-state">No se detectaron variables en el scope actual.</div>`;
          dom.memTotalCount.textContent = "0 Variables";
          return;
        }
        dom.memoryCanvas.innerHTML = "";
        dom.memTotalCount.textContent = `${vars.length} Variables`;

        const stackVars = vars.filter(v => !v.is_mutable);
        const heapVars = vars.filter(v => v.is_mutable);

        const stackCol = document.createElement("div");
        stackCol.className = "mem-column";
        stackCol.innerHTML = `<div class="mem-column-header"><span>🧱 STACK (Inmutables)</span><span>${stackVars.length}</span></div>`;

        if (stackVars.length === 0) {
          stackCol.innerHTML += `<div style="font-size:0.75rem; color:#64748b; font-style:italic; padding:0.5rem;">Sin variables primitivas</div>`;
        } else {
          stackVars.forEach(v => {
            const c = document.createElement("div");
            c.className = "mem-card";
            c.innerHTML = `
              <div class="mem-top-row">
                <span class="mem-name">${v.icon} ${v.name}</span>
                <span class="mem-type">(${v.type})</span>
              </div>
              <div class="mem-val-row">${v.value}</div>
              <div class="mem-meta-row">
                <span class="mem-bytes-badge">${v.size_bytes} B</span>
                <span class="mem-hex-id">${v.id}</span>
              </div>
            `;
            stackCol.appendChild(c);
          });
        }

        const heapCol = document.createElement("div");
        heapCol.className = "mem-column";
        heapCol.innerHTML = `<div class="mem-column-header" style="color:#c084fc;"><span>📦 HEAP (Mutables / Objetos)</span><span>${heapVars.length}</span></div>`;

        if (heapVars.length === 0) {
          heapCol.innerHTML += `<div style="font-size:0.75rem; color:#64748b; font-style:italic; padding:0.5rem;">Sin estructuras en Heap</div>`;
        } else {
          heapVars.forEach(v => {
            const c = document.createElement("div");
            c.className = "mem-card heap-card";
            c.innerHTML = `
              <div class="mem-top-row">
                <span class="mem-name" style="color:#c084fc;">${v.icon} ${v.name}</span>
                <span class="mem-type">(${v.type})</span>
              </div>
              <div class="mem-val-row">${v.value}</div>
              <div class="mem-meta-row">
                <span class="mem-bytes-badge" style="color:#c084fc; border-color:rgba(192,132,252,0.4);">${v.size_bytes} B</span>
                <span class="mem-hex-id">${v.id}</span>
              </div>
            `;
            heapCol.appendChild(c);
          });
        }

        dom.memoryCanvas.appendChild(stackCol);
        dom.memoryCanvas.appendChild(heapCol);
      }

      async function openClassCertModal(certData) {
        if (!certData) return;
        state.lastClassCertData = certData;
        dom.classCertModal.classList.remove("hidden");
        
        const defaultName = (state.profile && state.profile.name) ? state.profile.name : "Estudiante Wisrovi";
        dom.classCertStudentName.value = certData.student_name || defaultName;
        
        if (dom.classCertModalSubtitle) {
          dom.classCertModalSubtitle.textContent = `${certData.title} • Curso ${certData.course_num} (Clase 0${certData.class_num})`;
        }
        dom.classCertPreviewFrame.innerHTML = certData.html;
        dom.classCertLinkedinText.value = certData.linkedin_text;
      }

      async function openClassCertForCurrent() {
        const defaultName = (state.profile && state.profile.name) ? state.profile.name : "Estudiante Wisrovi";
        try {
          const res = await fetch("/api/certificate/class/preview", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              course_num: state.currentCourse,
              class_num: state.currentClass,
              student_name: defaultName
            })
          });
          const data = await res.json();
          if (data.success) {
            openClassCertModal(data.data);
          }
        } catch (e) {
          console.error("Error cargando diploma de clase:", e);
        }
      }

      async function openCert() {
        dom.certModal.classList.remove("hidden");
        const name = dom.studentNameInput.value || "Estudiante Wisrovi";
        const courseChoice = dom.certCourseSelect.value;
        
        if (courseChoice === "current") {
          const res = await fetch("/api/certificate/class/preview", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ course_num: state.currentCourse, class_num: state.currentClass, student_name: name })
          });
          const data = await res.json();
          if (data.success) {
            dom.certPreviewFrame.innerHTML = data.data.html;
          }
          return;
        }

        let courseTitle = "Programa Integral de Formación en Python: De Cero a Agentes de IA";
        let hours = 160;

        if (courseChoice === "1") { courseTitle = "Curso 1: Fundamentos Básicos de Python"; hours = 40; }
        else if (courseChoice === "2") { courseTitle = "Curso 2: Algoritmos Avanzados y Estructuras de Datos"; hours = 40; }
        else if (courseChoice === "3") { courseTitle = "Curso 3: Desarrollo de Agentes de Inteligencia Artificial"; hours = 40; }
        else if (courseChoice === "4") { courseTitle = "Curso 4: Taller Práctico & Proyecto Integrador Full-Stack"; hours = 40; }

        const res = await fetch("/api/certificate/generate", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ student_name: name, course_title: courseTitle, hours: hours })
        });
        const data = await res.json();
        dom.certPreviewFrame.innerHTML = data.html;
      }

      function openAchievements() {
        dom.achievementsModal.classList.remove("hidden");
        const badges = [
          { id: "first_code", name: "🚴 Primer Pedaleo", desc: "Ejecutaste tu primer bloque de código en Python." },
          { id: "memory_master", name: "🔬 Explorador del Heap", desc: "Inspeccionaste variables y memoria en el Arenero." },
          { id: "c1_graduate", name: "🎯 Fundador de Python", desc: "Completaste las 8 clases del Curso 1." },
          { id: "c2_graduate", name: "⚡ Mago de Algoritmos", desc: "Completaste las 8 clases del Curso 2." },
          { id: "c3_graduate", name: "🤖 Conjurador de IA", desc: "Completaste las 8 clases del Curso 3." },
          { id: "c4_graduate", name: "🏆 Graduado de Élite", desc: "Completaste el Programa Integral de 32 Semanas." },
          { id: "streak_3", name: "🔥 Racha Imparable", desc: "Mantuviste 3 días consecutivos de práctica activa." },
          { id: "speedster", name: "✨ Código Pythonic", desc: "Superaste un reto a la primera sin pedir pistas." }
        ];

        dom.achievementsGrid.innerHTML = "";
        badges.forEach(b => {
          const isUnlocked = state.profile && state.profile.unlocked_badges && state.profile.unlocked_badges.includes(b.id);
          const card = document.createElement("div");
          card.style.cssText = `background: ${isUnlocked ? 'rgba(16,185,129,0.15)' : 'rgba(15,23,42,0.6)'}; border: 1px solid ${isUnlocked ? '#10b981' : '#334155'}; border-radius: 8px; padding: 0.85rem; display: flex; flex-direction: column; gap: 0.3rem;`;
          card.innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:center;">
              <strong style="color: ${isUnlocked ? '#34d399' : '#94a3b8'}; font-size: 0.9rem;">${b.name}</strong>
              <span style="font-size:0.75rem; color:${isUnlocked ? '#34d399' : '#64748b'};">${isUnlocked ? '✓ Desbloqueado' : '🔒 Bloqueado'}</span>
            </div>
            <p style="font-size: 0.78rem; color: #94a3b8;">${b.desc}</p>
          `;
          dom.achievementsGrid.appendChild(card);
        });
      }

      function renderSlideDeck() {
        if (!state.classContent) return;
        const d = state.classContent;
        dom.slideDeckTitle.textContent = `Curso ${d.course_num} - Clase 0${d.class_num}: ${d.title}`;
        dom.slideCurrentNum.textContent = state.currentSlide;
        
        let slideHtml = "";
        if (state.currentSlide === 1) {
          slideHtml = `
            <div class="slide-content-card" style="text-align:center;">
              <span style="font-size:3rem;">🐍</span>
              <div style="font-size:0.85rem; text-transform:uppercase; letter-spacing:2px; color:#38bdf8; font-weight:800; margin-top:0.5rem;">${d.course_name} &bull; Clase 0${d.class_num}</div>
              <h1 style="font-size:2.2rem; font-weight:900; color:#fff; margin:0.8rem 0;">${d.title}</h1>
              <div style="font-size:1.1rem; color:#fde047; font-weight:700; background:rgba(234,179,8,0.15); border:1px solid rgba(234,179,8,0.4); padding:0.8rem 1.2rem; border-radius:10px; display:inline-block; margin-top:0.5rem;">
                Metáfora Central: «${d.metaphor}»
              </div>
              <p style="font-size:1rem; color:#cbd5e1; line-height:1.6; margin-top:1.5rem; max-width:800px; margin-left:auto; margin-right:auto;">
                ${d.theory.replace(/\\n/g, "<br>")}
              </p>
            </div>
          `;
        } else if (state.currentSlide === 2) {
          slideHtml = `
            <div class="slide-content-card">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
                <h2 style="font-size:1.5rem; color:#38bdf8; font-weight:800;">📐 Arquitectura y Flujo de Ejecución</h2>
                <span style="font-size:0.85rem; color:#94a3b8;">Diagrama Mermaid de Alto Contraste</span>
              </div>
              <div id="slide-mermaid-box" style="background:#020612; border:1px solid var(--border-glass); border-radius:10px; padding:1.5rem; display:flex; justify-content:center; align-items:center; min-height:360px;">
              </div>
            </div>
          `;
          setTimeout(() => {
            const el = document.getElementById("slide-mermaid-box");
            if (el && window.mermaid && d.mermaid) {
              const id = "slide-mermaid-" + Date.now();
              mermaid.render(id, d.mermaid).then(({ svg }) => { el.innerHTML = svg; }).catch(() => { el.innerHTML = `<pre>${d.mermaid}</pre>`; });
            }
          }, 50);
        } else if (state.currentSlide === 3) {
          slideHtml = `
            <div class="slide-content-card">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
                <h2 style="font-size:1.5rem; color:#34d399; font-weight:800;">⚡ Demostración en Vivo &amp; Código Canónico</h2>
                <span style="font-size:0.85rem; color:#94a3b8;">Python 3.12+ Tipado Estricto</span>
              </div>
              <pre style="background:#020612; border:1px solid var(--border-glass); border-radius:10px; padding:1.2rem; font-family:var(--font-code); font-size:1rem; color:#38bdf8; overflow-x:auto; line-height:1.5;">${d.demo_code}</pre>
            </div>
          `;
        } else if (state.currentSlide === 4) {
          const antipattern = (d.pythonic_tip && d.pythonic_tip.antipattern) ? d.pythonic_tip.antipattern : "# Antipatrón común";
          const pythonic = (d.pythonic_tip && d.pythonic_tip.pythonic) ? d.pythonic_tip.pythonic : "# Patrón idiomático";
          slideHtml = `
            <div class="slide-content-card">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem;">
                <h2 style="font-size:1.5rem; color:#f59e0b; font-weight:800;">✨ Comparativa de Ingeniería: Antipatrón vs Pythonic (PEP 8)</h2>
              </div>
              <div style="display:grid; grid-template-columns:1fr 1fr; gap:1.2rem;">
                <div style="background:rgba(239,68,68,0.1); border:1px solid #ef4444; border-radius:10px; padding:1.2rem;">
                  <strong style="color:#f87171; font-size:1rem;">❌ Antipatrón / Trampa Común</strong>
                  <pre style="background:#020612; padding:0.8rem; border-radius:6px; margin-top:0.6rem; font-size:0.9rem; color:#fca5a5; overflow-x:auto;">${antipattern}</pre>
                </div>
                <div style="background:rgba(16,185,129,0.1); border:1px solid #10b981; border-radius:10px; padding:1.2rem;">
                  <strong style="color:#34d399; font-size:1rem;">✅ Solución Idiomática Pythonic</strong>
                  <pre style="background:#020612; padding:0.8rem; border-radius:6px; margin-top:0.6rem; font-size:0.9rem; color:#6ee7b7; overflow-x:auto;">${pythonic}</pre>
                </div>
              </div>
            </div>
          `;
        } else if (state.currentSlide === 5) {
          slideHtml = `
            <div class="slide-content-card" style="text-align:center;">
              <span style="font-size:3rem;">🚴</span>
              <div style="font-size:0.85rem; text-transform:uppercase; letter-spacing:2px; color:#a855f7; font-weight:800; margin-top:0.5rem;">La Regla de la Bicicleta &bull; 70% Práctica Activa</div>
              <h1 style="font-size:2rem; font-weight:900; color:#fff; margin:0.8rem 0;">Reto Práctico del Estudiante</h1>
              <p style="font-size:1.15rem; color:#cbd5e1; max-width:800px; margin:1rem auto; line-height:1.6;">
                ${d.challenge_prompt}
              </p>
              <div style="background:rgba(2,132,199,0.15); border:1px solid #38bdf8; border-radius:10px; padding:1rem; margin-top:1.5rem; display:inline-flex; align-items:center; gap:1.5rem;">
                <div style="text-align:left;">
                  <div style="font-size:0.8rem; color:#94a3b8;">Objetivo de Acreditación:</div>
                  <div style="font-size:1rem; font-weight:800; color:#38bdf8;">Superar pruebas unitarias en el Arenero (+150 XP)</div>
                </div>
                <button class="btn btn-primary" id="slide-open-challenge-btn" style="font-weight:800;">🚀 Abrir Editor de Reto</button>
              </div>
            </div>
          `;
          setTimeout(() => {
            const btn = document.getElementById("slide-open-challenge-btn");
            if (btn) {
              btn.addEventListener("click", () => {
                dom.slideDeckModal.classList.add("hidden");
                switchStep(4);
              });
            }
          }, 50);
        }
        dom.slideDeckBody.innerHTML = slideHtml;
      }

      function openSlideDeck() {
        state.currentSlide = 1;
        dom.slideDeckModal.classList.remove("hidden");
        renderSlideDeck();
        soundChime();
      }

      initApp();
    });
  </script>
</body>
</html>
"""
