import requests


def get_weather(municipality):
    url = "https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=eb9f91b8047d28d20c57d1f37bf57a38"

    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']

        return weather_description, temperature
    else:
        return None, None


def main():
    municipality = input("Enter the name of a municipality: ")
    weather_description, temperature = get_weather(municipality)

    if weather_description and temperature:
        print(f"Weather in {municipality}: {weather_description}")
        print(f"Temperature: {temperature}°C")
    else:
        print("Error. Please try again.")


    main()
