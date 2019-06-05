from .. import Dataset, Feature


class LabelEncoder(Feature):
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
        return self.values.index(row)
