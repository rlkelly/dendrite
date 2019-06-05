from .row_select import RowSelect


class Dataset(object):
    def __init__(self, dataset, header=None):
        self.dataset = dataset
        if header:
            self.header = header
        else:
            self.header = [str(i) for i in range(len(self.dataset[0]))]

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
        return f'Dataset(cols: {self.header})'

    def __getitem__(self, index):
        return self.dataset[index]

    def print_rows(self):
        header = ', '.join(self.header)
        print(header)
        print('-' * len(header))
        for row in self.dataset:
            print(row)
        print()

    def to_pandas(self):
        return PandasDataset(self.dataset, columns=self.header)
