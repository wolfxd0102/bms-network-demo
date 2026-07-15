import requests
import time
import os

SIMULATOR_URL = os.getenv(
    "SIMULATOR_URL",
    "http://battery_simulator:5000/voltages"
)

MONITOR_THRESHOLD = float(os.getenv("MONITOR_THRESHOLD", "0.02"))
BALANCE_THRESHOLD = float(os.getenv("BALANCE_THRESHOLD", "0.04"))
CONTROL_INTERVAL = float(os.getenv("CONTROL_INTERVAL", "2"))

print("BMS controller started.", flush=True)
print("Simulator URL:", SIMULATOR_URL, flush=True)
print("Monitor threshold:", MONITOR_THRESHOLD, flush=True)
print("Balance threshold:", BALANCE_THRESHOLD, flush=True)
print("Control interval:", CONTROL_INTERVAL, flush=True)

while True:
    try:
        response = requests.get(SIMULATOR_URL, timeout=2)
        response.raise_for_status()
        data = response.json()

        voltages = data["cell_voltages"]

        max_voltage = max(voltages)
        min_voltage = min(voltages)
        voltage_gap = max_voltage - min_voltage

        print("-" * 50, flush=True)
        print("Cell voltages:", voltages, flush=True)
        print("Max voltage:", max_voltage, flush=True)
        print("Min voltage:", min_voltage, flush=True)
        print("Voltage gap:", round(voltage_gap, 3), flush=True)

        if voltage_gap <= MONITOR_THRESHOLD:
            print("Decision: cells are well balanced", flush=True)
        elif voltage_gap <= BALANCE_THRESHOLD:
            print("Decision: monitor only", flush=True)
        else:
            print("Decision: active balancing needed", flush=True)

    except requests.exceptions.RequestException as error:
        print("Could not reach battery simulator:", error, flush=True)

    time.sleep(CONTROL_INTERVAL)
