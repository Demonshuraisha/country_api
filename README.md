# Country API

API Python pour la gestion et la consultation de données sur les pays du monde.

## Description
Ce projet permet de manipuler, rechercher et exposer des informations sur les pays à partir d’un fichier JSON, via des routes organisées en modules.

## Fonctionnalités
- Consultation des données de pays (nom, code, etc.)
- API modulaire avec organisation par routes
- Chargement des données depuis un fichier JSON

## Installation

1. Clonez le dépôt :
   ```sh
   git clone https://github.com/Demonshuraisha/country_api
   cd country_api
   ```
2. (Optionnel) Créez un environnement virtuel :
   ```sh
   python -m venv env
   source env/bin/activate  # ou env\Scripts\activate sous Windows
   ```
3. Installez les dépendances :
   ```sh
   pip install -r requirements.txt
   ```

## Utilisation

Lancez l’API avec :
```sh
uvicorn main:app --reload
```

## Structure du projet
- `main.py` : point d’entrée de l’application
- `models.py` : définitions des modèles de données
- `routes/` : routes de l’API (country, extra, ...)
- `country.json` : données des pays

## Auteur
- [Votre nom]

## Licence
Ce projet est sous licence MIT. 