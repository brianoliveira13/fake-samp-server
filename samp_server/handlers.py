from .bytestream import ByteStream
from .packet import QueryPacket

def handle_server_info(bs: ByteStream, query: QueryPacket):
    response = ByteStream()
    response._stream.write(query.samp_bytes)
    response._stream.write(query.server_ip)
    response._stream.write(query.server_port)
    response._stream.write(bytes([ord('i')]))
    response.write_num(0, 'B')
    response.write_num(422, 'H') 
    response.write_num(500, 'H')
    response.write_str('Mega Bomba Roleplay', 'I')
    response.write_str('RPG', 'I')
    response.write_str('Spanish', 'I')
    return response.get()

def handle_server_rules(bs: ByteStream, query: QueryPacket):
    response = ByteStream()
    response._stream.write(query.samp_bytes)
    response._stream.write(query.server_ip)
    response._stream.write(query.server_port)
    response._stream.write(bytes([ord('r')]))

    rules = {
        "lagcomp": "1",
        "mapname": "San Andreas",
        "version": "0.3.7",
        "weather": "10",
        "worldtime": "12:00",
        "weburl": "https://github.com/brianoliveira13/fake-samp-server"
    }
    response.write_num(len(rules), 'H')

    for key, value in rules.items():
        response.write_str(key, 'B')
        response.write_str(value, 'B')
    return response.get() 