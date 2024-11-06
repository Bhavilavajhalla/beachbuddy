from flask import Flask, render_template, request, jsonify
import json
import requests

app = Flask(__name__)

# Load beach data from the JSON file
with open('data/beaches.json') as beaches_file:
    beaches_data = json.load(beaches_file)

INCOIS_API_URL = ""  # Replace with the actual INCOIS API URL

# Find the beach coordinates by name from the JSON file
def get_coordinates(location_name):
    for beach in beaches_data['beaches']:
        if beach['name'].lower() == location_name.lower():
            return beach['latitude'], beach['longitude']
    return None, None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/beaches', methods=['GET'])
def get_beaches():
    location_name = request.args.get('location')

    # Get latitude and longitude from the JSON file
    lat, lon = get_coordinates(location_name)

    if lat is None or lon is None:
        return jsonify({'error': 'Location not found in database'})

    # Fetch ocean data from INCOIS API using lat, lon
    api_url = f"{INCOIS_API_URL}?lat={lat}&lon={lon}&api_key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b"  # Update with INCOIS API Key
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            ocean_data = response.json()
        else:
            ocean_data = {"error": "Unable to fetch data from INCOIS API"}
    except Exception as e:
        ocean_data = {"error": f"API request failed: {e}"}

    return jsonify(ocean_data)

if __name__ == "__main__":
    app.run(debug=True)
