import numpy as np
from sklearn.model_selection import train_test_split

from .. import Feature, DataModel, Dataset, Row, Target
from ..dataset_types import NumpyDataset, NumpyTarget

class TrainTestSplit(object):
    def __init__(self, X, y, test_size=0.5):
        self.X = X
        self.y = y
        self.test_size = test_size

    def split(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X.to_array(), self.y.to_array(), test_size=self.test_size)
        return NumpyDataset(X_train), NumpyDataset(X_test), NumpyTarget(y_train), NumpyTarget(y_test)
