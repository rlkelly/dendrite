from .. import Dataset, Feature


class Uniques(Feature):
    def __init__(self, dataset, column):
        self.dataset = dataset
        values = set()
        value_count = 0
        for row in dataset:
            values.add(row[column])
            if len(values) > self.MAX_FEATURES:
                raise Exception('Too Many Features')
        self.values = tuple(values)
