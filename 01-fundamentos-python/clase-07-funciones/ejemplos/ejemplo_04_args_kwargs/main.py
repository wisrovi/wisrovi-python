"""Ejemplo 04: *args y **kwargs."""
def registrar_evento(nombre_evento: str, *etiquetas, **metadatos):
    print(f"Evento: {nombre_evento}")
    print(f"Etiquetas: {etiquetas}")
    print(f"Metadatos: {metadatos}")

registrar_evento("Login_Usuario", "auth", "seguridad", ip="192.168.1.1", user_id=101)
