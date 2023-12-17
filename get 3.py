from flask import Flask, jsonify

app = Flask(__name__)

# Airport database (replace with your own implementation to fetch airport information)
airport_database = {
    "EFHK": {
        "ICAO": "EFHK",
        "Name": "Helsinki-Vantaa Airport",
        "Location": "Helsinki"
    },
    "EGLL": {
        "ICAO": "EGLL",
        "Name": "Heathrow Airport",
        "Location": "London"
    },
    # Add more airports as needed
}

@app.route("/airport/<icao_code>")
def get_airport_info(icao_code):
    if icao_code in airport_database:
        airport_info = airport_database[icao_code]
        return jsonify(airport_info)
    else:
        return jsonify({"error": "Airport not found"}), 404