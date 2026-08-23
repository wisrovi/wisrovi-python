#!/usr/bin/env python3
"""
Wisrovi CLI - Asistente y Acompañante de Aprendizaje Interactivo.
Ecosistema oficial para estudiantes del programa 'De Cero a Agentes de IA'.
"""

import os
import sys
import argparse
import subprocess
import webbrowser
from typing import Optional

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.markdown import Markdown
    from rich.text import Text
except ImportError:
    # Fallback básico si rich no estuviera instalado en algún entorno mínimo
    class Console:
        def print(self, *args, **kwargs):
            print(*args)
    Console = Console

console = Console()

BANNER = r"""[bold cyan]
  _       _                           _ 
 \ \     / (_)___ _ __ _____   _____ (_)
  \ \ /\ / /| / __| '__/ _ \ \ / / \ \/ /
   \ V  V / | \__ \ | | (_) \ V / | |>  < 
    \_/\_/  |_|___/_|  \___/ \_/  |_/_/\_\
[/bold cyan]
[bold green]🐍 Programa Integral de Formación en Python: De Cero a Agentes de IA[/bold green]
[dim]Director Académico: William Rodríguez (Wisrovi) | https://wisrovi.dev[/dim]
"""

COURSES_DATA = {
    1: {
        "title": "Curso 1: Fundamentos Básicos de Python",
        "folder": "01-fundamentos-python",
        "level": "Nivel 1 (Principiantes)",
        "classes": [
            ("clase-01-panorama-general", "El Megáfono, las Cajas, el Semáforo y la Cinta"),
            ("clase-02-variables-y-tipos", "Las Cajas Etiquetadas en Memoria"),
            ("clase-03-control-flujo-condicionales", "El Semáforo y las Puertas Lógicas"),
            ("clase-04-control-flujo-bucles", "La Cinta Transportadora"),
            ("clase-05-listas-y-colecciones", "El Archivador y las Cajas Selladas"),
            ("clase-06-diccionarios", "La Agenda Telefónica y el Filtro de Únicos"),
            ("clase-07-funciones", "La Licuadora (Entradas ➔ Jugo)"),
            ("clase-08-proyecto-integrador-basico", "El Tablero de Control y el Casco (try/except)")
        ]
    },
    2: {
        "title": "Curso 2: Algoritmos Avanzados y Estructuras de Datos",
        "folder": "02-algoritmos-estructuras",
        "level": "Nivel 2 (Intermedio)",
        "classes": [
            ("clase-01-analisis-complejidad-big-o", "El Velocímetro y el Odómetro Big-O"),
            ("clase-02-pilas-y-colas", "La Pila de Platos y la Fila del Banco"),
            ("clase-03-tablas-hash-y-sets", "El Casillero Postal Inteligente"),
            ("clase-04-algoritmos-busqueda", "El Diccionario Abierto por la Mitad"),
            ("clase-05-algoritmos-ordenamiento", "El Organizador de Barajas de Cartas"),
            ("clase-06-arboles-binarios-busqueda", "El Árbol Genealógico de Decisiones"),
            ("clase-07-grafos-y-recorridos", "El Mapa de Metro y Vuelos"),
            ("clase-08-recursividad-y-programacion-dinamica", "Las Muñecas Rusas y el Bloc de Notas")
        ]
    },
    3: {
        "title": "Curso 3: Desarrollo de Agentes de Inteligencia Artificial",
        "folder": "03-agentes-ia",
        "level": "Nivel 3 (Avanzado)",
        "classes": [
            ("clase-01-fundamentos-llm-tokenizacion", "El Traductor de Sílabas y Piezas de LEGO"),
            ("clase-02-prompt-engineering-avanzado", "El Director de Cine y el Guión Técnico"),
            ("clase-03-salidas-estructuradas-pydantic", "El Inspector de Aduanas y el Formulario Rígido"),
            ("clase-04-tool-calling-funciones", "El Cinturón de Herramientas de Batman"),
            ("clase-05-embeddings-y-bases-vectoriales", "El Mapa de Constelaciones Semánticas"),
            ("clase-06-arquitecturas-rag", "El Estudiante con el Libro Abierto en el Examen"),
            ("clase-07-agentes-autonomos-react", "El Detective Privado (Pensar, Actuar, Observar)"),
            ("clase-08-sistemas-multi-agente", "La Agencia de Expertos Especializados")
        ]
    },
    4: {
        "title": "Curso 4: Taller Práctico & Proyecto Integrador Full-Stack",
        "folder": "04-proyecto-final",
        "level": "Nivel 4 (Profesional)",
        "classes": [
            ("clase-01-arquitectura-y-planificacion", "El Plano del Rascacielos Modular"),
            ("clase-02-backend-fastapi", "El Mesero de Restaurante de Alta Cocina"),
            ("clase-03-persistencia-sql-transacciones", "La Bóveda Acorazada y el Libro Mayor ACID"),
            ("clase-04-frontend-streamlit", "El Tablero de Mandos Interactivo"),
            ("clase-05-integracion-agente-ia", "El Asistente Inteligente en Vivo"),
            ("clase-06-testing-y-calidad", "El Laboratorio de Control de Calidad"),
            ("clase-07-docker-y-compose", "El Contenedor de Carga Estandarizado"),
            ("clase-08-despliegue-cicd-portafolio", "La Cinta de Ensamblaje Automatizada hacia Producción")
        ]
    }
}

