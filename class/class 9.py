import requests


def get_random_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        joke = data["value"]
        return joke
    else:
        return "Failed!"


random_joke = get_random_joke()
print(random_joke)
