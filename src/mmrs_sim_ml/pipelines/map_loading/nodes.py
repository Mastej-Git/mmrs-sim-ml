"""
This is a boilerplate pipeline 'map_loading'
generated using Kedro 1.2.0
"""


import os
import numpy as np
from typing import Callable


def _parse_map(file_name) -> np.ndarray:
    with open(file_name, 'r') as f:
        lines = f.readlines()
    
    height = int(lines[1].split()[1])
    width = int(lines[2].split()[1])
    
    map_lines = lines[4:4 + height]
    
    map_data = np.zeros((height, width), dtype=np.uint8)
    for row, line in enumerate(map_lines):
        for col, char in enumerate(line.rstrip('\n')):
            if col < width:
                map_data[row, col] = 1 if char == '@' else 0
    
    return map_data

def parse_maps(raw_maps_zip: dict[str, Callable]) -> dict[str, np.ndarray]:

    map_arrays = {}
    
    for filename in raw_maps_zip.keys():
        if not filename.endswith('256'):
            continue
        array = _parse_map("data/01_raw/maps/" + filename + ".map")
        map_arrays[filename] = array

    # print(f"DEBUG wynik: {len(map_arrays)} map")
    return map_arrays