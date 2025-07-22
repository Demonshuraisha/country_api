from fastapi import APIRouter, Path, HTTPException
from models import Country
import json
from dataclasses import asdict

router = APIRouter()

# Chargement des pays
with open('country.json', 'r', encoding='utf-8') as f:
    country_list = json.load(f)
list_country = {k+1: v for k, v in enumerate(country_list)}

@router.get("/total_country")
def get_total_country() -> dict:
    return {"total_country": len(list_country)}

@router.get("/country")
def get_all_country() -> list[Country]:
    return [Country(**list_country[id]) for id in list_country]

@router.get("/country/search")
def get_country_by_name(name: str) -> list[Country]:
    """
    Recherche les pays dont le nom contient la chaîne 'name' (insensible à la casse).
    """
    return [
        Country(**list_country[country_id])
        for country_id in list_country
        if name.lower() in list_country[country_id]["nom"].lower()
    ]

@router.get("/country/{id}")
def get_country_by_id(id: int = Path(ge=1)) -> Country:
    if id not in list_country:
        raise HTTPException(status_code=404, detail="Country not found")
    return Country(**list_country[id])

@router.post("/country/")
def create_country(country: Country) -> Country:
    if country.id in list_country:
        raise HTTPException(status_code=400, detail="Country already exists")
    list_country[country.id] = asdict(country)
    return country

@router.put("/country/{id}")
def update_country(country: Country, id: int = Path(ge=1)) -> Country:
    if id not in list_country:
        raise HTTPException(status_code=404, detail="Country not found")
    list_country[id] = asdict(country)
    return country

@router.delete("/country/{id}")
def delete_country(id: int = Path(ge=1)) -> Country:
    if id in list_country:
        country = Country(**list_country[id])
        del list_country[id]
        return country
    else:
        raise HTTPException(status_code=404, detail="Country not found") 