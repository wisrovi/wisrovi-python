"""Exportación de JSON Schema."""
from pydantic import BaseModel
class Task(BaseModel): title: str
print(Task.model_json_schema())
