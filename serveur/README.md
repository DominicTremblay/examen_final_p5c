# Serveur Flask

## Installation


1. Créer un fichier `.env` à la racine du serveur

```
SECRET_KEY='votre_clé_secrète'
DATABASE_URL=sqlite:///films.db
FLASK_ENV=development
FLASK_DEBUG=1
```

2. Créer un environnement virtuel

`python -m venv venv`

3. Activer l'environnement virtuel

- Windows: `venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`

4. Installer les dépendances

`pip install -r requirements.txt`

5. Créer la base de données

`flask db upgrade`

6. Entrer les données de test

`flask seed run`

7. Démarrer le serveur

`flask run`

9. Ouvrir un navigateur et aller à l'adresse `http://localhost:5000`


## Structure du serveur

### Routes 

- Le fichier des routes pour l'API est localisé dans `app/api/routes.py`
- utiliser `@api_bp.route` pour définir les routes (ex.: `@api_bp.route("/", methods=["GET"])`)

### Modèle

- Le modèle se trouve dans `app/modeles`

### Base de données SQLite3

- La base de données se trouve dans `instance/films.db`

### Seeds

- Le fichier des seeds se trouve dans `seeds/seeds.py`



