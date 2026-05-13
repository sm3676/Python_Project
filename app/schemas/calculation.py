from pydantic import ConfigDict
from pydantic import BaseModel
from typing import Literal

class CalculationCreate(BaseModel):
    operand1: float
    operand2: float

    operation: Literal[
        "add",
        "subtract",
        "multiply",
        "divide",
        "power",
        "mod"
    ]

# 👉 response model
class CalculationResponse(BaseModel):
    id: int
    operand1: float
    operand2: float
    operation: str
    result: float

    model_config = ConfigDict(from_attributes=True)