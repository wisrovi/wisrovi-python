"""Ejemplo 01: CRUD en Diccionarios."""
perfil = {
    "usuario": "wisrovi",
    "rol": "Architect",
    "activo": True
}

# Lectura segura con valor por defecto
email = perfil.get("email", "no_registrado@dev.com")
perfil["nivel"] = "Senior"

print(f"Usuario: {perfil['usuario']} | Rol: {perfil['rol']} | Email: {email}")
