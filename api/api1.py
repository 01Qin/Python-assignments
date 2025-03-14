import requests
import time


def get_weather(municipality):
    api_key = "29a925ae6946277bb91e8fd8292b5154"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}'

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
    if kelvin < 0:
        return None
    celsius = kelvin - 273.15
    return round(celsius, 2)


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

        print("Please wait for 10 minutes before entering the next municipality.")
        action = input("Do you want to quit(q) or wait for 10 minutes(w)? ")
        if action.lower() == 'q':
            print("Exiting the program...")
            break
        elif action.lower() == 'w':
            print(f"Please wait for 10 minutes before entering the next municipality.")
            time.sleep(600)
        else:
            print("Invalid input. Please try again.")


main()
