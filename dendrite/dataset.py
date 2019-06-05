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

    def print_rows(self):
        for row in self.dataset:
            print(row)

    def __repr__(self):
        string_header = ', '.join(self.header)
        return f'Dataset({string_header})'

    def __getitem__(self, index):
        return self.dataset[index]


def Target(Dataset):
    pass
