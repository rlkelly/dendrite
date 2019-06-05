class Row(object):
    def __init__(self, values):
        self.values = values

    def __len__(self):
        return len(self.values)

    def __repr__(self):
        return f'Row ({self.values})'

    def __getitem__(self, item):
        if type(item) == int:
            ix = item
        else:
            raise Exception('Invalid Index')
        return self.values[ix]
