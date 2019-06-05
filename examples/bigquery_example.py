from context import dendrite

from dendrite import Feature
from dendrite.bigquery import BigQueryModel


class IsMajorViolation(Feature):
    description = "check for a major violation"

    @staticmethod
    def transform(row):
        return row['Is_Major_Violation'] != '-'


class IsNitrateViolation(Feature):
    name = 'is_nitrate_violation'
    description = "checks for a nitrate violation"

    @staticmethod
    def transform(row):
        return row['Contaminant_Name'] == 'Nitrate'


if __name__ == '__main__':
    b = BigQueryModel(
        'chrome-sensor-238716',
        'SELECT * FROM `OSINT.water_data` LIMIT 10',
    )
    b.add_features(IsMajorViolation, IsNitrateViolation)
    print(b.map_dataset())
