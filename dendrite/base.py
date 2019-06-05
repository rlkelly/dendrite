from abc import ABCMeta, abstractmethod
from typing import List

from .dataset import Dataset
from .feature import Feature
from .row import Row
from .row_select import RowSelect


class DataModel(metaclass=ABCMeta):
    def __init__(self, dataset=None, index=None):
        self.dataset = dataset
        self.features = []
        self.index = index

    @property
    def header(self):
        return self.dataset.header

    def get_new_header(self):
        return [feature.name for feature in self.features]

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
            self.features.append(feature())

    def map_row(self, row: Row):
        output = []
        for feature in self.features:
            output.append(feature.execute(row))
        return Row(output)

    def map_rows(self, rows: List[Row]):
        output = []
        for row in rows:
            output.append(Row(self.map_row(row)))
        return output

    def map_dataset(self):
        return Dataset(self.map_rows(self.dataset), self.get_new_header())

    def __getitem__(self, index: int):
        return RowSelect(self.dataset[index], self.header)
