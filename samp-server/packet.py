class QueryPacket:
    def __init__(self, data: bytes):
        if len(data) < 11:
            raise ValueError('packet too small')
        self.samp_bytes = data[0:4]
        self.server_ip = data[4:8]
        self.server_port = data[8:10]
        self.packet_type = data[10]