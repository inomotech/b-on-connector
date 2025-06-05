from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChargeStatistics(_message.Message):
    __slots__ = ["ac_energy", "dc_energy", "lat", "lon", "pac_avg", "pac_max", "soc_percent_end", "soc_percent_start", "timestamp_end", "timestamp_start", "vin"]
    AC_ENERGY_FIELD_NUMBER: _ClassVar[int]
    DC_ENERGY_FIELD_NUMBER: _ClassVar[int]
    LAT_FIELD_NUMBER: _ClassVar[int]
    LON_FIELD_NUMBER: _ClassVar[int]
    PAC_AVG_FIELD_NUMBER: _ClassVar[int]
    PAC_MAX_FIELD_NUMBER: _ClassVar[int]
    SOC_PERCENT_END_FIELD_NUMBER: _ClassVar[int]
    SOC_PERCENT_START_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_END_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_START_FIELD_NUMBER: _ClassVar[int]
    VIN_FIELD_NUMBER: _ClassVar[int]
    ac_energy: float
    dc_energy: float
    lat: float
    lon: float
    pac_avg: float
    pac_max: float
    soc_percent_end: float
    soc_percent_start: float
    timestamp_end: int
    timestamp_start: int
    vin: str
    def __init__(self, vin: _Optional[str] = ..., timestamp_start: _Optional[int] = ..., timestamp_end: _Optional[int] = ..., soc_percent_start: _Optional[float] = ..., soc_percent_end: _Optional[float] = ..., ac_energy: _Optional[float] = ..., dc_energy: _Optional[float] = ..., pac_avg: _Optional[float] = ..., pac_max: _Optional[float] = ..., lat: _Optional[float] = ..., lon: _Optional[float] = ...) -> None: ...

class DriveStatistics(_message.Message):
    __slots__ = ["belt_use_count", "delivery_stops", "door_lock_count", "door_open_count", "drivemode_d_time", "drivemode_e_time", "drivemode_n_time", "drivemode_p_time", "drivemode_r_time", "driving_time", "energy_integrated", "hand_brake_count", "ignition_count", "ignition_time", "km_end", "km_start", "lat_end", "lat_start", "lon_end", "lon_start", "recuperated_energy", "soc_percent_end", "soc_percent_start", "speed_avg", "speed_max", "timestamp_end", "timestamp_start", "vin"]
    BELT_USE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_STOPS_FIELD_NUMBER: _ClassVar[int]
    DOOR_LOCK_COUNT_FIELD_NUMBER: _ClassVar[int]
    DOOR_OPEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    DRIVEMODE_D_TIME_FIELD_NUMBER: _ClassVar[int]
    DRIVEMODE_E_TIME_FIELD_NUMBER: _ClassVar[int]
    DRIVEMODE_N_TIME_FIELD_NUMBER: _ClassVar[int]
    DRIVEMODE_P_TIME_FIELD_NUMBER: _ClassVar[int]
    DRIVEMODE_R_TIME_FIELD_NUMBER: _ClassVar[int]
    DRIVING_TIME_FIELD_NUMBER: _ClassVar[int]
    ENERGY_INTEGRATED_FIELD_NUMBER: _ClassVar[int]
    HAND_BRAKE_COUNT_FIELD_NUMBER: _ClassVar[int]
    IGNITION_COUNT_FIELD_NUMBER: _ClassVar[int]
    IGNITION_TIME_FIELD_NUMBER: _ClassVar[int]
    KM_END_FIELD_NUMBER: _ClassVar[int]
    KM_START_FIELD_NUMBER: _ClassVar[int]
    LAT_END_FIELD_NUMBER: _ClassVar[int]
    LAT_START_FIELD_NUMBER: _ClassVar[int]
    LON_END_FIELD_NUMBER: _ClassVar[int]
    LON_START_FIELD_NUMBER: _ClassVar[int]
    RECUPERATED_ENERGY_FIELD_NUMBER: _ClassVar[int]
    SOC_PERCENT_END_FIELD_NUMBER: _ClassVar[int]
    SOC_PERCENT_START_FIELD_NUMBER: _ClassVar[int]
    SPEED_AVG_FIELD_NUMBER: _ClassVar[int]
    SPEED_MAX_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_END_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_START_FIELD_NUMBER: _ClassVar[int]
    VIN_FIELD_NUMBER: _ClassVar[int]
    belt_use_count: int
    delivery_stops: int
    door_lock_count: int
    door_open_count: int
    drivemode_d_time: float
    drivemode_e_time: float
    drivemode_n_time: float
    drivemode_p_time: float
    drivemode_r_time: float
    driving_time: float
    energy_integrated: float
    hand_brake_count: int
    ignition_count: int
    ignition_time: float
    km_end: float
    km_start: float
    lat_end: float
    lat_start: float
    lon_end: float
    lon_start: float
    recuperated_energy: float
    soc_percent_end: float
    soc_percent_start: float
    speed_avg: float
    speed_max: float
    timestamp_end: int
    timestamp_start: int
    vin: str
    def __init__(self, vin: _Optional[str] = ..., timestamp_start: _Optional[int] = ..., timestamp_end: _Optional[int] = ..., km_start: _Optional[float] = ..., km_end: _Optional[float] = ..., soc_percent_start: _Optional[float] = ..., soc_percent_end: _Optional[float] = ..., ignition_count: _Optional[int] = ..., ignition_time: _Optional[float] = ..., delivery_stops: _Optional[int] = ..., driving_time: _Optional[float] = ..., drivemode_d_time: _Optional[float] = ..., drivemode_n_time: _Optional[float] = ..., drivemode_r_time: _Optional[float] = ..., drivemode_e_time: _Optional[float] = ..., drivemode_p_time: _Optional[float] = ..., energy_integrated: _Optional[float] = ..., recuperated_energy: _Optional[float] = ..., hand_brake_count: _Optional[int] = ..., door_open_count: _Optional[int] = ..., door_lock_count: _Optional[int] = ..., belt_use_count: _Optional[int] = ..., lat_start: _Optional[float] = ..., lon_start: _Optional[float] = ..., lat_end: _Optional[float] = ..., lon_end: _Optional[float] = ..., speed_max: _Optional[float] = ..., speed_avg: _Optional[float] = ...) -> None: ...
