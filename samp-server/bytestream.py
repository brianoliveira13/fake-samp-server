import struct
from io import BytesIO
from typing import Optional, Any

class ByteStream:
    def __init__(self, data: bytes = b''):
        self._stream = BytesIO(data)

    def set_stream(self, stream: BytesIO):
        self._stream = stream

    def read_num(self, fmt: str, pos: Optional[int] = None) -> Any:
        if pos is not None:
            self._stream.seek(pos)
        size = struct.calcsize(fmt)
        data = self._stream.read(size)
        if len(data) < size:
            raise ValueError('no data to read')
        return struct.unpack('<' + fmt, data)[0]

    def read_str(self, length_fmt: str = 'I', pos: Optional[int] = None) -> str:
        if pos is not None:
            self._stream.seek(pos)
        length = self.read_num(length_fmt)
        data = self._stream.read(length)
        if len(data) < length:
            raise ValueError('no data to read the string')
        return data.decode('latin1', errors='ignore')

    def write_num(self, value: Any, fmt: str, pos: Optional[int] = None):
        if pos is not None:
            self._stream.seek(pos)
        data = struct.pack('<' + fmt, value)
        self._stream.write(data)

    def write_str(self, value: str, length_fmt: str = 'I', pos: Optional[int] = None):
        if pos is not None:
            self._stream.seek(pos)
        encoded = value.encode('latin1', errors='ignore')
        length = len(encoded)
        self.write_num(length, length_fmt)
        self._stream.write(encoded)

    def get(self) -> bytes:
        current_pos = self._stream.tell()
        self._stream.seek(0)
        data = self._stream.read()
        self._stream.seek(current_pos)
        return data

    def get_position(self) -> int:
        return self._stream.tell()

    def seek(self, pos: int):
        self._stream.seek(pos)