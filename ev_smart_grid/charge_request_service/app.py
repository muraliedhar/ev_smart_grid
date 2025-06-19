from flask import Flask, request
import requests

app = Flask(__name__)
LOAD_BALANCER_URL = "http://load_balancer:5001"

@app.route("/charge", methods=["POST"])
def charge():
    data = request.get_json()
    response = requests.post(f"{LOAD_BALANCER_URL}/route", json=data)
    return response.text, response.status_code
@app.route("/charge", methods=["GET"])
def info():
    return "Send a POST request with vehicle_id JSON to charge."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