def cmd_list(args):
    console.print(BANNER)
    
    table = Table(title="🗺️ Mapa Integral de Cursos y Clases Semanales", border_style="cyan")
    table.add_column("Curso", style="bold green", justify="center")
    table.add_column("Estado", justify="center")
    table.add_column("Semana", style="bold yellow", justify="center")
    table.add_column("Directorio de la Clase", style="bold white")
    table.add_column("Metáfora Didáctica", style="italic cyan")

    filter_course = getattr(args, "course", None)
    
    for c_num, data in COURSES_DATA.items():
        if filter_course and int(filter_course) != c_num:
            continue
        status_tag = "[bold green]✅ Activo[/bold green]"
        
        for idx, (folder, metaphor) in enumerate(data["classes"], start=1):
            table.add_row(
                f"C{c_num}",
                status_tag,
                f"S{idx:02d}",
                folder,
                f"«{metaphor}»"
            )
            
    console.print(table)
    console.print("\n💡 [bold yellow]Tip:[/bold yellow] Usa [bold cyan]wisrovi start <curso> <clase>[/bold cyan] o [bold cyan]wisrovi ui[/bold cyan] para abrir el Tutor Virtual Interactivo.")

def cmd_start(args):
    console.print(BANNER)
    try:
        c_num = int(args.course)
        clase_idx = int(args.clase)
        if c_num not in COURSES_DATA:
            console.print("[bold red]❌ Error:[/bold red] Curso inválido (elige 1, 2, 3 o 4).")
            sys.exit(1)

        from wisrovi_lib import GamificationEngine
        engine = GamificationEngine()
        is_unlocked = engine.is_class_unlocked(c_num, clase_idx)
        class_key = f"{c_num}-{clase_idx}"
        is_completed = class_key in engine.profile.completed_classes

        if not is_unlocked and not getattr(args, "force", False):
            console.print(Panel(
                f"[bold red]🔒 Clase C{c_num}-S{clase_idx:02d} Bloqueada[/bold red]\n\n"
                f"No puedes adelantar lecciones sin haber completado las anteriores.\n"
                f"Para acceder a esta clase, primero debes superar la lección previa.\n\n"
                f"💡 [bold yellow]Ruta recomendada:[/bold yellow] Usa [bold cyan]wisrovi ui[/bold cyan] para seguir el orden pedagógico con el Tutor Virtual.",
                title="⚠️ Bloqueo de Progresión Pedagógica",
                border_style="red"
            ))
            sys.exit(0)

        data = COURSES_DATA[c_num]
        folder, metaphor = data["classes"][clase_idx - 1]
    except Exception:
        console.print("[bold red]❌ Error:[/bold red] Curso o número de clase inválido. Ejemplo: [bold cyan]wisrovi start 1 1[/bold cyan]")
        sys.exit(1)
        
    class_path = os.path.join(data["folder"], folder)
    status_label = "[bold green]🔄 MODO REPASO Y PRÁCTICA LIBRE (Lección ya superada)[/bold green]" if is_completed else "[bold cyan]🚀 LECCIÓN ACTIVA EN CURSO[/bold cyan]"
    
    panel_content = f"""{status_label}

[bold yellow]Curso:[/bold yellow] {data['title']}
[bold yellow]Semana {clase_idx:02d}:[/bold yellow] {folder}
[bold yellow]Metáfora Central:[/bold yellow] [italic cyan]«{metaphor}»[/italic cyan]

[bold green]📁 Recursos de la Sesión:[/bold green]
• 📄 [bold white]Manual PDF Oficial:[/bold white] {class_path}/{folder}.pdf
• 📖 [bold white]Libro Digital:[/bold white] {class_path}/book.md
• 📓 [bold white]Cuaderno Jupyter:[/bold white] {class_path}/notebook/{folder}.ipynb
• 💻 [bold white]Ejemplos de Código:[/bold white] {class_path}/ejemplos/
• 🏋️ [bold white]Reto Práctico:[/bold white] {class_path}/ejercicios/reto.py

[bold cyan]🚀 Comandos de Trabajo Rápido:[/bold cyan]
• Ejecutar ejemplos: [bold white]python {class_path}/ejemplos/ejemplo_01_*/main.py[/bold white]
• Validar reto:       [bold white]pytest tests/curso_{c_num:02d}/test_clase_{clase_idx:02d}.py[/bold white]
"""
    console.print(Panel(panel_content, title=f"🚀 Sesión de Trabajo: {folder}", border_style="green"))

