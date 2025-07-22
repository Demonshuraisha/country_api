from fastapi import APIRouter
from models import Country
import json

router = APIRouter()

# Chargement des pays
with open('country.json', 'r', encoding='utf-8') as f:
    country_list = json.load(f)
list_country = {k+1: v for k, v in enumerate(country_list)}

@router.get("/monnaie")
def get_all_monnaie() -> list[str]:
    monnaies = set()
    for country in list_country:
        if "monnaie" in list_country[country]:
            monnaies.add(list_country[country]["monnaie"])
    return sorted(monnaies)

@router.get("/continent")
def get_all_continent() -> list[str]:
    continent = set()
    for country in list_country:
        if "continent" in list_country[country]:
            continent.add(list_country[country]["continent"])
    return sorted(continent)

@router.get("/langue")
def get_all_langue() -> list[str]:
    langues = set()
    for country in list_country:
        if "langues_officielles" in list_country[country]:
            for langue in list_country[country]["langues_officielles"]:
                langues.add(langue)
    return sorted(langues) 