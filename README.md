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

## Vehicle signals

| Status message | Details | MQTT topic | Message parameters | Other details |
| --- | --- | --- | --- | --- |
| VehicleACChargeCurrent | This message is used to transmit the current flow on the vehicle’s AC side. | `{TENANT}/vehicleStatus/{THING_IMEI}/vehicle/acChargeCurrent` | <pre>Signal(<br>  timestamp = timestamp,<br>  value_per_phase = ValuePerPhase(phase1=value1, phase2=value2, phase3=value3),<br>)</pre> | Scaling factor: 100 |
| VehicleACChargeVoltage | This message is used to transmit the voltage present on the vehicle’s AC side. | `{TENANT}/vehicleStatus/{THING_IMEI}/vehicle/acChargeVoltage` | <pre>Signal(<br>  timestamp = timestamp,<br>  value_per_phase = ValuePerPhase(phase1=value1, phase2=value2, phase3=value3),<br>)</pre> | Scaling factor: 10 |
| VehicleACCurrentRealized | This message is used to transmit the charge power currently realized by the vehicle. The value transmitted here is not including any derating but is referring to the value set in the respective command message. | `{TENANT}/vehicleStatus/{THING_IMEI}/vehicle/chargingPowerRealized` | <pre>Signal(<br>  timestamp = timestamp,<br>  ac_current_realized = ACCurrentRealized(realized_ac_current=value1, type=value2, rpc_id=value3, slice_id=value4),<br>)</pre> | |
| VehicleAmbientTemperature | This message is used to transmit the temperature of vehicle’s outside environment temperature sensor. | `{TENANT}/vehicleStatus/{THING_IMEI}/vehicle/ambientTemperature` | <pre>Signal(<br>  timestamp = timestamp,<br>  integer_number = value,<br>)</pre> | Scaling factor: 10 |
| VehicleBatteryTemperature | This message is used to transmit the temperature of vehicle’s battery pack. | `{TENANT}/vehicleStatus/{THING_IMEI}/battery/batteryTemperature` | <pre>Signal(<br>  timestamp = timestamp,<br>  integer_number = value,<br>)</pre> | Scaling factor: 10 |
| VehicleCabinTemperature | This message is used to transmit the temperature of vehicle’s driver cabin. | `{TENANT}/vehicleStatus/{THING_IMEI}/vehicle/cabinTemperature` | <pre>Signal(<br>  timestamp = timestamp,<br>  integer_number = value,<br>)</pre> | Scaling factor: 10 |
| VehicleChargePlugStatus | This message is used to transmit the state of the vehicle’s charge plug/socket. | `{TENANT}/vehicleStatus/{THING_IMEI}/vehicle/chargePlugStatus` | <pre>Signal(<br>  timestamp = timestamp,<br>  charge_plug_status = value,<br>)</pre> | |
| VehicleChargingDCPowerMax | This message is used to transmit the charge power realizable by the vehicle at the moment. | `{TENANT}/vehicleStatus/{THING_IMEI}/vehicle/chargingDCPowerMax` | <pre>Signal(<br>  timestamp = timestamp,<br>  charging_dc_power_max = ChargingDcPowerMax(derating_justified=value1, derating_unjustified=value2),<br>)</pre> | |
| VehicleDCChargeCurrent | This message is used to transmit the current flow on the vehicle’s DC side. | `{TENANT}/vehicleStatus/{THING_IMEI}/vehicle/dcChargeCurrent` | <pre>Signal(<br>  timestamp = timestamp,<br>  integer_number = value,<br>)</pre> | Scaling factor: 100 |
| VehicleDCChargeVoltage | This message is used to transmit the voltage present on the vehicle’s DC side. | `{TENANT}/vehicleStatus/{THING_IMEI}/vehicle/dcChargeVoltage` | <pre>Signal(<br>  timestamp = timestamp,<br>  integer_number = value,<br>)</pre> | Scaling factor: 100 |
| VehicleIgnitionStatus | This message is used to transmit the state of the vehicle’s ignition. | `{TENANT}/vehicleStatus/{THING_IMEI}/vehicle/ignitionStatus` | <pre>Signal(<br>  timestamp = timestamp,<br>  ignition_status = value,<br>)</pre> | |
| VehicleOdometer | This message is used to transmit the odometer value. | `{TENANT}/vehicleStatus/{THING_IMEI}/vehicle/odometer` | <pre>Signal(<br>  timestamp = timestamp,<br>  integer_number = value,<br>)</pre> | Scaling factor: 10 |
| VehicleOnlineStatus | This message is used to transmit the vehicle’s connectivity state to the backend. This message shall be sent at least every 15 minutes to act as a keep-alive message for the backend. | `{TENANT}/vehicleStatus/{THING_IMEI}/vehicle/onlineStatus` | <pre>Signal(<br>  timestamp = timestamp,<br>  online_status = value,<br>)</pre> | |
| VehiclePositionStatus | This message is used to transmit the vehicle’s location. | `{TENANT}/vehicleStatus/{THING_IMEI}/vehicle/positionStatus` | <pre>Signal(<br>  timestamp = timestamp,<br>  position = Position(lat=value1, lon=value2),<br>)</pre> | |
| VehiclePreconditioningStatus | This message is used to transmit information about the vehicle’s preconditioning. | `{TENANT}/vehicleStatus/{THING_IMEI}/vehicle/preconditioningStatus` | <pre>Signal(<br>  timestamp = timestamp,<br>  preconditioning_status= PreconditioningStatus(<br>    preconditioning_schedule_request_id=value1,<br>    preconditioning_schedule_slice_id=value2,<br>    slice_status=value3,<br>  ),<br>)</pre> | |
| VehicleStateOfCharge | This message transmits the current state of charge of the vehicle’s battery. | `{TENANT}/vehicleStatus/{THING_IMEI}/battery/stateOfCharge` | <pre>Signal(<br>  timestamp = timestamp,<br>  integer_number = value,<br>)</pre> | Scaling factor: 10 |
| VehicleVINStatus | This message transmits the current VIN of the vehicle the telematic unit is connected to. Since in some cases telematic units can be switched between vehicles, this message is used to signal that to the backend, allowing the status messages reported by the telematic unit to be associated with the correct vehicle. | `{TENANT}/vehicleStatus/{THING_IMEI}/vehicle/vinStatus` | <pre>Signal(<br>  timestamp = timestamp,<br>  text = value),<br>)</pre> | |

## Data exploration
1. Open [the B-ON platform](https://iot.b-on.com/) and log in.
2. Explore the Vehicle assets and their data.
