"""
This is a boilerplate pipeline 'voronoi_generation'
generated using Kedro 1.2.0
"""

import numpy as np
from scipy.ndimage import distance_transform_edt
from skimage.morphology import skeletonize
from typing import Callable


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
    # print(f"DEBUG wynik: {len(voronoi_dict)}")
    return voronoi_dict

def generate_distance_field(maps_dict: dict[str, Callable[[], np.ndarray]]) -> dict[str, np.ndarray]:
    distance_field_dict = {}
    for name, map_data in maps_dict.items():
        distance_field_dict[name] = _generate_distance_field(map_data())
    return distance_field_dict
