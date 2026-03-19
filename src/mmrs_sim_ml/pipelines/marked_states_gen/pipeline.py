"""
This is a boilerplate pipeline 'marked_states_gen'
generated using Kedro 1.2.0
"""

from kedro.pipeline import Node, Pipeline  # noqa

from .nodes import random_ms_gen

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
            func=random_ms_gen,
            inputs={
                "agvs": "params:agvs",
                "maps_dict": "processed_maps",
                "voronoi_skeleton": "voronoi_data",
                "distance_field": "distance_field_data"
            },
            outputs="random_ms_data",
            name="random_ms_gen",
        ),
    ])
