/**
 * Wisrovi Academy - Virtual AI Tutor & RPG Engine
 * Lógica reactiva de la Single-Page Application (SPA)
 */

document.addEventListener("DOMContentLoaded", () => {
  // Estado global de la sesión
  const state = {
    currentCourse: 1,
    currentClass: 1,
    profile: null,
    curriculum: [],
    classContent: null,
    currentStep: 1
  };

  // Inicializar Mermaid
  if (window.mermaid) {
    mermaid.initialize({
      startOnLoad: false,
      theme: "dark",
      securityLevel: "loose"
    });
  }

  // ----------------------------------------------------------------------------
  // ELEMENTOS DEL DOM
  // ----------------------------------------------------------------------------
  const dom = {
    levelTitle: document.getElementById("player-level-title"),
    levelBadge: document.getElementById("player-level-badge"),
    xpVal: document.getElementById("player-xp-val"),
    xpPercent: document.getElementById("xp-progress-percent"),
    xpFill: document.getElementById("player-xp-fill"),
    streak: document.getElementById("player-streak"),
    progressPill: document.getElementById("total-progress-pill"),
    classTree: document.getElementById("class-tree-container"),
    
    // Encabezado de clase
    courseName: document.getElementById("lesson-course-name"),
    bossBadge: document.getElementById("lesson-boss-badge"),
    lessonTitle: document.getElementById("lesson-title"),
    metaphor: document.getElementById("lesson-metaphor"),

    // Pasos
    stepBtns: document.querySelectorAll(".step-btn"),
    stepPanes: document.querySelectorAll(".step-pane"),

    // Paso 1
    theoryText: document.getElementById("theory-text"),
    mermaidBox: document.getElementById("mermaid-render-box"),

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

    // Footer de Navegación
    prevBtn: document.getElementById("prev-class-btn"),
    nextBtn: document.getElementById("next-class-btn"),

    // Modal Certificado
    certModal: document.getElementById("cert-modal"),
    openCertBtn: document.getElementById("open-cert-btn"),
    closeCertBtn: document.getElementById("close-cert-btn"),
    studentNameInput: document.getElementById("student-name-input"),
    certPreviewFrame: document.getElementById("cert-preview-frame"),
    copyBadgeBtn: document.getElementById("copy-badge-btn"),
    downloadCertBtn: document.getElementById("download-cert-btn")
  };

  // ----------------------------------------------------------------------------
  // INICIALIZACIÓN Y CARGA DE DATOS
  // ----------------------------------------------------------------------------
  async function initApp() {
    await fetchProfile();
    await fetchCurriculum();
    await loadClass(state.currentCourse, state.currentClass);
    setupEventListeners();
  }

  async function fetchProfile() {
    try {
      const res = await fetch("/api/progress");
      const data = await res.json();
      state.profile = data;
      state.currentCourse = data.current_course || 1;
      state.currentClass = data.current_class || 1;
      updateProfileUI();
    } catch (e) {
      console.error("Error al cargar perfil:", e);
    }
  }

  function updateProfileUI() {
    if (!state.profile) return;
    const p = state.profile;
    dom.levelTitle.textContent = `Nv. ${p.level} ${p.level_title.split(' ')[1] || 'Aprendiz'}`;
    dom.xpVal.textContent = p.xp;
    dom.streak.textContent = `${p.streak_days} Días`;
    
    // Barra de XP (módulo 500)
    const currentLvlXP = p.xp % 500;
    const percent = Math.min(100, Math.round((currentLvlXP / 500) * 100));
    dom.xpPercent.textContent = `${percent}%`;
    dom.xpFill.style.width = `${percent}%`;
  }

  async function fetchCurriculum() {
    try {
      const res = await fetch("/api/curriculum");
      const data = await res.json();
      state.curriculum = data.classes;
      dom.progressPill.textContent = `${data.progress_percent}% Completado`;
      renderSidebarTree();
    } catch (e) {
      console.error("Error al cargar currículo:", e);
    }
  }

  function renderSidebarTree() {
    dom.classTree.innerHTML = "";
    const courses = [
      { id: 1, name: "Curso 1: Fundamentos Básicos" },
      { id: 2, name: "Curso 2: Algoritmos y Estructuras" },
      { id: 3, name: "Curso 3: Agentes de IA" },
      { id: 4, name: "Curso 4: Proyecto Final Integrador" }
    ];

    courses.forEach(c => {
      const group = document.createElement("div");
      group.className = "tree-course-group";
      
      const title = document.createElement("div");
      title.className = "tree-course-title";
      title.textContent = c.name;
      group.appendChild(title);

      const courseClasses = state.curriculum.filter(cls => cls.course_num === c.id);
      courseClasses.forEach(cls => {
        const item = document.createElement("div");
        const isActive = (cls.course_num === state.currentCourse && cls.class_num === state.currentClass);
        item.className = `tree-class-item ${isActive ? 'active' : ''} ${cls.completed ? 'completed' : ''}`;
        
        const bossIcon = cls.boss_battle ? "⚔️ " : "";
        item.innerHTML = `
          <span>${bossIcon}S${cls.class_num.toString().padStart(2, '0')}: ${cls.title.split(':')[1] || cls.title}</span>
          <span class="check-icon">${cls.completed ? '✓' : '○'}</span>
        `;

        item.addEventListener("click", () => {
          loadClass(cls.course_num, cls.class_num);
        });

        group.appendChild(item);
      });

      dom.classTree.appendChild(group);
    });
  }

  // ----------------------------------------------------------------------------
  // CARGA DE CLASE ESPECÍFICA
  // ----------------------------------------------------------------------------
  async function loadClass(courseNum, classNum) {
    state.currentCourse = courseNum;
    state.currentClass = classNum;
    
    try {
      const res = await fetch(`/api/class/${courseNum}/${classNum}`);
      const data = await res.json();
      state.classContent = data;
      renderClassContent(data);
      renderSidebarTree(); // Actualizar clase activa
      switchStep(1); // Volver al paso 1
    } catch (e) {
      console.error("Error al cargar clase:", e);
    }
  }

  function renderClassContent(data) {
    dom.courseName.textContent = data.course_name;
    dom.lessonTitle.textContent = data.title;
    dom.metaphor.textContent = `Metáfora Central: «${data.metaphor}»`;
    
    if (data.boss_battle) {
      dom.bossBadge.classList.remove("hidden");
    } else {
      dom.bossBadge.classList.add("hidden");
    }

    // Paso 1: Teoría & Mermaid
    dom.theoryText.innerHTML = data.theory.replace(/\n/g, "<br>");
    renderMermaid(data.mermaid);

    // Paso 2: Demo
    dom.demoCode.value = data.demo_code;
    dom.demoTerm.innerHTML = `<span class="term-prompt">&gt;</span> <span class="term-msg">Presiona 'Ejecutar Demo' para compilar.</span>`;

    // Paso 3: Arenero
    dom.sandboxCode.value = data.playground_code;
    dom.sandboxTerm.innerHTML = `<span class="term-prompt">&gt;</span> <span class="term-msg">Modifica variables y pulsa 'Inspeccionar Memoria'.</span>`;
    dom.memoryCanvas.innerHTML = `<div class="empty-memory-state">Ejecuta código para visualizar las variables en la memoria RAM.</div>`;

    // Paso 4: Reto
    dom.challengePrompt.textContent = data.challenge_prompt;
    dom.challengeCode.value = data.challenge_starter;
    dom.challengeResults.innerHTML = `<div class="status-msg">Escribe tu solución y pulsa 'Evaluar Reto'.</div>`;
    
    // Pistas socráticas
    dom.hintsAccordion.innerHTML = "";
    data.socratic_hints.forEach((hint, idx) => {
      const hintDiv = document.createElement("div");
      hintDiv.style.padding = "0.5rem";
      hintDiv.style.background = "#1e293b";
      hintDiv.style.borderRadius = "6px";
      hintDiv.style.marginBottom = "0.4rem";
      hintDiv.style.fontSize = "0.82rem";
      hintDiv.textContent = hint;
      dom.hintsAccordion.appendChild(hintDiv);
    });
  }

  function renderMermaid(chartCode) {
    dom.mermaidBox.innerHTML = "";
    if (window.mermaid && chartCode) {
      const id = "mermaid-svg-" + Date.now();
      mermaid.render(id, chartCode).then(({ svg }) => {
        dom.mermaidBox.innerHTML = svg;
      }).catch(err => {
        dom.mermaidBox.innerHTML = `<pre style="color: #94a3b8; font-size: 0.8rem;">${chartCode}</pre>`;
      });
    }
  }

  // ----------------------------------------------------------------------------
  // NAVEGACIÓN ENTRE PASOS
  // ----------------------------------------------------------------------------
  function switchStep(stepNum) {
    state.currentStep = stepNum;
    dom.stepBtns.forEach(btn => {
      btn.classList.toggle("active", parseInt(btn.dataset.step) === stepNum);
    });
    dom.stepPanes.forEach(pane => {
      pane.classList.toggle("active", pane.id === `pane-step-${stepNum}`);
    });
  }

  // ----------------------------------------------------------------------------
  // EVENT LISTENERS & EJECUCIÓN
  // ----------------------------------------------------------------------------
  function setupEventListeners() {
    // Pestañas de pasos
    dom.stepBtns.forEach(btn => {
      btn.addEventListener("click", () => {
        switchStep(parseInt(btn.dataset.step));
      });
    });

    // Ejecutar Demo
    dom.runDemoBtn.addEventListener("click", async () => {
      dom.demoTerm.innerHTML = "<span class='term-prompt'>&gt;</span> Ejecutando...";
      const res = await fetch("/api/run-code", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: dom.demoCode.value })
      });
      const data = await res.json();
      dom.demoTerm.innerHTML = `<span class='term-prompt'>&gt;</span> ${data.stdout || data.stderr || 'Ejecutado sin salida.'}`;
    });

    // Ejecutar Arenero & Memoria
    dom.runSandboxBtn.addEventListener("click", async () => {
      dom.sandboxTerm.innerHTML = "<span class='term-prompt'>&gt;</span> Analizando estado del Heap...";
      const res = await fetch("/api/run-code", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: dom.sandboxCode.value })
      });
      const data = await res.json();
      dom.sandboxTerm.innerHTML = `<span class='term-prompt'>&gt;</span> ${data.stdout || data.stderr || 'Ejecutado.'}`;
      renderMemoryCanvas(data.memory_variables);
    });

    // Evaluar Reto
    dom.evalChallengeBtn.addEventListener("click", async () => {
      dom.challengeResults.innerHTML = "<div class='status-msg'>🧪 Ejecutando suite de pruebas automatizadas...</div>";
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
        // ¡Lanzar confeti!
        if (window.confetti) {
          confetti({ particleCount: 120, spread: 80, origin: { y: 0.6 } });
        }
        dom.challengeResults.innerHTML = `
          <div style="background: rgba(5, 150, 105, 0.2); border: 1px solid #059669; color: #6ee7b7; padding: 0.75rem; border-radius: 6px;">
            🎉 <strong>¡RETO SUPERADO! (+150 XP)</strong><br>
            Tu código pasó todas las pruebas unitarias. ¡Excelente trabajo de ingeniería!
          </div>
        `;
        await fetchProfile();
        await fetchCurriculum();
      } else {
        dom.challengeResults.innerHTML = `
          <div style="background: rgba(220, 38, 38, 0.2); border: 1px solid #dc2626; color: #fca5a5; padding: 0.75rem; border-radius: 6px;">
            ⚠️ <strong>La solución aún no cumple todas las condiciones:</strong><br>
            <p style="margin-top: 0.3rem; font-size: 0.85rem;">${data.evaluation.socratic_hint}</p>
          </div>
        `;
      }
    });

    // Botones de Navegación Footer
    dom.prevBtn.addEventListener("click", () => {
      if (state.currentClass > 1) {
        loadClass(state.currentCourse, state.currentClass - 1);
      } else if (state.currentCourse > 1) {
        loadClass(state.currentCourse - 1, 8);
      }
    });

    dom.nextBtn.addEventListener("click", () => {
      if (state.currentClass < 8) {
        loadClass(state.currentCourse, state.currentClass + 1);
      } else if (state.currentCourse < 4) {
        loadClass(state.currentCourse + 1, 1);
      }
    });

    // Modal Certificado
    dom.openCertBtn.addEventListener("click", () => openCertificateModal());
    dom.closeCertBtn.addEventListener("click", () => dom.certModal.classList.add("hidden"));
    
    dom.copyBadgeBtn.addEventListener("click", () => {
      const badge = `[![Wisrovi Certified](https://img.shields.io/badge/Wisrovi%20Academy-Certified%20AI%20Engineer-gold.svg)](https://academy_python.wisrovi.dev)`;
      navigator.clipboard.writeText(badge);
      alert("¡Badge Markdown copiado al portapapeles! Pégalo en tu perfil de GitHub.");
    });
  }

  function renderMemoryCanvas(variables) {
    if (!variables || variables.length === 0) {
      dom.memoryCanvas.innerHTML = `<div class="empty-memory-state">No se detectaron variables globales en este fragmento.</div>`;
      return;
    }
    
    dom.memoryCanvas.innerHTML = "";
    variables.forEach(v => {
      const card = document.createElement("div");
      card.className = "mem-var-card";
      card.innerHTML = `
        <div>
          <span class="mem-var-name">${v.icon} ${v.name}</span>
          <span style="color: #94a3b8; font-size: 0.75rem;">(${v.type})</span> = <strong style="color: #f8fafc;">${v.value}</strong>
        </div>
        <div>
          <span class="mem-var-bytes">${v.size_bytes} Bytes</span>
          <span class="mem-var-id">${v.id}</span>
        </div>
      `;
      dom.memoryCanvas.appendChild(card);
    });
  }

  async function openCertificateModal() {
    dom.certModal.classList.remove("hidden");
    const name = dom.studentNameInput.value || (state.profile ? state.profile.name : "Alejandro Martínez");
    
    const res = await fetch("/api/certificate/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        student_name: name,
        course_title: "Programa Integral de Formación en Python: De Cero a Agentes de IA",
        hours: 160
      })
    });
    
    const data = await res.json();
    dom.certPreviewFrame.innerHTML = data.html;
  }

  // Arrancar aplicación
  initApp();
});
