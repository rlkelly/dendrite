from context import dendrite

from dendrite.base import Feature
from dendrite.bigquery import BigQueryModel


class IsMajorViolation(Feature):
    @staticmethod
    def generate(row):
        return row['Is_Major_Violation'] != '-'


class IsNitrateViolation(Feature):
    @staticmethod
    def generate(row):
        return row['Contaminant_Name'] == 'Nitrate'


if __name__ == '__main__':
    b = BigQueryModel(
        'chrome-sensor-238716',
        'SELECT * FROM `OSINT.water_data` LIMIT 10',
    )
    b.add_feature(IsMajorViolation)
    b.add_feature(IsNitrateViolation)
    print(b.map_dataset())
