from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sts.v2 import types_pb2 as _types_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

CHARGE_PLUG_STATUS_CONNECTED_LOCKED: ChargePlugStatus
CHARGE_PLUG_STATUS_CONNECTED_UNLOCKED: ChargePlugStatus
CHARGE_PLUG_STATUS_DISCONNECTED: ChargePlugStatus
CHARGE_PLUG_STATUS_LOCKING_ERROR: ChargePlugStatus
CHARGE_PLUG_STATUS_UNSPECIFIED: ChargePlugStatus
CONNECTIVITY_STATUS_OFFLINE: ConnectivityStatus
CONNECTIVITY_STATUS_OFFLINE_UNGRACEFUL: ConnectivityStatus
CONNECTIVITY_STATUS_ONLINE: ConnectivityStatus
CONNECTIVITY_STATUS_UNSPECIFIED: ConnectivityStatus
DESCRIPTOR: _descriptor.FileDescriptor
IGNITION_STATUS_ACCESSORY: IgnitionStatus
IGNITION_STATUS_OFF: IgnitionStatus
IGNITION_STATUS_ON: IgnitionStatus
IGNITION_STATUS_UNSPECIFIED: IgnitionStatus
POWER_SETTING_TYPE_CHARGING_POWER: PowerSettingType
POWER_SETTING_TYPE_CHARGING_SCHEDULE: PowerSettingType
POWER_SETTING_TYPE_FALLBACK_SCHEDULE: PowerSettingType
POWER_SETTING_TYPE_INTERNAL: PowerSettingType
POWER_SETTING_TYPE_UNSPECIFIED: PowerSettingType
PRECONDITIONING_SLICE_STATUS_CANCELLED_CUTOFF_AMBIENT_TEMPERATURE: PreconditioningSliceStatus
PRECONDITIONING_SLICE_STATUS_CANCELLED_CUTOFF_SOC: PreconditioningSliceStatus
PRECONDITIONING_SLICE_STATUS_CANCELLED_INTERNAL_ERROR: PreconditioningSliceStatus
PRECONDITIONING_SLICE_STATUS_CANCELLED_UNPLUGGED: PreconditioningSliceStatus
PRECONDITIONING_SLICE_STATUS_END: PreconditioningSliceStatus
PRECONDITIONING_SLICE_STATUS_START: PreconditioningSliceStatus
PRECONDITIONING_SLICE_STATUS_UNSPECIFIED: PreconditioningSliceStatus

class ACCurrentRealized(_message.Message):
    __slots__ = ["realized_ac_current", "rpc_id", "slice_id", "type"]
    REALIZED_AC_CURRENT_FIELD_NUMBER: _ClassVar[int]
    RPC_ID_FIELD_NUMBER: _ClassVar[int]
    SLICE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    realized_ac_current: _types_pb2.ValuePerPhase
    rpc_id: bytes
    slice_id: int
    type: PowerSettingType
    def __init__(self, realized_ac_current: _Optional[_Union[_types_pb2.ValuePerPhase, _Mapping]] = ..., type: _Optional[_Union[PowerSettingType, str]] = ..., rpc_id: _Optional[bytes] = ..., slice_id: _Optional[int] = ...) -> None: ...

class ChargingDcPowerMax(_message.Message):
    __slots__ = ["derating_justified", "derating_unjustified"]
    DERATING_JUSTIFIED_FIELD_NUMBER: _ClassVar[int]
    DERATING_UNJUSTIFIED_FIELD_NUMBER: _ClassVar[int]
    derating_justified: int
    derating_unjustified: int
    def __init__(self, derating_justified: _Optional[int] = ..., derating_unjustified: _Optional[int] = ...) -> None: ...

