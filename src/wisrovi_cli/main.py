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
    table.add_column("Semana", style="bold yellow", justify="center")
    table.add_column("Directorio de la Clase", style="bold white")
    table.add_column("Metáfora Didáctica", style="italic cyan")

    filter_course = getattr(args, "course", None)
    
    for c_num, data in COURSES_DATA.items():
        if filter_course and int(filter_course) != c_num:
            continue
        for idx, (folder, metaphor) in enumerate(data["classes"], start=1):
            table.add_row(
                f"C{c_num}",
                f"S{idx:02d}",
                folder,
                f"«{metaphor}»"
            )
            
    console.print(table)
    console.print("\n💡 [bold yellow]Tip:[/bold yellow] Usa [bold cyan]wisrovi start <curso> <clase>[/bold cyan] para abrir una sesión de trabajo.")

def cmd_start(args):
    console.print(BANNER)
    try:
        c_num = int(args.course)
        clase_idx = int(args.clase)
        data = COURSES_DATA[c_num]
        folder, metaphor = data["classes"][clase_idx - 1]
    except Exception:
        console.print("[bold red]❌ Error:[/bold red] Curso o número de clase inválido. Ejemplo: [bold cyan]wisrovi start 1 1[/bold cyan]")
        sys.exit(1)
        
    class_path = os.path.join(data["folder"], folder)
    
    panel_content = f"""[bold yellow]Curso:[/bold yellow] {data['title']}
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

def main():
    parser = argparse.ArgumentParser(
        description="Wisrovi CLI - Asistente de Aprendizaje en Python",
        formatter_class=argparse.RawTextHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command")

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

    # docs
    p_docs = subparsers.add_parser("docs", help="Abre la plataforma web o lanza el servidor local")
    p_docs.add_argument("--serve", action="store_true", help="Inicia 'mkdocs serve' localmente")

    # info
    subparsers.add_parser("info", help="Muestra información del autor y enlaces oficiales")

    args = parser.parse_args()

    if args.command == "list":
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
