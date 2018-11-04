from enum import IntEnum


class IndexDrives(IntEnum):
    """ This enum holds the index value of drive object entrys
    """
    ControlWord = 0x6040
    StatusWord = 0x6041
    OperationMode = 0x6060
