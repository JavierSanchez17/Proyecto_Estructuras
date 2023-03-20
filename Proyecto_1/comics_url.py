import requests


def comics():
    publickey = '130c7354b5734b793a253f9087d61518'
    hashed = 'a165aa46a0c484d5a49298745951c610'

    url = f'https://gateway.marvel.com:443/v1/public/comics?ts=1&apikey={publickey}&hash={hashed}'

    response = requests.get(url).json()
    return response


class Comics_url:
    def __init__(self):
        self.comics = comics()
