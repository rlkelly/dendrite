from context import dendrite

from dendrite import Feature, DataModel, Dataset, Row, Target
from dendrite.predictors import LinearRegressor


if __name__ == '__main__':
    # x1 * 3 + x2 * 2 + 5
    dataset = Dataset([[2, 3], [5, 2], [1, 1]])
    target = Target([[17], [24], [10]])
    d = Dataset(dataset)
    model = DataModel(d)
    model.print_rows()

    model.add_predictor(LinearRegressor())
    model.fit(target)
    test_data = Dataset([[8, 3], [2, 5]])
    test_result = Dataset([[35], [21]])
    model.predict(test_data).print_rows()
    print(model.score(test_data, test_result))
    model.print_model()
