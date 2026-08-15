#!/usr/bin/env python3
"""
CLI interactiva para estudiantes del curso wisrovi-python.
Permite ejecutar tests por clase, consultar el progreso y abrir recursos.
"""

import sys
import subprocess
import argparse

BANNER = r"""
  _       _                           _ 
 \ \     / (_)___ _ __ _____   _____ (_)
  \ \ /\ / /| / __| '__/ _ \ \ / / \ \/ /
   \ V  V / | \__ \ | | (_) \ V / | |>  < 
    \_/\_/  |_|___/_|  \___/ \_/  |_/_/\_\
   🐍 Programa de Formación en Python: De Cero a Agentes de IA
"""

COURSES = {
    "1": ("Curso 1: Fundamentos Básicos de Python", "01-fundamentos-python"),
    "2": ("Curso 2: Algoritmos y Estructuras de Datos", "02-algoritmos-estructuras"),
    "3": ("Curso 3: Creación y Desarrollo de Agentes de IA", "03-agentes-ia"),
    "4": ("Curso 4: Taller Práctico & Proyecto Final", "04-proyecto-final")
}

def cmd_status():
    print(BANNER)
    print("🗺️  ESTADO DEL PROGRAMA DE FORMACIÓN:")
    print("=" * 60)
    for k, (name, path) in COURSES.items():
        print(f"  [{k}] 🟢 {name} ({path}/)")
    print("=" * 60)
    print("\n💡 Tip: Ejecuta 'wisrovi test 1' para probar los ejercicios del Curso 1.")

def cmd_test(args):
    target = args.target
    print(BANNER)
    test_folders = {
        "1": "tests/curso_01",
        "2": "tests/curso_02",
        "3": "tests/curso_03",
        "4": "tests/curso_04"
    }
    if not target or target == "all":
        print("🧪 Ejecutando TODAS las suites de pruebas en /tests...")
        cmd = ["pytest", "-v", "tests/"]
    elif target in test_folders:
        name, _ = COURSES[target]
        print(f"🧪 Ejecutando pruebas para {name} ({test_folders[target]}/)...")
        cmd = ["pytest", "-v", test_folders[target]]
    else:
        print(f"🧪 Ejecutando pruebas en: {target}...")
        cmd = ["pytest", "-v", target]
        
    res = subprocess.run(cmd)
    sys.exit(res.returncode)

def cmd_docs():
    print(BANNER)
    print("🌐 Documentación interactiva del curso:")
    print("   Enlace en vivo: https://wisrovi.github.io/wisrovi-python/")
    print("   Código fuente:  docs/")
    print("\nPara iniciar el servidor local de MkDocs ejecuta:")
    print("   pip install -e '.[docs]' && mkdocs serve")

def main():
    parser = argparse.ArgumentParser(
        description="Wisrovi CLI - Asistente de Aprendizaje en Python"
    )
    subparsers = parser.add_subparsers(dest="command")

    # Comando status
    subparsers.add_parser("status", help="Muestra el mapa y estado de los cursos")

    # Comando test
    test_p = subparsers.add_parser("test", help="Ejecuta los tests automatizados (pytest)")
    test_p.add_argument("target", nargs="?", default="all", help="Número de curso (1, 2, 3, 4) o ruta específica")

    # Comando docs
    subparsers.add_parser("docs", help="Muestra información sobre la documentación interactiva")

    args = parser.parse_args()

    if args.command == "status":
        cmd_status()
    elif args.command == "test":
        cmd_test(args)
    elif args.command == "docs":
        cmd_docs()
    else:
        cmd_status()

if __name__ == "__main__":
    main()
