import requests
import csv


def fetch_characters():
    url = "https://rickandmortyapi.com/api/character/"
    params = {
        "species": "Human",
        "status": "Alive",
        "origin": "Earth"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        characters = response.json()["results"]
        return characters
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def write_to_csv(characters):
    if not characters:
        return

    with open('rick_and_morty_characters.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Location', 'Image'])

        for character in characters:
            name = character['name']
            location = character['origin']['name']
            image = character['image']

            writer.writerow([name, location, image])

    print("CSV file 'rick_and_morty_characters.csv' has been created successfully.")


def main():
    characters = fetch_characters()
    if characters:
        write_to_csv(characters)


if __name__ == "__main__":
    main()
