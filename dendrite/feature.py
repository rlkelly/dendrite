from abc import ABCMeta, abstractmethod
import re


class Feature(metaclass=ABCMeta):
    def __init__(self, dataset=None):
        pass

    def __call__(self, dataset=None):
        pass

    @property
    def name(self):
        name = type(self).__name__
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def columns(self):
        return self.name

    def perform_transform(self, row):
        try:
            return self.transform(row)
        except Exception as e:
            raise Exception(e)

    @staticmethod
    @abstractmethod
    def transform(row):
        pass

    def execute(self, row):
        return self.perform_transform(row)
