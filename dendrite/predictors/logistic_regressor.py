from sklearn.linear_model import LogisticRegression

from ..predictor import Predictor
from ..dataset import Dataset


class LogisticRegressor(Predictor):
    """For single-class Logistic Regression"""
    def __init__(self, *args, **kwargs):
        self.lr = LogisticRegression(*args, solver='lbfgs', **kwargs)
        self.prediction = None

    def fit(self, dataset, target):
        ds = dataset.to_array()
        t = [t[0] for t in target.to_array()]
        self.lr.fit(ds, t)
        return self

    def predict(self, dataset):
        self.prediction = Dataset(self.lr.predict(dataset.to_array()))
        return self.prediction

    def score(self, input, output):
        return self.lr.score(input, output)

    def print_model(self):
        for i, classifier in enumerate(self.lr.coef_):
            print(' + '.join([
                f'x{i} * {b}' for i, b in enumerate(classifier)
            ]) + f' + {self.lr.intercept_[i]}')

    def __getattr__(self, name):
        # TODO: this is just a demonstration of an idea
        def method(*args, **kwargs):
            m = getattr(self.lr, name)
            return m(*args, **kwargs)
        return method
