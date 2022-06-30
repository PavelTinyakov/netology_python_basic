import requests


def genius_hero(*names_heroes: str) -> str:
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url).json()
    intelligence = 0
    name = ''
    for hero in response:
        if hero['name'] in names_heroes and hero['powerstats']['intelligence'] > intelligence:
            intelligence = hero['powerstats']['intelligence']
            name = hero['name']
    return f'{name = }, {intelligence = }'


if __name__ == '__main__':
    print(genius_hero('Hulk', 'Thanos', 'Capitan America'))
