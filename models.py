from dataclasses import dataclass

@dataclass
class Country:
    id: int
    nom: str
    capitale: str
    région: str
    continent: str
    estimation_population_2023: int
    superficie_km2: int
    monnaie: str
    langues_officielles: list[str] 