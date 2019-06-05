from random import randint, random

from context import dendrite

from dendrite import Feature, DataModel, Dataset, Row, Target
from dendrite.converters.one_hot import OneHotEncoder
from dendrite.predictors import LogisticRegressor
from dendrite.plotters import ROCCurve


if __name__ == '__main__':
    dataset = Dataset([[randint(0, 10), randint(0, 10)] for _ in range(100)])
    model = DataModel(dataset)
    model.add_predictor(LogisticRegressor())
    target = Target([[random() > 0.5] for _ in range(100)])
    # target = OneHotEncoder(target).make_dataset(target)
    model.fit(target)
    model.plot(ROCCurve)
