from .. import Dataset, Feature


class OneHotEncoder(Feature):
    description = "creates_one_hot_encoding"
    column = 0
    MAX_FEATURES = 25

    def __init__(self, dataset=None):
        values = set()
        value_count = 0
        for row in dataset:
            value_count += 1
            values.add(row[self.column])
            if value_count > self.MAX_FEATURES:
                raise Exception('Too Many Features')
        self.values = tuple(values)

    def __call__(self, dataset=None):
        self.__init__(dataset)

    def get_name(self):
        return [f'{self.name}_{value}' for value in self.values]

    def make_dataset(self, dataset):
        # TODO: kludge
        return Dataset([self.transform(row) for row in dataset])

    def transform(self, row):
        output = [0] * len(self.values)
        output[self.values.index(row[self.column])] = 1
        return output
