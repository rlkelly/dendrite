from .. import Dataset, Feature
from .uniques import Uniques

class OneHotEncoder(Uniques):
    description = "creates_one_hot_encoding"
    column = 0 # Must set on creation
    MAX_FEATURES = 25

    def __init__(self, dataset=None):
        super(OneHotEncoder, self).__init__(dataset, self.column)

    def __call__(self, dataset=None):
        if dataset:
            self.__init__(dataset)
        return Dataset([self.transform(row) for row in self.dataset])

    def columns(self):
        return [f'{self.name}_{value}' for value in self.values]

    def transform(self, row):
        output = [0] * len(self.values)
        output[self.values.index(row[self.column])] = 1
        return output
