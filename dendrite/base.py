from abc import ABCMeta, abstractmethod


class Row(object):
    def __init__(self, values, header):
        self.values = values
        self.header = header

    def __getitem__(self, item):
        ix = self.header.index(item)
        return self.values[ix]

    def __len__(self):
        return len(self.values)


class Feature(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def generate(row):
        pass


class Model(metaclass=ABCMeta):
    def __init__(self, dataset=None):
        self.dataset = dataset
        self.features = []
        self.header = None

    def update_dataset(self, dataset, header):
        self.header = header
        self.dataset = []
        for i in range(len(dataset)):
            assert len(dataset[i]) == len(dataset[i - 1])
            self.dataset.append(Row(dataset[i], self.header))
        assert len(self.header) == len(self.dataset[0])

    def add_feature(self, *features):
        for feature in features:
            assert issubclass(feature, Feature)
            self.features.append(feature())

    def map_row(self, row):
        output = []
        for feature in self.features:
            output.append(feature.generate(row))
        return output

    def map_rows(self, rows):
        output = []
        for row in rows:
            output.append(self.map_row(row))
        return output

    def map_dataset(self):
        return self.map_rows(self.dataset)
