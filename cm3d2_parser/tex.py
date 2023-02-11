import io
import struct
from dataclasses import dataclass
from typing import Optional, List, Tuple

from .utils import dump_str, read_str


@dataclass
class Texture:
    version: int
    text_path: str
    tex_format: int
    uv_rects: Optional[List[Tuple]]
    width: Optional[int]
    height: Optional[int]
    png_data: bytes


def load_tex(data: bytes) -> Texture:
    f = io.BytesIO(data)
    assert read_str(f) == 'CM3D2_TEX'
    version, = struct.unpack('<i', f.read(4))
    text_path = read_str(f)
    tex_format = 5
    width = height = uv_rects = None
    if version >= 1010:
        if version >= 1011:
            num_rect, = struct.unpack('<i', f.read(4))
            uv_rects = []
            for _ in range(num_rect):
                # x, y, w, h
                uv_rects.append( struct.unpack('<4f', f.read(4 * 4)) )
        width, height, tex_format = struct.unpack('<3i', f.read(4 * 3))
    png_size, = struct.unpack('<i', f.read(4))
    png_data = f.read(png_size)
    return Texture(version, text_path, tex_format, uv_rects, width, height, png_data)


def dump_tex(tex: Texture) -> bytes:
    f = io.BytesIO()
    f.write(dump_str('CM3D2_TEX'))
    f.write(struct.pack('<i', tex.version))
    f.write(dump_str(tex.text_path))
    if tex.version >= 1010:
        if tex.version >= 1011:
            f.write(struct.pack('<i', len(tex.uv_rects)))
            for uv_rect in tex.uv_rects:
                f.write(struct.pack('<4f', *uv_rect))
        f.write(struct.pack('<3i', tex.width, tex.height, tex.tex_format))
    f.write(struct.pack('<i', len(tex.png_data)))
    f.write(tex.png_data)
    return f.getvalue()
