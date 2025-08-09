from .bytestream import ByteStream
from .packet import QueryPacket

def handle_server_info(bs: ByteStream, query: QueryPacket):
    bs = ByteStream()
    bs._stream.write(query.samp_bytes)
    bs._stream.write(query.server_ip)
    bs._stream.write(query.server_port)
    bs._stream.write(bytes([ord('i')]))
    return bs.get()

def handle_server_rules(bs: ByteStream, query: QueryPacket):
    bs = ByteStream()
    bs._stream.write(query.samp_bytes)
    bs._stream.write(query.server_ip)
    bs._stream.write(query.server_port)
    bs._stream.write(bytes([ord('r')]))

    rules = {
        "lagcomp": "1",
        "mapname": "San Andreas",
        "version": "0.3.7",
        "weather": "10",
        "worldtime": "12:00"
    }
    bs.write_num(len(rules), 'H')

    for key, value in rules.items():
        bs.write_str(key, 'B')
        bs.write_str(value, 'B')
    return bs.get() 