/**
 * Wisrovi Academy - Virtual AI Tutor & RPG Engine v2.0
 * Lógica reactiva SPA con sistema de compuertas estrictas (4 pasos obligatorios),
 * sintetizador Web Audio, narración por voz y visualizador Heap en tiempo real.
 */

document.addEventListener("DOMContentLoaded", () => {
  // Estado global de la sesión
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
    elapsedSeconds: 0
  };

  // Sintetizador Web Audio API nativo
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
    const timerElem = document.getElementById("session-timer");
    if (timerElem) timerElem.textContent = `${m}:${s}`;
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
    dom.gatePills.forEach(pill => {
      pill.addEventListener("click", () => switchStep(parseInt(pill.dataset.step)));
    });

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

    // Paso 3
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

    // Paso 4
    dom.evalChallengeBtn.addEventListener("click", async () => {
      soundClick();
      const currentCode = dom.challengeCode.value.trim();
      
      // Validación estricta: Debe haber modificado el código de inicio
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

    // Escuchar con voz
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
        alert("🎉 ¡FELICITACIONES! Has completado y superado las 8 clases del Curso 1: Fundamentos Básicos de Python.\n\nGenerando tu Certificado Oficial de Acreditación...");
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
