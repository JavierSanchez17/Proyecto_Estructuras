import requests


def characters():
    publickey = '130c7354b5734b793a253f9087d61518'
    hashed = 'a165aa46a0c484d5a49298745951c610'

    url = f'https://gateway.marvel.com:443/v1/public/characters?ts=1&apikey={publickey}&hash={hashed}'

    response = requests.get(url).json()
    return response


class Personajes_Url:
    def __init__(self):
        self.personajes = characters()

