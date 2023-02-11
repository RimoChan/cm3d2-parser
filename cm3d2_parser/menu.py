import io
import struct
from dataclasses import dataclass
from typing import Dict, List

from .utils import dump_str, read_str


@dataclass
class Menu:
    version: int
    text_path: str
    name: str
    category: str
    description: str
    attrs: Dict[str, List[list]]


def load_menu(b: bytes) -> Menu:
    f = io.BytesIO(b)
    assert read_str(f) == 'CM3D2_MENU'
    version = struct.unpack('<i', f.read(4))[0]
    text_path = read_str(f)
    name = read_str(f)
    category = read_str(f)
    description = read_str(f)
    length, = struct.unpack('<i', f.read(4))
    attrs = {}
    for _ in range(99999):
        c = []
        n = ord(f.read(1))
        if n == 0:
            break
        for _ in range(n):
            c.append(read_str(f))
        attrs.setdefault(c[0], []).append(c[1:])
    return Menu(version, text_path, name, category, description, attrs)


def dump_menu(menu: Menu) -> bytes:
    f = io.BytesIO()
    f.write(dump_str('CM3D2_MENU'))
    f.write(struct.pack('<i', menu.version))
    f.write(dump_str(menu.text_path))
    f.write(dump_str(menu.name))
    f.write(dump_str(menu.category))
    f.write(dump_str(menu.description))
    f2 = io.BytesIO()
    for k, v in menu.attrs.items():
        for i in v:
            f2.write(struct.pack('<B', len(i)+1))
            f2.write(dump_str(k))
            for j in i:
                f2.write(dump_str(j))
    f2.write(struct.pack('<B', 0))
    f2v = f2.getvalue()
    f.write(struct.pack('<i', len(f2v)))
    f.write(f2v)
    return f.getvalue()
