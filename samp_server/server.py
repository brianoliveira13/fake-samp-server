import socket
from typing import Optional
from .events import Event
from .bytestream import ByteStream
from .packet import QueryPacket
from .query import QueryType

class SAMPServer:
    def __init__(self):
        self.socket: Optional[socket.socket] = None
        self._running = False
        self.server_info = Event()
        self.server_rules = Event()

    def init(self, port: int):
        try:
            self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self._socket.bind(('127.0.0.1', port))
            print(f'samp server started on port {port}')
            self._running = True
        except Exception as e:
            print(f'error starting server: {e}')
            raise

    def monitor(self):
        if not self._socket:
            return
        self._socket.settimeout(1.0)

        while self._running:
            try:
                data, addr = self._socket.recvfrom(512)
                if len(data) > 0:
                    self._process_packet(data, addr)
            except socket.timeout:
                continue
            except Exception as e:
                print(f'error receiving data: {e}')
                break

    def _process_packet(self, data: bytes, addr: tuple):
        try:
            if len(data) < 11:
                return
            
            query = QueryPacket(data)
            bs = ByteStream()
            result = None

            if query.type == QueryType.SERVER_INFO:
                result = self.server_info.call(bs, query)
            elif query.type == QueryType.SERVER_RULES:
                result = self.server_rules.call(bs, query)
            else:
                return
            
            self._socket.sendto(result, addr)
        except Exception as e:
            print(f'error processing packet: {e}')

    def shutdown(self):
        self._running = False
        if self._socket:
            self._socket.close()
            self._socket = None