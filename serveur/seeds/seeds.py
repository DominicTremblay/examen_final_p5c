from datetime import datetime
from flask_seeder import Seeder, Faker, generator
from werkzeug.security import generate_password_hash
import random
from app.modeles import Film, Utilisateur, Commentaire, favoris
from app import db


class FilmSeeder(Seeder):

    def empty_database(self):
        """Supprime tous les enregistrements des tables de la base de données."""
        db.session.execute(favoris.delete())
        db.session.execute(db.delete(Film))
        db.session.execute(db.delete(Utilisateur))

        db.session.commit()

    # Methode run appelee par Flask-Seeder
    def run(self):

        self.empty_database()

        # Creer les films
        movies = [
            {
                "titre": "Barbie",
                "genre": "Comedie",
                "annee_sortie": 2023,
                "image_url": "https://m.media-amazon.com/images/M/MV5BYjI3NDU0ZGYtYjA2YS00Y2RlLTgwZDAtYTE2YTM5ZjE1M2JlXkEyXkFqcGc@._V1_.jpg",
                "description": "Barbie découvre le monde réel en quittant Barbieland.",
            },
            {
                "titre": "Oppenheimer",
                "genre": "Drame",
                "annee_sortie": 2023,
                "image_url": "https://m.media-amazon.com/images/M/MV5BN2JkMDc5MGQtZjg3YS00NmFiLWIyZmQtZTJmNTM5MjVmYTQ4XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
                "description": "L'histoire du créateur de la bombe atomique, J. Robert Oppenheimer.",
            },
            {
                "titre": "Mission: Impossible – Dead Reckoning Part One",
                "genre": "Action",
                "annee_sortie": 2023,
                "image_url": "https://m.media-amazon.com/images/I/91dYe4m4XXL.jpg",
                "description": "Ethan Hunt doit stopper une nouvelle menace mondiale.",
            },
            {
                "titre": "Dune: Part Two",
                "genre": "Sci-Fi",
                "annee_sortie": 2024,
                "image_url": "https://m.media-amazon.com/images/M/MV5BZTA3NzY0ZjItNTk2OC00NTlkLWEzMzktZmFkOWJjMWE0MmQzXkEyXkFqcGc@._V1_.jpg",
                "description": "Paul Atreides continue sa quête sur Arrakis.",
            },
            {
                "titre": "Aquaman and the Lost Kingdom",
                "genre": "Action",
                "annee_sortie": 2024,
                "image_url": "https://m.media-amazon.com/images/M/MV5BYjQ1ZTUzMWMtY2VkNS00ZDRjLWEwODYtYmFkMWJiNTQxMDUzXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
                "description": "Aquaman affronte une nouvelle menace pour son royaume.",
            },
            {
                "titre": "Spider-Man: Across the Spider-Verse",
                "genre": "Animation",
                "annee_sortie": 2023,
                "image_url": "https://m.media-amazon.com/images/M/MV5BNThiZjA3MjItZGY5Ni00ZmJhLWEwN2EtOTBlYTA4Y2E0M2ZmXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
                "description": "Miles Morales explore le multivers des Spider-Men.",
            },
            {
                "titre": "The Marvels",
                "genre": "Action",
                "annee_sortie": 2023,
                "image_url": "https://m.media-amazon.com/images/M/MV5BYzczOWM4MzItMWMyOS00ZDczLWIxMzctNzBmYTgzOTI1MzI3XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
                "description": "Les Marvels unissent leurs forces contre une menace cosmique.",
            },
            {
                "titre": "Guardians of the Galaxy Vol. 3",
                "genre": "Action",
                "annee_sortie": 2023,
                "image_url": "https://m.media-amazon.com/images/M/MV5BOTJhOTMxMmItZmE0Ny00MDc3LWEzOGEtOGFkMzY4MWYyZDQ0XkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
                "description": "Les Gardiens se lancent dans une mission pour sauver l'un des leurs.",
            },
            {
                "titre": "The Expendables 4",
                "genre": "Action",
                "annee_sortie": 2023,
                "image_url": "https://m.media-amazon.com/images/M/MV5BZjgyMmRmM2EtYWY5ZC00ZTllLWJhM2QtMGRlNGEzMWEzYzllXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg",
                "description": "Les Expendables reviennent pour une nouvelle mission.",
            },
            {
                "titre": "John Wick: Chapter 4",
                "genre": "Action",
                "annee_sortie": 2023,
                "image_url": "https://m.media-amazon.com/images/M/MV5BNDI3OWNiMGItZmVkMS00Mjg3LWJhNzUtNDViMWU3OTJiODAyXkEyXkFqcGc@._V1_.jpg",
                "description": "John Wick affronte ses ennemis dans une quête ultime de vengeance.",
            },
        ]

        # Creer les utilisateurs
        utilisateurs = [
            {
                "nom": "Asterix",
                "courriel": "asterix@gmail.com",
                "mot_de_passe_hache": generate_password_hash("toutatis"),
                "avatar_url": f"https://robohash.org/{'asterix@gmail.com'}?set=set1&size=128x128",
            },
            {
                "nom": "Obelix",
                "courriel": "obelix@gmail.com",
                "mot_de_passe_hache": generate_password_hash("toutatis"),
                "avatar_url": f"https://robohash.org/{'obelix@gmail.com'}?set=set1&size=128x128",
            },
            {
                "nom": "Cetautomatix",
                "courriel": "cetautomatix@gmail.com",
                "mot_de_passe_hache": generate_password_hash("toutatis"),
                "avatar_url": f"https://robohash.org/{'cetautomatix@gmail.com'}?set=set1&size=128x128",
            },
            {
                "nom": "Abraracourcix",
                "courriel": "abraracourcix@gmail.com",
                "mot_de_passe_hache": generate_password_hash("toutatis"),
                "avatar_url": f"https://robohash.org/{'abraracourcix@gmail.com'}?set=set1&size=128x128",
            },
        ]

        # Ajouter films a la bd
        film_instances = []
        for movie in movies:
            film = Film(
                titre=movie["titre"],
                genre=movie["genre"],
                annee_sortie=movie["annee_sortie"],
                image_url=movie["image_url"],
                description=movie["description"],
            )
            print(f"Ajout film: {movie['titre']}")
            film_instances.append(film)  # Store for later relationships
            self.db.session.add(film)

        # Ajouter utilisateur et assigner les films
        utilisateur_instances = []
        for user in utilisateurs:
            utilisateur = Utilisateur(
                nom=user["nom"],
                courriel=user["courriel"],
                mot_passe_hache=user["mot_de_passe_hache"],
                avatar_url=user["avatar_url"]
            )
            print(f"Ajout utilisateur: {user['nom']}")

            utilisateur.films = random.sample(film_instances, 3)
            utilisateur_instances.append(utilisateur)
            self.db.session.add(utilisateur)

        # Commit all changes to the database
        self.db.session.commit()

        # Ajouter followers (2 par utilisateur)
        for utilisateur in utilisateur_instances:
            followers_potentiels = [
                u for u in utilisateur_instances if u != utilisateur
            ]
            if len(followers_potentiels) >= 2:
                followers = random.sample(followers_potentiels, 1)
                for follower in followers:
                    # Check if the follower already exists
                    if follower not in utilisateur.followers:
                        utilisateur.followers.append(follower)
                        print(f"{follower.nom} suit {utilisateur.nom}")


        # Créer des commentaires pour chaque film
        commentaires = [
            "J'ai adoré ce film, c'était incroyable !",
            "Pas mal, mais je m'attendais à mieux.",
            "Un chef-d'œuvre, à voir absolument !",
            "J'ai trouvé l'histoire ennuyeuse.",
            "Les effets spéciaux étaient impressionnants.",
            "Les acteurs ont fait un excellent travail.",
            "C'était trop long à mon goût.",
            "Une belle surprise, je ne m'attendais pas à ça.",
            "Déçu par la fin, mais globalement bon.",
            "Un film à revoir plusieurs fois !",
        ]

        # Ajouter 3 commentaires aléatoires de différents utilisateurs à chaque film
        for film in film_instances:
            for _ in range(3):
                utilisateur = random.choice(utilisateur_instances)
                contenu = random.choice(commentaires)

                commentaire = Commentaire(
                    contenu=contenu,
                    date_creation=datetime.now(),  # Add current timestamp
                    film=film,
                    utilisateur=utilisateur,
                )
                print(
                    f"Ajout commentaire: '{contenu}' par {
                      utilisateur.nom} sur {film.titre}"
                )
                db.session.add(commentaire)

        # Commit final des commentaires
        self.db.session.commit()