def cmd_test(args):
    console.print(BANNER)
    target = args.target
    test_folders = {
        "1": "tests/curso_01",
        "2": "tests/curso_02",
        "3": "tests/curso_03",
        "4": "tests/curso_04"
    }
    
    if not target or target == "all":
        console.print("[bold yellow]🧪 Ejecutando la suite completa de 34 pruebas centralizadas...[/bold yellow]\n")
        cmd = ["pytest", "-v", "tests/"]
    elif target in test_folders:
        name = COURSES_DATA[int(target)]["title"]
        console.print(f"[bold yellow]🧪 Ejecutando pruebas para {name} ({test_folders[target]}/)...[/bold yellow]\n")
        cmd = ["pytest", "-v", test_folders[target]]
    else:
        console.print(f"[bold yellow]🧪 Ejecutando pruebas en ruta personalizada: {target}...[/bold yellow]\n")
        cmd = ["pytest", "-v", target]
        
    res = subprocess.run(cmd)
    if res.returncode == 0:
        console.print("\n[bold green]✅ ¡100% de las pruebas pasadas con éxito! Código con calidad certificada.[/bold green]")
    else:
        console.print("\n[bold red]❌ Se detectaron fallos en las pruebas. Revisa la traza de Pytest para depurar tu solución.[/bold red]")
    sys.exit(res.returncode)

def cmd_solve(args):
    console.print(BANNER)
    try:
        c_num = int(args.course)
        clase_idx = int(args.clase)
        data = COURSES_DATA[c_num]
        folder, _ = data["classes"][clase_idx - 1]
    except Exception:
        console.print("[bold red]❌ Error:[/bold red] Curso o clase inválido. Ejemplo: [bold cyan]wisrovi solve 1 1[/bold cyan]")
        sys.exit(1)
        
    test_file = f"tests/curso_{c_num:02d}/test_clase_{clase_idx:02d}.py"
    console.print(f"[bold yellow]🔍 Evaluando tu solución en:[/bold yellow] [bold white]{data['folder']}/{folder}/ejercicios/reto.py[/bold white]\n")
    
    res = subprocess.run(["pytest", "-v", test_file])
    if res.returncode == 0:
        console.print(Panel(f"🎉 [bold green]¡FELICITACIONES! Has superado el reto de la Semana {clase_idx:02d} ({folder}).[/bold green]\nTu lógica cumple con todos los contratos de tipado y casos de prueba.", border_style="green"))
    else:
        console.print(Panel(f"⚠️ [bold red]El reto aún no pasa todas las aserciones.[/bold red]\nRevisa el archivo [bold cyan]{test_file}[/bold cyan] para ver qué casos extremos o valores de retorno están fallando.", border_style="red"))
    sys.exit(res.returncode)

