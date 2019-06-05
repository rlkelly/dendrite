from __future__ import annotations

import numpy as np

from ..base import DataModel, Row, Dataset, Target


class NumpyDataset(Dataset):
    def __init__(self, dataset, header=None):
        super(NumpyDataset, self).__init__(dataset, header)
        self.nd_array = np.array(dataset)

    def to_array(self):
        return self.nd_array

    def __getitem__(self, *key, **kwargs):
        return self.nd_array.__getitem__(*key, **kwargs)

class NumpyTarget(Target):
    def __init__(self, dataset, header=None):
        super(NumpyTarget, self).__init__(dataset, header)
        self.nd_array = np.array(dataset)

    def to_array(self):
        return self.nd_array

    def __getitem__(self, *key, **kwargs):
        return self.nd_array.__getitem__(*key, **kwargs)
