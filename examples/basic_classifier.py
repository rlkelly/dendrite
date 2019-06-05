from random import randint, random

from context import dendrite

from dendrite import Feature, DataModel, Dataset, Row, Target
from dendrite.converters.one_hot import OneHotEncoder
from dendrite.predictors import LogisticRegressor
from dendrite.plotters import ROCCurve
from dendrite.dataset_types import RandomDataset, RandomBinaryTarget


if __name__ == '__main__':
    dataset = RandomDataset(5, 100)
    model = DataModel(dataset)
    model.add_predictor(LogisticRegressor())
    target = RandomBinaryTarget(1, 100)
    t2 = OneHotEncoder(target)()
    model.fit(target)
    model.plot(ROCCurve)
