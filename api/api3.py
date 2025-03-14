from flask import Flask, jsonify
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='dbuser',
    password='password',
    database='airport',
    autocommit=True
)

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the airport API."})


@app.route("/airport/<icao_code>", methods=['GET'])
def get_airport_info(icao_code):
    cursor = connection.cursor(dictionary=True)
    query = f"SELECT * FROM airport WHERE ident = '{icao_code}'"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()

    if result:
        airport_info = {
            "ICAO": result['ident'],
            "Name": result['name'],
            "Location": result['municipality']
        }
        return jsonify(airport_info)
    else:
        return jsonify({"Error": "Airport not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
