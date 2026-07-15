# BMS Network Demo

This is a small Docker Compose demo for a Battery Management System project.

It contains two services:

- `battery_simulator`: a Flask API that generates fake battery cell voltages.
- `bms_controller`: a Python controller that requests voltage data from the simulator and decides whether balancing is needed.

## Project Structure

```text
bms-network-demo/
├── src/
│   ├── battery_simulator.py
│   └── bms_controller.py
├── config/
│   └── .env.example
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env
