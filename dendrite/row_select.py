from .row import Row


class RowSelect(Row):
    def __init__(self, row, header):
        self.row = row
        self.header = header

    @property
    def values(self):
        return self.row.values

    def __getitem__(self, item):
        if type(item) == str:
            ix = self.header.index(item)
        elif type(item) == int:
            ix = item
        else:
            raise Exception('Invalid Index')
        return self.row[ix]