def cmd_docs(args):
    console.print(BANNER)
    url = "https://academy_python.wisrovi.dev/"
    if getattr(args, "serve", False):
        console.print("[bold green]🚀 Iniciando servidor local de documentación con MkDocs Material...[/bold green]")
        subprocess.run(["mkdocs", "serve"])
    else:
        console.print(f"[bold green]🌐 Abriendo la plataforma web en tu navegador:[/bold green] [bold cyan]{url}[/bold cyan]")
        webbrowser.open(url)

def cmd_info():
    console.print(BANNER)
    info_panel = """[bold white]Director Académico & Arquitecto:[/bold white] [bold cyan]William Rodríguez (Wisrovi)[/bold cyan]
[bold white]Ubicación:[/bold white] Badajoz, España
[bold white]Sitio Web Oficial:[/bold white] https://wisrovi.dev
[bold white]Repositorio GitHub:[/bold white] https://github.com/wisrovi/wisrovi-python
[bold white]Plataforma Web Docs:[/bold white] https://academy_python.wisrovi.dev/
[bold white]PyPI Open Source Suite:[/bold white] https://pypi.org/user/wisrovi/ (26+ Librerías publicadas)
"""
    console.print(Panel(info_panel, title="ℹ️ Información del Programa & Autor", border_style="cyan"))

def cmd_ui(args):
    console.print(BANNER)
    port = getattr(args, "port", 8501)
    host = getattr(args, "host", "127.0.0.1")
    c_num = getattr(args, "course", None)
    cls_num = getattr(args, "clase", None)
    
    query = []
    if c_num: query.append(f"course={c_num}")
    if cls_num: query.append(f"class={cls_num}")
    q_str = f"?{'&'.join(query)}" if query else ""
    
    url = f"http://{host}:{port}/{q_str}"
    console.print(f"[bold green]🚀 Iniciando Wisrovi Interactive Studio (Modo Estudiante):[/bold green] [bold cyan]{url}[/bold cyan]")
    console.print("[dim]Presiona CTRL+C para detener el servidor.[/dim]\n")
    
    import threading
    import time
    def _open_browser():
        time.sleep(1.2)
        webbrowser.open(url)
    threading.Thread(target=_open_browser, daemon=True).start()
    
    try:
        from wisrovi_lib.server import start_server
        start_server(host=host, port=port)
    except Exception as e:
        console.print(f"[bold red]Error al iniciar servidor FastAPI:[/bold red] {e}")

def cmd_tutor(args):
    console.print(BANNER)
    port = getattr(args, "port", 8501)
    host = getattr(args, "host", "127.0.0.1")
    c_num = getattr(args, "course", None)
    cls_num = getattr(args, "clase", None)
    
    query = ["mode=tutor"]
    if c_num: query.append(f"course={c_num}")
    if cls_num: query.append(f"class={cls_num}")
    q_str = f"?{'&'.join(query)}"
    
    url = f"http://{host}:{port}/tutor{q_str}"
    console.print(Panel(
        f"[bold magenta]👨‍🏫 Iniciando Modo Presentador / Docente en Vivo (Wisrovi Master Deck):[/bold magenta]\n"
        f"URL: [bold cyan]{url}[/bold cyan]\n"
        f"• [bold green]Acceso Maestro:[/bold green] Las 32 clases desbloqueadas sin restricciones de gamificación.\n"
        f"• [bold green]Herramientas:[/bold green] Live Coding, Guía Pedagógica del Mentor, Notas de Aula y Temporizador de Retos.",
        title="👑 Consola del Instructor / Tutor",
        border_style="magenta"
    ))
    console.print("[dim]Presiona CTRL+C para detener el servidor.[/dim]\n")
    
    import threading
    import time
    def _open_browser():
        time.sleep(1.2)
        webbrowser.open(url)
    threading.Thread(target=_open_browser, daemon=True).start()
    
    try:
        from wisrovi_lib.server import start_server
        start_server(host=host, port=port)
    except Exception as e:
        console.print(f"[bold red]Error al iniciar servidor FastAPI:[/bold red] {e}")

