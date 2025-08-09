from enum import IntEnum

class QueryType(IntEnum):
    SERVER_INFO = ord('i')
    SERVER_RULES = ord('r')
    SERVER_PING = ord('p')