from typing import Callable, Iterator


class MSSBase(object):
    monitors = []  # type: list
    image = None  # type: bytes
    width = 0  # type: int
    height = 0  # type: int

    def __enter__(self) -> object: ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def bgra_to_rgb(self, raw: bytearray) -> bytes: ...
    def enum_display_monitors(self, force: bool=False) -> list: ...
    def get_pixels(self, monitor: dict) -> bytes: ...
    def save(self, mon: int=0, output: str='monitor-%d.png', callback: Callable[[str], None]=None) -> Iterator[str]: ...
    def to_png(self, data: bytes, output: str) -> None: ...