def cmd_cert(args):
    console.print(BANNER)
    from wisrovi_lib import CertificateGenerator, GamificationEngine
    engine = GamificationEngine()
    s_name = getattr(args, "name", None) or engine.profile.name or "Estudiante Wisrovi"
    c_num = getattr(args, "course", None)
    cls_num = getattr(args, "clase", None)
    out_format = getattr(args, "format", "pdf")
    output_path = getattr(args, "output", None)

    if c_num and cls_num:
        console.print(f"[bold green]🎓 Generando Micro-Diploma de Clase:[/bold green] Curso {c_num} - Clase 0{cls_num} ({s_name})...")
        payload = CertificateGenerator.get_class_share_payload(s_name, int(c_num), int(cls_num))
        default_filename = f"Diploma_Wisrovi_C{c_num}_Clase{int(cls_num):02d}.{out_format}"
        out_file = output_path or default_filename
        
        if out_format.lower() == "png":
            CertificateGenerator.generate_class_certificate_png(s_name, int(c_num), int(cls_num), out_file)
        else:
            CertificateGenerator.generate_class_certificate_pdf(s_name, int(c_num), int(cls_num), out_file)
            
        console.print(f"[bold green]✅ Diploma exportado con éxito en:[/bold green] [bold cyan]{out_file}[/bold cyan]")
        console.print(Panel(payload["linkedin_text"], title="💼 Texto Oficial para Publicar en LinkedIn", border_style="cyan"))
    else:
        console.print(f"[bold green]🏆 Generando Master Diploma Oficial (160 Horas):[/bold green] {s_name}...")
        course_title = "Programa Integral de Formación en Python: De Cero a Agentes de IA"
        default_filename = f"Master_Diploma_Wisrovi_Python_160h.{out_format}"
        out_file = output_path or default_filename
        
        if out_format.lower() == "png":
            CertificateGenerator.generate_master_certificate_png(s_name, course_title, 160, out_file)
        else:
            CertificateGenerator.generate_pdf_certificate(s_name, course_title, 160, out_file)
            
        console.print(f"[bold green]✅ Master Diploma exportado con éxito en:[/bold green] [bold cyan]{out_file}[/bold cyan]")

def cmd_profile(args):
    console.print(BANNER)
    from wisrovi_lib import GamificationEngine, BADGES
    engine = GamificationEngine()
    p = engine.profile

    grid_table = Table(title="🗺️ Matriz de Avance en las 32 Clases", border_style="cyan")
    grid_table.add_column("Curso", style="bold green", justify="center")
    grid_table.add_column("Progreso", style="bold yellow", justify="center")
    for i in range(1, 9):
        grid_table.add_column(f"S{i:02d}", justify="center")

    for c in range(1, 5):
        row = [f"Curso {c}"]
        completed_in_c = sum(1 for i in range(1, 9) if f"{c}-{i}" in p.completed_classes)
        row.append(f"{completed_in_c}/8 ({int(completed_in_c/8*100)}%)")
        for i in range(1, 9):
            key = f"{c}-{i}"
            row.append("🟩" if key in p.completed_classes else "⬜")
        grid_table.add_row(*row)

    xp_pct = min(100, int((p.xp % 500) / 500 * 100))
    bar_len = 25
    filled = int(bar_len * (xp_pct / 100))
    bar_str = "█" * filled + "░" * (bar_len - filled)

    badges_list = []
    for b_id in p.unlocked_badges:
        if b_id in BADGES:
            badges_list.append(f"{BADGES[b_id]['icon']} [bold white]{BADGES[b_id]['title']}[/bold white]")

    badges_str = "  ".join(badges_list) if badges_list else "[italic dim]Completa retos para desbloquear insignias.[/italic dim]"

    profile_text = f"""[bold white]Alumno:[/bold white] [bold cyan]{p.name}[/bold cyan] ({p.email})
[bold white]Rango:[/bold white] [bold yellow]Nivel {p.level} • {p.level_title}[/bold yellow]
[bold white]Experiencia (XP):[/bold white] [bold green]{p.xp} XP[/bold green]  [{bar_str}] {xp_pct}% para Nivel {p.level + 1}
[bold white]Racha de Estudio:[/bold white] 🔥 [bold red]{p.streak_days} días consecutivos[/bold red]
[bold white]Total Clases Superadas:[/bold white] [bold green]{len(p.completed_classes)} / 32[/bold green] ({int(len(p.completed_classes)/32*100)}%)

[bold white]🏆 Insignias y Trofeos Desbloqueados:[/bold white]
{badges_str}
"""
    console.print(Panel(profile_text, title="👤 Perfil del Estudiante & Gamificación", border_style="green"))
    console.print(grid_table)

