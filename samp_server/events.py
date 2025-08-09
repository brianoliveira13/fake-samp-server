import threading
from typing import Callable, Optional, Any

class Event:
    def __init__(self):
        self._func: Optional[Callable] = None
        self._lock = threading.Lock()

    def set(self, func: Callable):
        with self._lock:
            self._func = func

    def call(self, *args, **kwargs) -> Any:
        with self._lock:
            if self._func:
                return self._func(*args, **kwargs)
            return None