"""
This is a boilerplate pipeline 'path_generation'
generated using Kedro 1.2.0
"""

from kedro.pipeline import Pipeline, Node

from .nodes import create_paths


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
            func=create_paths,
            inputs="params:agvs",
            outputs="bezier_points",
            name="create_paths_node",
        ),
    ])