def cmd_book(args):
    console.print(BANNER)
    try:
        c_num = int(args.course)
        cls_num = int(args.clase)
        data = COURSES_DATA[c_num]
        folder, _ = data["classes"][cls_num - 1]
    except Exception:
        console.print("[bold red]❌ Error:[/bold red] Curso o clase inválido. Ejemplo: [bold cyan]wisrovi book 1 1[/bold cyan]")
        sys.exit(1)

    book_path = os.path.join(data["folder"], folder, "book.md")
    if not os.path.exists(book_path):
        console.print(f"[bold red]❌ Archivo no encontrado:[/bold red] {book_path}")
        sys.exit(1)

    with open(book_path, "r", encoding="utf-8") as f:
        content = f.read()

    console.print(Markdown(content))

def cmd_benchmark(args):
    """Ejecuta benchmark de tiempo y memoria sobre la solución de una clase."""
    console.print(BANNER)
    try:
        c_num = int(args.course)
        s_num = int(args.clase)
    except Exception:
        console.print("[bold red]❌ Error:[/bold red] Parámetros inválidos. Ejemplo: [bold cyan]wisrovi benchmark 1 2[/bold cyan]")
        return
        
    if c_num not in COURSES_DATA or s_num < 1 or s_num > len(COURSES_DATA[c_num]["classes"]):
        console.print(f"[bold red]❌ Error: Curso {c_num} o Clase {s_num} no válidos.[/bold red]")
        return
        
    class_folder = COURSES_DATA[c_num]["classes"][s_num - 1][0]
    course_folder = COURSES_DATA[c_num]["folder"]
    reto_path = os.path.join(os.getcwd(), course_folder, class_folder, "ejercicios", "reto.py")
    
    if not os.path.exists(reto_path):
        console.print(f"[bold red]❌ Archivo reto.py no encontrado en: {reto_path}[/bold red]")
        return
        
    with open(reto_path, "r", encoding="utf-8") as f:
        code = f.read()
        
    from wisrovi_lib.memory_inspector import MemoryInspector
    try:
        res = MemoryInspector.benchmark_code(code, iterations=getattr(args, "iterations", 50))
        console.print(Panel(
            f"[bold green]⚡ Benchmark de Rendimiento - Curso {c_num} Clase 0{s_num}[/bold green]\n\n"
            f"[cyan]📁 Archivo:[/cyan] {reto_path}\n"
            f"[yellow]⏱️ Tiempo Promedio:[/yellow] [bold white]{res['avg_time_microseconds']} µs[/bold white]\n"
            f"[yellow]⚡ Mejor Tiempo (Min):[/yellow] [bold white]{res['min_time_microseconds']} µs[/bold white]\n"
            f"[magenta]💾 Memoria Heap Pico:[/magenta] [bold white]{res['peak_memory_kb']} KB ({res['peak_memory_bytes']} bytes)[/bold white]\n"
            f"[bold white]🏆 Calificación Big-O:[/bold white] {res['speed_grade']}",
            title="🔬 Laboratorio de Rendimiento Big-O (Wisrovi Studio)",
            border_style="cyan"
        ))
    except Exception as e:
        console.print(f"[bold red]❌ Error al ejecutar benchmark: {e}[/bold red]")

