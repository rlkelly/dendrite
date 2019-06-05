import collections
from typing import List, Type

from .dataset import Dataset
from .feature import Feature
from .predictor import Predictor
from .row import Row
from .row_select import RowSelect
from .target import Target


def flatten(x):
    if isinstance(x, list):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]


class DataModel:
    def __init__(self, dataset=None):
        self.dataset = dataset
        self.features = []
        # TODO: do I need an index?

    @property
    def header(self):
        return self.dataset.header

    def get_new_header(self):
        return [feature.columns() for feature in self.features]

    def update_dataset(self, dataset, header):
        self.header = header
        self.dataset = []
        for i in range(len(dataset)):
            assert len(dataset[i]) == len(dataset[i - 1])
            self.dataset.append(Row(dataset[i]))
        assert len(self.header) == len(self.dataset[0])

    def add_features(self, *features):
        return self.add_feature(*features)

    def add_feature(self, *features):
        for feature in features:
            assert issubclass(feature, Feature)
            self.features.append(feature(self.dataset))

    def map_row_value(self, row: Row):
        output = []
        for feature in self.features:
            output.append(feature.execute(row))
        return output

    def map_rows(self, rows: List[Row]):
        output = []
        for row in rows:
            output.append(Row(self.map_row_value(row)))
        return output

    def map_dataset(self, inplace=False):
        for feature in self.features:
            feature(self.dataset)
        d = Dataset(self.map_rows(self.dataset), self.get_new_header())
        if inplace:
            self.dataset = d
            self.features = []
        return d

    def __getitem__(self, index: int):
        return RowSelect(self.dataset[index], self.header)

    # def print_rows(self):
    #     header = ', '.join(self.header)
    #     print(header)
    #     print('-' * len(header))
    #     self.dataset.print_rows()

    def flatten(self, inplace=False):
        output = []
        for row in self.dataset:
            output.append(flatten(row.values))
        if inplace:
            self.dataset = Dataset(output, flatten(self.header))
        return output

    def add_predictor(self, predictor: Type[Predictor]):
        self.predictor = predictor

    def fit(self, target):
        self.target = target
        return self.predictor.fit(self.dataset, target)

    def predict(self, dataset):
        return self.predictor.predict(dataset)

    def score(self, dataset, target):
        return self.predictor.score(dataset, target)

    def print_model(self):
        self.predictor.print_model()

    def plot(self, plotter):
        plotter().plot(self)

    def __getattr__(self, name):
        # TODO: this is just a demonstration of an idea
        def method(*args, **kwargs):
            m = getattr(self.dataset, name)
            return m(*args, **kwargs)
        return method
