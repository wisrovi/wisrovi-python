"""Ejemplo 01: Tipos Primitivos, Type Hints (PEP 484) y Funciones Modulares."""


def crear_perfil_usuario(
    nombre: str,
    edad: int,
    altura: float,
    es_estudiante: bool,
) -> str:
    """Combina variables de diferentes tipos primitivos en un reporte formateado."""
    
    if es_estudiante == True:
        categoria = "Estudiante Activo"
    else:
        categoria = "Profesional / Graduado"

    # categoria = "Estudiante Activo" if es_estudiante else "Profesional / Graduado"

    resumen = (
        f"--- FICHA DE USUARIO ---\n"
        f"Nombre:     {nombre} (Tipo: {type(nombre).__name__})\n"
        f"Edad:       {edad} años (Tipo: {type(edad).__name__})\n"
        f"Altura:     {altura:.2f} m (Tipo: {type(altura).__name__})\n"
        f"Condición:  {categoria} (Tipo booleano: {type(es_estudiante).__name__})"
    )
    return resumen


# Declaración de variables tipadas
nombre_usuario: str = "Wisrovi"
edad_usuario: int = 30
altura_usuario: float = 1.78
activo: bool = False

# Llamada a la función con paso de variables
perfil_generado = crear_perfil_usuario(
    nombre=nombre_usuario,
    edad=edad_usuario,
    altura=altura_usuario,
    es_estudiante=activo,
)

print(perfil_generado)
