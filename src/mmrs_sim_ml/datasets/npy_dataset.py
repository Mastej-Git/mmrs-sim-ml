
import numpy as np
from pathlib import Path
from typing import Any, Dict
from kedro.io import AbstractDataset


class NpyDataset(AbstractDataset):
    def __init__(self, filepath: str):
        self._filepath = Path(filepath)

    def _load(self) -> np.ndarray:
        return np.load(self._filepath)

    def _save(self, data: np.ndarray) -> None:
        self._filepath.parent.mkdir(parents=True, exist_ok=True)
        np.save(self._filepath, data)

    def _describe(self) -> Dict[str, Any]:
        return {"filepath": self._filepath}
    