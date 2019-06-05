import pandas as pd

from .row_select import RowSelect


class Dataset(object):
    def __init__(self, dataset, header, primary_key=None):
        self.dataset = dataset
        self.header = header
        self.primary_key = primary_key

    def __len__(self):
        return len(self.dataset)

    def __iter__(self):
        self.ix = 0
        return self

    def __next__(self):
        if self.ix >= len(self.dataset):
            raise StopIteration
        res = self.dataset[self.ix]
        self.ix += 1
        return RowSelect(res, self.header)

    def __repr__(self):
        string_header = ', '.join(self.header)
        return f'Dataset({string_header})'

    def __getitem__(self, index):
        return self.dataset[index]

    def print_rows(self):
        for row in self.dataset:
            print(row)

    def to_pandas(self):
        return PandasDataset(self.dataset, columns=self.header)


class PandasDataset(Dataset):
    def __init__(self, dataset, header):
        self.dataset = pd.DataFrame(dataset, columns=header)

    @property
    def columns(self):
        return list(self.dataset.columns)

    @property
    def columns(self):
        return self.dataset.index.name

    def join(self, other: PandasDataset, left_index, right_index, how='inner', inplace=False):
        left = self.dataset.set_index(left_index)
        right = self.dataset.set_index(right_index)
        d = left.join(right, how=how)
        if inplace:
            self.dataset = d
        return d


def Target(Dataset):
    pass