def cmd_lint(args):
    """Ejecuta análisis estático AST y linter pedagógico Wisrovi."""
    console.print(BANNER)
    try:
        c_num = int(args.course)
        s_num = int(args.clase)
    except Exception:
        console.print("[bold red]❌ Error:[/bold red] Parámetros inválidos. Ejemplo: [bold cyan]wisrovi lint 1 2[/bold cyan]")
        return
        
    if c_num not in COURSES_DATA or s_num < 1 or s_num > len(COURSES_DATA[c_num]["classes"]):
        console.print(f"[bold red]❌ Error: Curso {c_num} o Clase {s_num} no válidos.[/bold red]")
        return
        
    class_folder = COURSES_DATA[c_num]["classes"][s_num - 1][0]
    course_folder = COURSES_DATA[c_num]["folder"]
    reto_path = os.path.join(os.getcwd(), course_folder, class_folder, "ejercicios", "reto.py")
    
    if not os.path.exists(reto_path):
        console.print(f"[bold red]❌ Archivo reto.py no encontrado en: {reto_path}[/bold red]")
        return
        
    with open(reto_path, "r", encoding="utf-8") as f:
        code = f.read()
        
    from wisrovi_lib.memory_inspector import MemoryInspector
    diagnostics = MemoryInspector.lint_code(code)
    
    if not diagnostics:
        console.print(Panel(
            f"[bold green]✨ ¡Código 100% Pythonic y Limpio![/bold green]\n"
            f"No se detectaron antipatrones ni problemas de tipado en {class_folder}/ejercicios/reto.py.",
            title="🎯 Diagnóstico PEP 8 / Wisrovi",
            border_style="green"
        ))
    else:
        table = Table(title=f"🔍 Diagnósticos Pedagógicos - Curso {c_num} Clase 0{s_num}", border_style="yellow")
        table.add_column("Línea", justify="center", style="bold cyan")
        table.add_column("Tipo", justify="center")
        table.add_column("Regla", style="bold magenta")
        table.add_column("Mensaje & Sugerencia", style="white")
        
        for d in diagnostics:
            sev_badge = "[bold red]ERROR[/bold red]" if d["severity"] == "error" else ("[bold yellow]AVISO[/bold yellow]" if d["severity"] == "warning" else "[bold blue]TIP[/bold blue]")
            table.add_row(
                str(d["line"]),
                sev_badge,
                d["code"],
                f"{d['message']}\n[italic dim]{d.get('hint', '')}[/italic dim]"
            )
        console.print(table)

