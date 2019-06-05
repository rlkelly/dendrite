from .row_select import RowSelect


class Dataset(object):
    def __init__(self, dataset, primary_key, header):
        self.dataset = dataset
        self.primary_key = primary_key
        self.header = header

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
