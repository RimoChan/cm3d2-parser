import os
from pathlib import Path
from typing import Union

from .mate import dump_mate, load_mate, Mate
from .menu import dump_menu, load_menu, Menu
from .tex import dump_tex, load_tex, Texture

PathLike = Union[str, bytes, os.PathLike]


_d = {
    '.mate': (load_mate, dump_mate),
    '.menu': (load_menu, dump_menu),
    '.tex': (load_tex, dump_tex),
}


def cm3d2_load(p: PathLike) -> Union[Mate, Menu, Texture]:
    p = Path(p)
    if t:= _d.get(p.suffix):
        return t[0](p.read_bytes())
    else:
        raise Exception('Unknown file type: ' + p.suffix)


def cm3d2_dump(p: PathLike, data: Union[Mate, Menu, Texture]):
    p = Path(p)
    if t:= _d.get(p.suffix):
        p.write_bytes(t[1](data))
    else:
        raise Exception('Unknown file type: ' + p.suffix)
