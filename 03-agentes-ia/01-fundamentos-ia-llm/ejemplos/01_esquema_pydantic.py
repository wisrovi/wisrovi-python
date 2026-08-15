"""Validación estricta de respuestas de IA con Pydantic V2."""
from pydantic import BaseModel, Field

class ResumenEjecutivo(BaseModel):
    titulo: str = Field(description="Título corto del artículo")
    puntos_clave: list[str] = Field(min_length=1)
    sentimiento_general: str = Field(pattern="^(POSITIVO|NEGATIVO|NEUTRO)$")
    score_relevancia: float = Field(ge=0.0, le=1.0)

# Simulación de respuesta JSON de LLM
raw_json = """{
    "titulo": "Lanzamiento de Python 3.12",
    "puntos_clave": ["Mejoras de rendimiento", "Sintaxis de tipos más clara", "Mensajes de error optimizados"],
    "sentimiento_general": "POSITIVO",
    "score_relevancia": 0.95
}"""

resumen = ResumenEjecutivo.model_validate_json(raw_json)
print(f"Resumen validado: {resumen.titulo} - Score: {resumen.score_relevancia}")
