from flask import Flask, jsonify
import random
import time
import os

app = Flask(__name__)

CELL_COUNT = int(os.getenv("CELL_COUNT", "5"))

@app.route("/voltages")
def get_voltages():
    voltages = [
        round(random.uniform(3.68, 3.73), 3)
        for _ in range(CELL_COUNT)
    ]

    data = {
        "cell_voltages": voltages,
        "timestamp": time.time()
    }

    print("Generated voltages:", data, flush=True)

    return jsonify(data)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    print("Battery simulator API started.", flush=True)
    print("Cell count:", CELL_COUNT, flush=True)

    app.run(host="0.0.0.0", port=5000)