class OnlineStatus(_message.Message):
    __slots__ = ["connectivity_status", "protocol_version"]
    CONNECTIVITY_STATUS_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_VERSION_FIELD_NUMBER: _ClassVar[int]
    connectivity_status: ConnectivityStatus
    protocol_version: str
    def __init__(self, connectivity_status: _Optional[_Union[ConnectivityStatus, str]] = ..., protocol_version: _Optional[str] = ...) -> None: ...

class Position(_message.Message):
    __slots__ = ["lat", "lon"]
    LAT_FIELD_NUMBER: _ClassVar[int]
    LON_FIELD_NUMBER: _ClassVar[int]
    lat: float
    lon: float
    def __init__(self, lat: _Optional[float] = ..., lon: _Optional[float] = ...) -> None: ...

class PreconditioningStatus(_message.Message):
    __slots__ = ["preconditioning_schedule_request_id", "preconditioning_schedule_slice_id", "slice_status"]
    PRECONDITIONING_SCHEDULE_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONING_SCHEDULE_SLICE_ID_FIELD_NUMBER: _ClassVar[int]
    SLICE_STATUS_FIELD_NUMBER: _ClassVar[int]
    preconditioning_schedule_request_id: bytes
    preconditioning_schedule_slice_id: int
    slice_status: PreconditioningSliceStatus
    def __init__(self, preconditioning_schedule_request_id: _Optional[bytes] = ..., preconditioning_schedule_slice_id: _Optional[int] = ..., slice_status: _Optional[_Union[PreconditioningSliceStatus, str]] = ...) -> None: ...

class Signal(_message.Message):
    __slots__ = ["ac_current_realized", "charge_plug_status", "charging_dc_power_max", "connectivity_status", "ignition_status", "integer_number", "online_status", "position", "preconditioning_status", "real_number", "text", "timestamp", "value_per_phase"]
    AC_CURRENT_REALIZED_FIELD_NUMBER: _ClassVar[int]
    CHARGE_PLUG_STATUS_FIELD_NUMBER: _ClassVar[int]
    CHARGING_DC_POWER_MAX_FIELD_NUMBER: _ClassVar[int]
    CONNECTIVITY_STATUS_FIELD_NUMBER: _ClassVar[int]
    IGNITION_STATUS_FIELD_NUMBER: _ClassVar[int]
    INTEGER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ONLINE_STATUS_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    PRECONDITIONING_STATUS_FIELD_NUMBER: _ClassVar[int]
    REAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    VALUE_PER_PHASE_FIELD_NUMBER: _ClassVar[int]
    ac_current_realized: ACCurrentRealized
    charge_plug_status: ChargePlugStatus
    charging_dc_power_max: ChargingDcPowerMax
    connectivity_status: ConnectivityStatus
    ignition_status: IgnitionStatus
    integer_number: int
    online_status: OnlineStatus
    position: Position
    preconditioning_status: PreconditioningStatus
    real_number: float
    text: str
    timestamp: _timestamp_pb2.Timestamp
    value_per_phase: _types_pb2.ValuePerPhase
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., text: _Optional[str] = ..., real_number: _Optional[float] = ..., integer_number: _Optional[int] = ..., position: _Optional[_Union[Position, _Mapping]] = ..., charge_plug_status: _Optional[_Union[ChargePlugStatus, str]] = ..., connectivity_status: _Optional[_Union[ConnectivityStatus, str]] = ..., online_status: _Optional[_Union[OnlineStatus, _Mapping]] = ..., ignition_status: _Optional[_Union[IgnitionStatus, str]] = ..., preconditioning_status: _Optional[_Union[PreconditioningStatus, _Mapping]] = ..., charging_dc_power_max: _Optional[_Union[ChargingDcPowerMax, _Mapping]] = ..., value_per_phase: _Optional[_Union[_types_pb2.ValuePerPhase, _Mapping]] = ..., ac_current_realized: _Optional[_Union[ACCurrentRealized, _Mapping]] = ...) -> None: ...

class ChargePlugStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ConnectivityStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class IgnitionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class PreconditioningSliceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class PowerSettingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
