# -*- coding: utf-8 -*-
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ast import literal_eval

# Chemin vers le dossier rcm (recommend)
rcm = "./movies_recommendation"

# Vérifiez si le dossier existe déjà
if not os.path.exists(rcm):
    os.makedirs(rcm, exist_ok=True)
    print(f"Le nouveau dossier '{rcm}' a été créé avec succès.")
else:
    print(f"Le dossier '{rcm}' existe déjà.")

# Changer le répertoire de travail actuel pour le nouveau dossier
os.chdir(rcm)

# Vérifiez et affichez le répertoire de travail actuel
current_directory = os.getcwd()
print(f"Répertoire de travail actuel : {current_directory}")

"""
In fact, I utilize the virtual environment like below:
python -m venv movies_recommendation
cd movies_recommendation
source bin/activate
echo ""> main.py
echo ""> preprocessing.py
"""

# Charger les données à partir des fichiers CSV
data_movies = pd.read_csv('/Users/dolphin/Downloads/movies_recommendation/data/tmdb/tmdb_5000_movies.csv', na_filter=False)
data_credits = pd.read_csv('/Users/dolphin/Downloads/movies_recommendation/data/tmdb/tmdb_5000_credits.csv')

print("\nDONNÉES FILMS")
print(data_movies.info())
print("\n\nDONNÉES CRÉDITS")
print(data_credits.info())

# Renommer la colonne 'id' en 'movie_id'
data_movies = data_movies.rename(columns={'id': 'movie_id'})

# Supprimer les colonnes non nécessaires de data_movies
data_movies = data_movies.drop(columns=[
                                        'budget', 'homepage', 'keywords', 'original_language', 'popularity', 
                                        'production_companies', 'production_countries', 'release_date', 
                                        'revenue', 'runtime', 'spoken_languages', 'status', 'tagline', 
                                        'title', 'vote_average', 'vote_count'
                                        ])

# Supprimer les colonnes non nécessaires de data_credits
data_credits = data_credits.drop(columns=['title', 'crew'])

# Fusionner data_movies et data_credits
data_movies = data_movies.merge(data_credits, on='movie_id')
print(data_movies.head())

# Convertir les chaînes JSON en listes avec literal_eval
features = ['cast', 'genres']
for feature in features:
    data_movies[feature] = data_movies[feature].apply(literal_eval)

# Fonction pour obtenir une liste de noms à partir des données JSON
def get_list(meta_data):
    if isinstance(meta_data, list):
        names = [col['name'] for col in meta_data]
        if len(names) > 3:
            names = names[:3]
        return names
    return []

for feature in features:
    data_movies[feature] = data_movies[feature].apply(get_list)

# Charger et traiter les données Bollywood
data_movies_hindi = pd.read_csv('/Users/dolphin/Downloads/movies_recommendation/data/bollywood/1950-2019/bollywood_full_1950-2019.csv', na_filter=False)
data_movies_hindi = data_movies_hindi.drop(columns=['title_x', 'tagline', 'poster_path', 'wiki_link', 'title_y', 'is_adult', 'year_of_release', 'imdb_rating', 'runtime', 'imdb_votes', 'story', 'wins_nominations', 'release_date'])
data_movies_hindi.rename(columns={'actors': 'cast', 'imdb_id': 'movie_id'}, inplace=True)
data_movies_hindi['genres'] = data_movies_hindi['genres'].str.split('|')
data_movies_hindi['cast'] = data_movies_hindi['cast'].str.split('|')

# Fonction pour nettoyer les données et obtenir les trois premiers acteurs
def clean_data(actors):
    if isinstance(actors, list):
        return actors[:3]
    return []

data_movies_hindi['cast'] = data_movies_hindi['cast'].apply(clean_data)

# Combiner les données de Hollywood et Bollywood
combine = pd.concat([data_movies, data_movies_hindi], ignore_index=True, sort=True)

# Vérifiez les données combinées
print("Données combinées")
print(combine.isnull().sum())

# Enregistrer les données dans un fichier CSV
combine.to_csv('movie_data.csv', index=False)

# Recharger et compresser les données
final_data = pd.read_csv('movie_data.csv', na_filter=False)
final_data['plot'] = final_data[['overview', 'summary']].apply(lambda x: ' '.join(x), axis=1)
final_data = final_data.drop(['summary', 'overview'], axis=1)

# Supprimer les lignes de données inutiles
final_data = final_data.drop([6221, 6222, 6219, 6210, 6211, 5508, 6121, 5634, 2962, 5499])
final_data.drop(final_data.index[6465:9130], inplace=True)

# Ajouter de nouvelles données
data_new = pd.DataFrame({
    'cast': [
        ['Robert Downey Jr.', 'Chris Evans', 'Chris Hemsworth'],
        ['Joaquin Phoenix', 'Robert De Niro', 'Zazie Beetz'],
        # Ajouter d'autres films ici
    ],
    'genres': [
        ['Action', 'Adventure', 'Drama'],
        ['Crime', 'Drama', 'Thriller'],
        # Ajouter d'autres genres ici
    ],
    'movie_id': [299534, 475557], # Ajouter d'autres IDs de films ici
    'original_title': ['Avengers: Endgame', 'Joker'],
    'plot': [
        'After the devastating events of Avengers: Infinity War (2018), the universe is in ruins...',
        'In Gotham City, mentally troubled comedian Arthur Fleck is disregarded...'
    ]
})

final_data = pd.concat([final_data, data_new], ignore_index=True, sort=True)

# Enregistrer les données finales dans un fichier CSV compressé
final_data.to_csv('movie_data_compress.csv.zip', index=False)

print("Traitement final des données terminé et enregistré sous 'movie_data_compress.csv.zip'")
