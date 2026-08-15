"""Paso de Mensajes Tipado."""
from pydantic import BaseModel
class Msg(BaseModel): sender: str; content: str
print(Msg(sender='AgentA', content='Listo'))
