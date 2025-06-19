from flask import Flask, request
import requests
import re

app = Flask(__name__)
SUBSTATIONS = ["http://substation1:5002", "http://substation2:5003"]

def get_load(substation_url):
    try:
        metrics = requests.get(f"{substation_url.replace(':5002', ':8000').replace(':5003', ':8001')}/metrics").text
        match = re.search(r'substation_current_load (\\d+)', metrics)
        return int(match.group(1)) if match else float('inf')
    except:
        return float('inf')

@app.route('/route', methods=['POST'])
def route():
    data = request.get_json()
    best_sub = min(SUBSTATIONS, key=get_load)
    response = requests.post(f"{best_sub}/charge", json=data)
    return response.text, response.status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
