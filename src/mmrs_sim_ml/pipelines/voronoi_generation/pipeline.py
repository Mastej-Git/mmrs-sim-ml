"""
This is a boilerplate pipeline 'voronoi_generation'
generated using Kedro 1.2.0
"""

from kedro.pipeline import Node, Pipeline  # noqa

from .nodes import generate_voronoi, generate_distance_field

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
            func=generate_voronoi,
            inputs="processed_maps",
            outputs="voronoi_data",
            name="generate_voronoi",
        ),
        Node(
            func=generate_distance_field,
            inputs="processed_maps",
            outputs="distance_field_data",
            name="generate_distance_field",
        ),
    ])
