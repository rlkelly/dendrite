from sklearn.linear_model import LinearRegression

from ..predictor import Predictor
from ..dataset import Dataset


class LinearRegressor(Predictor):
    """For regression with a single dimensional target variable"""
    def __init__(self, *args, **kwargs):
        self.lr = LinearRegression(*args, **kwargs)

    def fit(self, dataset, target):
        ds = [d.values for d in dataset.dataset]
        t = [t.values for t in target.dataset]
        self.lr.fit(ds, t)

    def predict(self, rows):
        return Dataset(self.lr.predict([r.values for r in rows]))

    def score(self):
        raise NotImplementedException()

    def print_model(self):
        print(' + '.join([
            f'x{i} * {b}' for i, b in enumerate(self.lr.coef_[0])
        ]) + f' + {self.lr.intercept_[0]}')
