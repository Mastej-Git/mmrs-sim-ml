"""
This is a boilerplate pipeline 'sector_division'
generated using Kedro 1.2.0
"""

from kedro.pipeline import Pipeline, Node

from .nodes import detect_col_sectors


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline([
        Node(
            func=detect_col_sectors,
            inputs={
                "agvs": "params:agvs",
                "bezier_points": "bezier_points",
            },
            outputs="collision_sectors",
            name="detect_col_sectors_node",
        ),
    ])
