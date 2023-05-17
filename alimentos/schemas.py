from ninja import Schema
from typing import List, Dict

class Alimento(Schema):
    titulo: str
    quantidade: int