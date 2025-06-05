from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ValuePerPhase(_message.Message):
    __slots__ = ["phase1", "phase2", "phase3"]
    PHASE1_FIELD_NUMBER: _ClassVar[int]
    PHASE2_FIELD_NUMBER: _ClassVar[int]
    PHASE3_FIELD_NUMBER: _ClassVar[int]
    phase1: int
    phase2: int
    phase3: int
    def __init__(self, phase1: _Optional[int] = ..., phase2: _Optional[int] = ..., phase3: _Optional[int] = ...) -> None: ...
