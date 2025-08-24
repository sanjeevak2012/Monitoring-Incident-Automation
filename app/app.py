from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import time, random

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.0')

@app.route('/health')
def health():
    return jsonify(status='ok')

@app.route('/work')
def work():
    time.sleep(random.uniform(0.05, 0.3))  # simulate latency
    return jsonify(result="done")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
