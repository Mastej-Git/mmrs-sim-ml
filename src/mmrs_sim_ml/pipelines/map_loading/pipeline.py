"""
This is a boilerplate pipeline 'map_loading'
generated using Kedro 1.2.0
"""

from kedro.pipeline import Node, Pipeline  # noqa

from .nodes import parse_maps


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
            func=parse_maps,
            inputs="raw_maps",
            outputs="processed_maps",
            name="parse_maps",
        ),
    ])
