class Formation:
    """
    Cette classe contient toutes les informations nécessaires à la construction du pdf qui fait office de brochure d'une formation.
    Les attributs sont créés à partir du json envoyé par l'API.
    """

    def __init__(self, data: dict):
        createur_data: dict = data.get("createur", {})

        self.titre: str = data.get("titre", "")
        self.description: str = data.get("description", "")
        self.financable: bool = data.get("financeable", False)
        self.prix: str = data.get("prix", None)
        self.apports: str = data.get("apports", [])
        self.prerequis: str = data.get("prerequis", [])
        self.module: list[Module] = self._get_list_module(data)
        self.createur: str = (
            f"{createur_data.get('nom', '')} {createur_data.get('prenom', '')}"
        )
        self.documents_duree, self.documents_types = self._get_documents_duree_types(
            data
        )
        self.duree: str = self._get_duree()
        self.nb_docs: int = len(self.documents_duree)

    def _get_documents_duree_types(self, data: dict) -> tuple[list, dict]:
        """
        Cette fonction sert à récupérer un dictionnaire avec les types en clé et le nombre en valeur.
        """
        documents_duree = []
        documents_types = {}
        for structure in data.get("structure", []):
            for chapitre in structure.get("chapitres", []):
                for subchapitre in chapitre.get("subchapitre", []):
                    for document in subchapitre.get("documents", []):
                        documents_duree.append(document.get("duree", ""))
                        if document["type"] in documents_types:
                            documents_types[document["type"]] += 1
                        else:
                            documents_types[document["type"]] = 1
        print(documents_types)

        return documents_duree, documents_types

    def _get_duree_total_en_secondes(self):
        return sum(self._parse_duree_to_int(duree) for duree in self.documents_duree)

    def _parse_duree_to_int(self, duree):
        heures, minutes, secondes = map(int, duree.split(":"))
        return heures * 3600 + minutes * 60 + secondes

    def _format_duree(self, seconde):
        heures = seconde // 3600
        minutes = (seconde % 3600) // 60
        secondes = seconde % 60
        return f"{heures:02}:{minutes:02}:{secondes:02}"

    def _get_duree(self):
        duree_total_seconds = self._get_duree_total_en_secondes()
        return self._format_duree(duree_total_seconds)

    def _get_list_module(self, data):
        list_module = []
        for module in data["structure"]:
            list_module.append(Module(module))
        return list_module

    def __str__(self):
        modules_str = "\n".join(str(module) for module in self.module)
        return f"""
                Titre: {self.titre},
                Description: {self.description},
                Createur: {self.createur}

                Finançable: {self.financable}
                Prix: {str(self.prix)},
                Apports: {self.apports},
                Prerequis: {self.prerequis}
                Duree totale: {self.duree}
                Nombre de documents: {self.nb_docs}
                Module : {modules_str}
                """


class Module:
    def __init__(self, data: dict):
        self.titre: str = data["module_titre"]
        self.chapitres: list[Chapitre] = self._get_list_chapitres(data)

    def _get_list_chapitres(self, data: dict):
        list_chapitre = []
        for chapitre in data["chapitres"]:
            list_chapitre.append(Chapitre(chapitre))
        return list_chapitre

    def __str__(self):
        chapitres_str = "\n".join(str(chapitre) for chapitre in self.chapitres)
        return f"Module Titre: {self.titre}\nChapitres:\n{chapitres_str}"


class Chapitre:
    def __init__(self, data: dict):
        self.chapitre_titre: str = data.get("chapitre_titre", "")
        self.subchapitres: list[Subchapitre] = self._get_subchapitres(data)

    def _get_subchapitres(self, data: dict):
        list_subchapitre = []
        for subchapitre in data["subchapitre"]:
            list_subchapitre.append(Subchapitre(subchapitre))
        return list_subchapitre

    def __str__(self):
        subchapitres_str = "\n".join(
            str(subchapitre) for i, subchapitre in enumerate(self.subchapitres)
        )
        return (
            f"Chapitre Titre: {self.chapitre_titre}\nSubchapitres:\n{subchapitres_str}"
        )


class Subchapitre:
    def __init__(self, data: dict):
        self.subchapitre_titre: str = data.get("subchapitre_titre", "")
        self.nb_doc: int = len(data.get("documents"))

    def __str__(self):
        return f"Subchapitre Titre: {self.subchapitre_titre}\nNombre de documents: {self.nb_doc}"
