from context import dendrite

from dendrite import Feature
from dendrite.dataset_types import BigQueryDataset
from dendrite.converters.one_hot import OneHotEncoder


class IsMajorViolation(Feature):
    description = "check for a major violation"

    @staticmethod
    def transform(row):
        return row['Is_Major_Violation'] != '-'


class IsNitrateViolation(Feature):
    description = "checks for a nitrate violation"

    @staticmethod
    def transform(row):
        return row['Contaminant_Name'] == 'Nitrate'

class ViolationCode(OneHotEncoder):
    description = "one hot encoding of violation code"
    column = 'Violation_Code'


if __name__ == '__main__':
    b = BigQueryDataset(
        'chrome-sensor-238716',
        'SELECT * FROM `OSINT.water_data` ORDER BY RAND() LIMIT 10',
    )
    b.add_features(IsMajorViolation, IsNitrateViolation, ViolationCode)
    b.map_dataset(inplace=True)
    b.flatten(inplace=True)
    b.print_rows()
