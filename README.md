# TP CI/CD avec GitHub Actions et Docker

Ce projet configure un pipeline CI/CD pour une application Python avec GitHub Actions et Docker.

Lien vers le dépôt GitHub : https://github.com/Paul-Berdier/tp-ci-cd

1. **Initialisation du dépôt Git** : Création et initialisation du dépôt.
2. **Clé SSH pour GitHub** : Génération et ajout de la clé SSH à GitHub.
3. **Création des fichiers** :
   - `simple_math.py` : Contient les fonctions addition et soustraction.
   - `test_simple_math.py` : Contient les tests unitaires pour les fonctions.
4. **Configuration de GitHub Actions** :
   - `.github/workflows/python-app.yml` : Définit les étapes de linting, tests et construction Docker.
5. **Dockerfile** : Définit l'image Docker pour l'application.
6. **requirements.txt** : Spécifie les dépendances du projet (pytest, pylint).
7. **Exécution du pipeline CI/CD** : Automatisation du linting, tests et construction Docker à chaque push.


