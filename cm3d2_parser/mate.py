import io
import struct
from dataclasses import dataclass
from typing import List

from .utils import dump_str, read_str


@dataclass
class Mate:
    version: int
    name1: str
    name2: str
    shader1: str
    shader2: str
    texture: List[tuple]
    color: List[tuple]
    flt: List[tuple]


def load_mate(b: bytes) -> Mate:
    f = io.BytesIO(b)
    assert read_str(f) == 'CM3D2_MATERIAL'
    version = struct.unpack('<i', f.read(4))[0]
    name1, name2, shader1, shader2 = read_str(f), read_str(f), read_str(f), read_str(f)
    texture = {}
    color = {}
    flt = {}
    for _ in range(99999):
        content_type = read_str(f)
        if content_type == 'end':
            break
        key = read_str(f)
        if content_type == 'tex':
            tex_type = read_str(f)
            c = [tex_type]
            if tex_type == 'tex2d':
                c += [read_str(f), read_str(f), struct.unpack('<4f', f.read(4 * 4))]
            texture[key] = c
        elif content_type == 'col':
            color[key] = struct.unpack('<4f', f.read(4 * 4))
        elif content_type == 'f':
            flt[key] = struct.unpack('<f', f.read(4))[0]
        else:
            raise Exception('Unknown content type: ' + content_type)
    return Mate(version, name1, name2, shader1, shader2, texture, color, flt)


def dump_mate(mate: Mate) -> bytes:
    f = io.BytesIO()
    f.write(dump_str('CM3D2_MATERIAL'))
    f.write(struct.pack('<i', mate.version))
    for i in mate.name1, mate.name2, mate.shader1, mate.shader2:
        f.write(dump_str(i))
    for k, v in mate.texture.items():
        f.write(dump_str('tex'))
        f.write(dump_str(k))
        for i in v:
            if isinstance(i, str):
                f.write(dump_str(i))
            else:
                f.write(struct.pack('<4f', *i))
    for k, v in mate.color.items():
        f.write(dump_str('col'))
        f.write(dump_str(k))
        f.write(struct.pack('<4f', *v))
    for k, v in mate.flt.items():
        f.write(dump_str('f'))
        f.write(dump_str(k))
        f.write(struct.pack('<f', v))
    f.write(dump_str('end'))
    return f.getvalue()