def main():
    parser = argparse.ArgumentParser(
        description="Wisrovi CLI - Asistente de Aprendizaje en Python & Consola del Docente",
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command")

    # ui (Modo Estudiante)
    p_ui = subparsers.add_parser("ui", help="Lanza el Estudio de Aprendizaje Guiado en el navegador (Modo Estudiante)")
    p_ui.add_argument("--port", type=int, default=8501, help="Puerto del servidor (defecto: 8501)")
    p_ui.add_argument("--host", type=str, default="127.0.0.1", help="Host del servidor (defecto: 127.0.0.1)")
    p_ui.add_argument("-c", "--course", type=int, default=None, help="Abrir directamente en el curso especificado (1..4)")
    p_ui.add_argument("-s", "--clase", type=int, default=None, help="Abrir directamente en la clase especificada (1..8)")

    # tutor (Modo Presentador / Docente en Vivo)
    p_tutor = subparsers.add_parser("tutor", help="Lanza el Modo Presentador / Docente en Vivo con acceso maestro a las 32 clases")
    p_tutor.add_argument("--port", type=int, default=8501, help="Puerto del servidor (defecto: 8501)")
    p_tutor.add_argument("--host", type=str, default="127.0.0.1", help="Host del servidor (defecto: 127.0.0.1)")
    p_tutor.add_argument("-c", "--course", type=int, default=None, help="Curso inicial para proyectar (1..4)")
    p_tutor.add_argument("-s", "--clase", type=int, default=None, help="Clase inicial para proyectar (1..8)")

    # cert (Generación de Diplomas y Micro-Acreditaciones)
    p_cert = subparsers.add_parser("cert", help="Genera y exporta diplomas oficiales en PDF o PNG")
    p_cert.add_argument("-n", "--name", type=str, default=None, help="Nombre del estudiante")
    p_cert.add_argument("-c", "--course", type=int, default=None, help="Número de curso (1..4) para micro-diploma")
    p_cert.add_argument("-s", "--clase", type=int, default=None, help="Número de clase (1..8) para micro-diploma")
    p_cert.add_argument("-f", "--format", type=str, choices=["pdf", "png"], default="pdf", help="Formato de exportación (pdf/png)")
    p_cert.add_argument("-o", "--output", type=str, default=None, help="Ruta de guardado personalizada")

    # profile / stats
    subparsers.add_parser("profile", help="Muestra el perfil del alumno, nivel, XP y trofeos")
    subparsers.add_parser("stats", help="Alias de 'profile'")

    # book
    p_book = subparsers.add_parser("book", help="Muestra el libro digital canónico (6 capítulos) de una clase")
    p_book.add_argument("course", help="Número de curso (1 a 4)")
    p_book.add_argument("clase", help="Número de clase (1 a 8)")

    # list
    p_list = subparsers.add_parser("list", help="Muestra la tabla de cursos y clases")
    p_list.add_argument("course", nargs="?", default=None, help="Número de curso (1, 2, 3, 4) opcional")

    # start
    p_start = subparsers.add_parser("start", help="Prepara e inicia una sesión de clase")
    p_start.add_argument("course", help="Número de curso (1 a 4)")
    p_start.add_argument("clase", help="Número de clase (1 a 8)")

    # test
    p_test = subparsers.add_parser("test", help="Ejecuta la suite de pruebas unitarias (Pytest)")
    p_test.add_argument("target", nargs="?", default="all", help="Número de curso (1..4) o ruta específica")

    # solve
    p_solve = subparsers.add_parser("solve", help="Evalúa el reto práctico de una clase específica")
    p_solve.add_argument("course", help="Número de curso (1 a 4)")
    p_solve.add_argument("clase", help="Número de clase (1 a 8)")

    # benchmark
    p_bench = subparsers.add_parser("benchmark", help="Mide tiempo de CPU (µs) y memoria heap de una solución")
    p_bench.add_argument("course", help="Número de curso (1 a 4)")
    p_bench.add_argument("clase", help="Número de clase (1 a 8)")
    p_bench.add_argument("-i", "--iterations", type=int, default=50, help="Número de iteraciones para promedio (defecto: 50)")

    # lint
    p_lint = subparsers.add_parser("lint", help="Analiza código con el linter pedagógico y buenas prácticas PEP 8")
    p_lint.add_argument("course", help="Número de curso (1 a 4)")
    p_lint.add_argument("clase", help="Número de clase (1 a 8)")

    # docs
    p_docs = subparsers.add_parser("docs", help="Abre la plataforma web o lanza el servidor local")
    p_docs.add_argument("--serve", action="store_true", help="Inicia 'mkdocs serve' localmente")

    # info
    subparsers.add_parser("info", help="Muestra información del autor y enlaces oficiales")

    args = parser.parse_args()

    if args.command == "ui":
        cmd_ui(args)
    elif args.command == "tutor":
        cmd_tutor(args)
    elif args.command == "cert":
        cmd_cert(args)
    elif args.command in ("profile", "stats"):
        cmd_profile(args)
    elif args.command == "book":
        cmd_book(args)
    elif args.command == "benchmark":
        cmd_benchmark(args)
    elif args.command == "lint":
        cmd_lint(args)
    elif args.command == "list":
        cmd_list(args)
    elif args.command == "start":
        cmd_start(args)
    elif args.command == "test":
        cmd_test(args)
    elif args.command == "solve":
        cmd_solve(args)
    elif args.command == "docs":
        cmd_docs(args)
    elif args.command == "info":
        cmd_info()
    else:
        cmd_list(args)

if __name__ == "__main__":
    main()
