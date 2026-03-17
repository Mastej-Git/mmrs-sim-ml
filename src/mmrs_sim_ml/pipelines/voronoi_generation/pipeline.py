"""
This is a boilerplate pipeline 'voronoi_generation'
generated using Kedro 1.2.0
"""

from kedro.pipeline import Node, Pipeline  # noqa

from .nodes import generate_voronoi

def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
            func=generate_voronoi,
            inputs="processed_maps",
            outputs="voronoi_data",
            name="generate_voronoi",
        ),
    ])
