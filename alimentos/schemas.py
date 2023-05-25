from ninja import Schema, ModelSchema
from typing import List, Dict
from .models import Alimento as ModelAlimento

class Alimento(ModelSchema):
    novo_campo: int[int] = []

    class Config(Schema.Config):
        model = ModelAlimento
        model_fields = ['id', 'quantidade']
        anystr_lower = True
        anystr_strip_whitespace = True
        allow_mutation = False