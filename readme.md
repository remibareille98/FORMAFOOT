# Projet PDF Automatisation - FORMAFOOT

Bienvenue dans ce projet de construction automatisée de plaquettes PDF pour présenter des formations en collaboration avec FORMAFOOT.

## Contenu du Projet

Dans ce projet, vous trouverez les éléments suivants :

- **Ressources Images** : Images conformes à la charte graphique.
- **Exemples de Design** : Quelques exemples de designs déjà appliqués.
- **api.json** : Fichier correspondant à l'objet d'entrée à traiter.
- **colors.json** : Références des couleurs utilisées.
- **Dossier de Fonts** : Ensemble de polices à intégrer au PDF.

## Objectif

L'objectif principal de ce projet est de réaliser une automatisation de la construction d'une plaquette PDF à partir de l'objet d'entrée fourni (json).

## Demandes Spécifiques

La demande spécifique consiste à réaliser une plaquette de présentation de formation qui inclut les éléments suivants :

**Page 1**
- **Titre et Description de la Formation** 
(voir exemple)

**Page 2**
- **Informations Générales** :
  - Finançable ou non
  - Prix
  - Apports
  - Prérequis
  - Durée totale
  - Nombre de documents types (vidéo, PDF, etc.)

**Page 3 et plus**

- **Descriptif de la Formation** :
  - Modules
  - Chapitres dans les modules
  - Sous-chapitres dans les chapitres
  - Nombre de Documents dans les sous-chapitres

## Détails Techniques

- **Langage** : Python 3.10
- **Librairie** : fpdf2==2.7.7
- **Approche** : Programmation Orientée Objet
- **Bonnes Pratiques de Code** : Respectées

Lien pour télécharger python3.10 : 
- **Mac** : https://www.python.org/downloads/macos/
- **Windows** : https://www.python.org/downloads/windows/

### Création de votre environnement virtuel et installation des dépendances 

- **Créer le venv** : `python3.10 -m venv venv` 
- **Activer le venv** : Mac -> `source/venv/bin/activate` Windows -> `venv\Scripts\activate`

- **Installation des dépendances** : `pip install -r requirements.txt` 

L'objectif est de garantir que le document soit fonctionnel, c'est-à-dire qu'il contienne toutes les informations nécessaires. Dans un second temps, une attention particulière sera portée à son aspect esthétique pour qu'il reflète l'identité de la marque (Brand FormaFoot).

---
**Contact:**  

Remi BAREILLE - Intervenant GEMA
remi.bareille.int@groupe-gema.com  

Bastien ANGELOZ - Tech Lead FORMAFOOT
bastien.angeloz.int@groupe-gema.com  

