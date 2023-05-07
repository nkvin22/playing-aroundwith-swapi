import json
import requests


movies = {}

def get_data(movie_id):

    BASE_URL = "https://www.swapi.tech/api/films"
    response = requests.get(f"{BASE_URL}/{movie_id}")

    result = response.json()["result"]
    movie_title = result["properties"]["title"]
    episode_id = result["properties"]["episode_id"]
    crawling_text = result["properties"]["opening_crawl"]
    directors = result["properties"]["director"]
    producers = result["properties"]["producer"]
    release_date = result["properties"]["release_date"]
    characters_urls = result["properties"]["characters"]
    planets_urls = result["properties"]["planets"]
    species_url = result["properties"]["species"]

    characters = []
    planets = []
    species = []

    for url in characters_urls:
        response = requests.get(url)
        character_name = response.json()["result"]["properties"]["name"]
        characters.append(character_name)

    for url in planets_urls:
        response = requests.get(url)
        planet_name = response.json()["result"]["properties"]["name"]
        planets.append(planet_name)

    for url in species_url:
        response = requests.get(url)
        species_name = response.json()["result"]["properties"]["name"]
        species.append(species_name)

    return {
        'title': movie_title,
        'episode_id': episode_id,
        'opening_crawl': crawling_text,
        'director': directors,
        'producers': producers,
        'release_date': release_date,
        'characters': characters,
        'planets': planets,
        'species': species
    }


while True:
    print(
        "1 - A New Hope\n"
        "2 - The empire strikes back\n"
        "3 - Return of the Jedi\n"
        "4 - The Phantom Menace\n"
        "5 - Attack of the Clones\n"
        "6 - Revenge of the Sith")
    movie_id = input("Enter film id to get information about it(in case of any other symbol(s) the program will close:")

    if movie_id in movies:
        movie_info = movies[movie_id]
    else:
        if movie_id not in ['1', '2', '3', '4', '5', '6']:
            break
        movie_info = get_data(movie_id)
        movies[movie_id] = movie_info

    print(f"Title: {movie_info['title']}")
    print(f"Episode ID: {movie_info['episode_id']}")
    print(f"Opening Crawl: {movie_info['opening_crawl']}")
    print(f"Director(s): {movie_info['director']}")
    print(f"Producer(s): {movie_info['producers']}")
    print(f"Release Date: {movie_info['release_date']}")
    print("Characters:")
    for character in movie_info['characters']:
        print(f"  ● {character}")
    print("Planets:")
    for planet in movie_info['planets']:
        print(f"  ● {planet}")
    print("Species:")
    for specie in movie_info['species']:
        print(f"  ● {specie}")

