"""Restricciones con Field()."""
from pydantic import BaseModel, Field
class Prod(BaseModel): price: float = Field(ge=0.0)
print(Prod(price=19.99))
