import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='airport',
         user='dbuser',
         password='password',
         autocommit=True
         )


def get_airport_coordinates(icao_code):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident ='{icao_code}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def calculate_distance(icao_code1, icao_code2):
    coordinates1 = get_airport_coordinates(icao_code1)
    coordinates2 = get_airport_coordinates(icao_code2)

    if coordinates1 is None or coordinates2 is None:
        return None

    distance = geodesic(coordinates1, coordinates2).kilometers
    return distance


def main():
    while True:
        icao_code1 = input("Enter the ICAO code of the first airport: ")

        if icao_code1.lower() == 'q':
            print("Exiting the program...")
            break
        icao_code2 = input("Enter the ICAO code of the second airport: ")

        distance = calculate_distance(icao_code1, icao_code2)

        if distance is not None:
            print(f"The distance between the two airports is {distance:.2f} kilometers.")
        else:
            print("Error. Please check the ICAO codes and try again.")


main()
