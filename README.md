# B-ON connector

This is a repository with an example of a connector.
It contains a notebook that connects to the B-ON platform and submits mocked TCU data.

## Setup

### Environment requirements
1. Install python `3.12`.
2. Install poetry: `pip install poetry==2.1.2`.
3. Install poetry dependencies: `poetry install`.

### Prerequisites
1. Get the `certificates` folder from B-ON. Put it in the repository root.
2. Get the connector metadata from B-ON: `B_ON_MQTT_ENDPOINT`, `TENANT`, `THING_IMEI`.

### Running the B-ON connector
1. Start the jupyter lab: `poetry run jupyter-lab`.
2. Open the notebook `b-on_connector.ipynb`.
3. Update the connector metadata in the notebook: `B_ON_MQTT_ENDPOINT`, `TENANT`, `THING_IMEI`.
4. Optionally change the values for position, odometer and battery.
5. Run the notebook: `Run > Run All Cells`

## Data exploration
1. Open [the B-ON platform](https://iot.b-on.com/) and log in.
2. Explore the Vehicle assets and their data.
