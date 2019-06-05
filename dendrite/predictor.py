from abc import ABCMeta, abstractmethod


class Predictor(metaclass=ABCMeta):
    @abstractmethod
    def fit(row):
        pass

    @abstractmethod
    def predict(row):
        pass

    @abstractmethod
    def score(row):
        pass
