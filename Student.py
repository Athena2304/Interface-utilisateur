from dataclasses import dataclass

# creation de la dataclass qui aura les informations des élèves
@dataclass
class Student:
    noms: str
    description: str
    participation: float