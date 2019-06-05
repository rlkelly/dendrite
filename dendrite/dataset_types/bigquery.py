from google.cloud import bigquery

from ..base import DataModel, Row, Dataset


class BigQueryModel(DataModel):
    """This requires your environment variable GOOGLE_APPLICATION_CREDENTIALS to be set"""

    def __init__(self, project_id, query):
        super(BigQueryModel, self).__init__()
        self.client = bigquery.Client(project_id)
        self.update_query(query)
        self.update_dataset()

    def update_query(self, query):
        self.query = query

    def get_data(self):
        return list(self.client.query(self.query).result())

    def update_dataset(self):
        results = self.get_data()
        dataset = []
        if len(results) == 0:
            raise Exception('Query Returned No Results')
        header = list(results[0]._xxx_field_to_index.keys())
        for row in results:
            dataset.append(Row(row._xxx_values))
        self.dataset = Dataset(dataset, header)
