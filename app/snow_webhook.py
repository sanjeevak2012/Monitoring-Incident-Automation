from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/snow", methods=["POST"])
def snow_webhook():
    data = request.json
    print("🚨 New Alert Received from Alertmanager 🚨")
    for alert in data.get("alerts", []):
        print(f"Incident Created: {alert['labels'].get('alertname')} - {alert['annotations'].get('description')}")
    return jsonify({"status": "incident created"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
