import requests


def get_weather(municipality):
    url = (f'http://api.openweathermap.org/data/2.5/weather?'
           f'q={municipality}&appid=29a925ae6946277bb91e8fd8292b5154&units=metric')

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature_kelvin = data['main']['temp']
        temperature_celsius = kelvin_to_celsius(temperature_kelvin)
        return weather_description, temperature_celsius
    else:
        return None, None


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return int(celsius)


def main():
    while True:
        municipality = input("Enter the name of a municipality (or 'q' to quit): ")
        if municipality.lower() == 'q':
            print("Exiting the program...")
            break
        weather_description, temperature = get_weather(municipality)

        if weather_description and temperature:
            print(f"Weather in {municipality}: {weather_description}")
            print(f"Temperature: {temperature}°C")
        else:
            print("Error. Please try again.")


main()
