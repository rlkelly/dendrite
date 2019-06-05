from random import randint, random

from ..base import Row, Dataset


class RandomDataset(Dataset):
    def __init__(self, width, depth, max_val=10):
        dataset = [[randint(0, max_val) for _ in range(width)] for _ in range(depth)]
        super(RandomDataset, self).__init__(dataset)

class RandomTarget(Dataset):
    def __init__(self, width, depth, max_val=10):
        dataset = [[randint(0, max_val) for _ in range(width)] for _ in range(depth)]
        super(RandomTarget, self).__init__(dataset)

class RandomBinaryTarget(Dataset):
    def __init__(self, width, depth, freq=0.5):
        dataset = [[random() > freq for _ in range(width)] for _ in range(depth)]
        super(RandomBinaryTarget, self).__init__(dataset)
