from google.cloud import bigquery

from .base import Model, Row, Dataset


class BigQueryModel(Model):
    """This requires your environment variable GOOGLE_APPLICATION_CREDENTIALS to be set"""

    def __init__(self, project_id, query, index=None):
        super(Model, self).__init__()
        self.features = []
        self.client = bigquery.Client(project_id)
        self.index = index
        self.update_query(query)
        self.update_dataset()

    def update_query(self, query):
        self.query = query

    def update_dataset(self):
        results = list(self.client.query(self.query).result())
        dataset = []
        if len(results) > 0:
            header = list(results[0]._xxx_field_to_index.keys())
            for row in results:
                dataset.append(Row(row._xxx_values))
        self.dataset = Dataset(dataset, self.index, header)
        return len(self.dataset)
