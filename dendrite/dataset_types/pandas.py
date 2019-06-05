from __future__ import annotations

import pandas as pd

from ..base import DataModel, Row, Dataset


class PandasDataset(Dataset):
    def __init__(self, dataset, header):
        self.dataset = pd.DataFrame(dataset, columns=header)

    @property
    def columns(self):
        return list(self.dataset.columns)

    @property
    def columns(self):
        return self.dataset.index.name

    def join(self, other: PandasDataset, left_index, right_index, how='inner', inplace=False):
        left = self.dataset.set_index(left_index)
        right = self.dataset.set_index(right_index)
        d = left.join(right, how=how)
        d.reset_index(inplace=True)
        if inplace:
            self.dataset = d
        return d
