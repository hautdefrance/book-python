from enum import Enum


class Permission(Enum):
    READ_WRITE_EXECUTE = 0b111
    READ_WRITE = 0b110
    READ_EXECUTE = 0b101
    READ = 0b100
    WRITE_EXECUTE = 0b011
    WRITE = 0b010
    EXECUTE = 0b001
    NONE = 0b000
