from context import dendrite

from dendrite import Feature, DataModel, Dataset, Row, Target
from dendrite.predictors.linear_regressor import LinearRegressor

if __name__ == '__main__':
    # x1 * 3 + x2 * 2 + 5
    dataset = Dataset([Row([2, 3]), Row([5, 2])])
    target = Dataset([Row([17]), Row([24])])
    d = Dataset(dataset)
    model = DataModel(d)
    model.print_rows()
    lr = LinearRegressor()

    model.add_predictor(lr)
    model.fit(target)

    test = Dataset([Row([8, 3]), Row([2, 5])])
    print(model.predict(test))
