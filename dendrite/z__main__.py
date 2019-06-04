import base
import bigquery
from base import Feature, Model
from bigquery import BigQueryModel


class TimesTwoFeature(Feature):
    @staticmethod
    def generate(row):
        return row[0] * 2

class TimesThreeFeature(Feature):
    @staticmethod
    def generate(row):
        return row[0] * 3


if __name__ == '__main__':
    TimesTwoFeature
    TimesThreeFeature
    model = Model()
    model.add_feature(TimesTwoFeature)
    model.add_feature(TimesThreeFeature)
    print(model.map_row([2]))

    dataset = [[2], [3]]
    print(model.map_rows(dataset))
    model.update_dataset(dataset, header=['value'])
    print(model.map_dataset())

    b = BigQueryModel('chrome-sensor-238716', 'SELECT * FROM `OSINT.water_data` LIMIT 10')
