from flask import Flask, request
from prometheus_client import start_http_server, Gauge
import threading
import time

app = Flask(__name__)
current_load = 0
load_metric = Gauge('substation_current_load', 'Current load on the substation')

@app.route('/charge', methods=['POST'])
def charge():
    global current_load
    current_load += 1
    load_metric.set(current_load)
    time.sleep(1)  # simulate charging
    current_load -= 1
    load_metric.set(current_load)
    return "Charging started", 200

def run_metrics_server():
    start_http_server(8000)

threading.Thread(target=run_metrics_server).start()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
