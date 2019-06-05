from sklearn.linear_model import LogisticRegressor

from ..predictor import Predictor
from ..dataset import Dataset


class LogisticRegressor(Predictor):
    """For regression with a single dimensional target variable"""
    def __init__(self, *args, **kwargs):
        self.lr = LogisticRegressor(*args, **kwargs)
        self.prediction = None

    def fit(self, dataset, target):
        ds = [d.values for d in dataset.dataset]
        t = [t.values for t in target.dataset]
        self.lr.fit(ds, t)

    def predict(self, rows):
        self.prediction = Dataset(self.lr.predict([r.values for r in rows]))
        return self.prediction

    def score(self, input, output):
        return self.lr.score(input, output)

    def print_model(self):
        for i, classifier in enumerate(self.lr.coef_):
            print(' + '.join([
                f'x{i} * {b}' for i, b in enumerate(classifier)
            ]) + f' + {self.lr.intercept_[i]}')
