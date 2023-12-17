from flask import Flask, jsonify
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='dbuser',
    password='password',
    database='airport',
    autocommit=True
)

app = Flask(__name__)


@app.route("/airport/<icao_code>")
def get_airport_info(icao_code):
    cursor = connection.cursor(dictionary=True)
    query = f"SELECT name, location FROM airport WHERE icao = '{icao_code}'"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()

    if result:
        airport_info = {
            "ICAO": icao_code,
            "Name": result['name'],
            "Location": result['location']
        }
        return jsonify(airport_info)
    else:
        return jsonify({"error": "Airport not found"}), 404


app.run(debug=True)