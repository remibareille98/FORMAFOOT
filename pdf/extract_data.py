import json
import os


def import_from_json(filename: str) -> list[dict]:
    with open(filename, "r", encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)
    return data


data = import_from_json(os.path.abspath("ressources/api object/api.json"))

# Infos page 1
titre = data["titre"]
description = data["description"]

# Infos page 2
financable = data["financeable"]
prix = data.get("prix")
apports = data["apports"]
prerequis = data["prerequis"]
createur = data["createur"]["nom"] + " " + data["createur"]["prenom"]
# Durée
# Exemple de format : "02:00:00"


def parse_duree_to_int(duree: str) -> tuple[int, int, int]:
    heures, minutes, secondes = map(int, duree.split(":"))

    return heures, minutes, secondes


def get_documents_duree(data):
    documents_duree = []
    for structure in data["structure"]:
        for chapitre in structure["chapitres"]:
            for subchapitre in chapitre["subchapitre"]:
                for document in subchapitre["documents"]:
                    documents_duree.append(document["duree"])
    return documents_duree


def get_duree_total_en_secondes(documents_duree: list[str]):
    duree_total_seconds = 0
    for document in documents_duree:
        heures, minutes, secondes = parse_duree_to_int(document)
        duree_seconds = heures * 3600 + minutes * 60 + secondes
        duree_total_seconds += duree_seconds
    return duree_total_seconds


documents_duree = get_documents_duree(data)
nb_docs = len(documents_duree)


def format_duree(seconde: int) -> str:
    # Division entière
    heures = seconde // 3600
    # J'utilise le reste pour calculer les minutes
    minutes = (seconde % 3600) // 60
    # Le reste de la division par 60 est egal aux secondes
    secondes = seconde % 60
    # Je retourne la durée dans le format de base avec 2 nombres pour chaque élément
    return f"{heures:02}:{minutes:02}:{secondes:02}"


def get_duree(documents_duree):
    duree_total_secondes = get_duree_total_en_secondes(documents_duree)
    return format_duree(duree_total_secondes)


duree = get_duree(documents_duree)
