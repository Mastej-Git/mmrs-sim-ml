"""
This is a boilerplate pipeline 'path_generation'
generated using Kedro 1.2.0
"""

from kedro.pipeline import Pipeline, node

from .nodes import create_paths


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        node(
            func=create_paths,
            inputs="params:path_generation",
            outputs="bezier_points",
            name="create_paths_node",
        ),
    ])
