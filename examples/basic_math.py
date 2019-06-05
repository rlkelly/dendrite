from context import dendrite

from dendrite import Feature, DataModel, Row
from dendrite.bigquery import BigQueryDataset


class TimesTwoFeature(Feature):
    description = "multiplies by two"

    @staticmethod
    def transform(row):
        return row['value'] * 2

class TimesThreeFeature(Feature):
    description = "multiplies by three"

    @staticmethod
    def transform(row):
        return row['value'] * 3


if __name__ == '__main__':
    model = DataModel()
    model.add_feature(TimesTwoFeature)
    model.add_feature(TimesThreeFeature)
    print(model.map_row(Row([2], ['value'])))

    dataset = [Row([2], ['value']), Row([3], ['value'])]
    print(model.map_rows(Dataset(dataset)))
    model.update_dataset(dataset, header=['value'])
    print(model.map_dataset())
