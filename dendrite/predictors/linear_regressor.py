from sklearn.linear_model import LinearRegression

from ..predictor import Predictor


class LinearRegressor(Predictor):
    def __init__(self, *args, **kwargs):
        self.lr = LinearRegression(*args, **kwargs)

    def fit(self, dataset, target):
        ds = [d.values for d in dataset.dataset]
        t = [t.values for t in target.dataset]
        self.lr.fit(ds, t)

    def predict(self, rows):
        return self.lr.predict([r.values for r in rows])

    def score(self):
        raise NotImplementedException()
