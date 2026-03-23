"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 1.2.0
"""

import numpy as np
from scipy.ndimage import distance_transform_edt
from skimage.morphology import skeletonize
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

    # print(f"DEBUG result: {len(map_arrays)} map")
    return map_arrays

def _get_free_space(map_data: np.ndarray):
    if map_data is None:
        raise ValueError("No map loaded.")
    return (map_data == 0).astype(np.uint8)

def _generate_voronoi(map_data: np.ndarray) -> np.ndarray:
    # self.distance_field = distance_transform_edt(free_space)        
    return skeletonize(_get_free_space(map_data)).astype(np.uint8)

def _generate_distance_field(map_data: np.ndarray) -> np.ndarray:
    return distance_transform_edt(_get_free_space(map_data))

def generate_voronoi(maps_dict: dict[str, Callable[[], np.ndarray]]) -> dict[str, np.ndarray]:
    voronoi_dict = {}
    for name, map_data in maps_dict.items():
        voronoi_dict[name] = _generate_voronoi(map_data())
    # print(f"DEBUG result: {len(voronoi_dict)}")
    return voronoi_dict

def generate_distance_field(maps_dict: dict[str, Callable[[], np.ndarray]]) -> dict[str, np.ndarray]:
    distance_field_dict = {}
    for name, map_data in maps_dict.items():
        distance_field_dict[name] = _generate_distance_field(map_data())
    return distance_field_dict

