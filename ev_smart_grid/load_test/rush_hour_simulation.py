import requests
import threading

def send_request():
    requests.post("http://localhost:5000/charge", json={"vehicle_id": 1})

threads = [threading.Thread(target=send_request) for _ in range(100)]
for t in threads: t.start()
for t in threads: t.join()
