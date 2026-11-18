import os
from flask import Flask, jsonify

app = Flask(__name__)

# Logic: Look for an environment variable. If it doesn't exist, use a default fallback.
SERVICE_NAME = os.environ.get('SERVICE_NAME', 'backend')
SERVICE_VERSION = os.environ.get('SERVICE_VERSION', '1.0.0')

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/info')
def info():
    return jsonify({"service": SERVICE_NAME, "version": SERVICE_VERSION}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
