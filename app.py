from flask import Flask, jsonify

import requests

app = Flask(__name__)

servers = [
    "http://google.com",
    "http://bing.com",
    "http://whatsapp.com",
    "htt://facebook.com"
]

try:
    for server in servers:
        response = requests.get(server, timeout=5)
        if response.status_code == 200:
            print(f"server {server} is up")
        else:
            print(f"server {server} is down (status code: {response.status_code})")

except requests.exceptions.RequestException :
    print(f"{server} is down")    


@app.route('/servers', methods=['GET'])
def get_servers():
    return jsonify(servers)

if __name__ == '__main__':
    app.run(debug=True)