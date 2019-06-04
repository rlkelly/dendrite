from google.cloud import bigquery

from dendrite.base import Model, Row


class BigQueryModel(Model):
    """This requires your environment variable GOOGLE_APPLICATION_CREDENTIALS to be set"""

    def __init__(self, project_id, query):
        super(Model, self).__init__()
        self.features = []
        self.client = bigquery.Client(project_id)
        self.update_query(query)
        self.update_dataset()

    def update_query(self, query):
        self.query = query

    def update_dataset(self):
        results = list(self.client.query(self.query).result())
        self.dataset = []
        if len(results) > 0:
            self.header = list(results[0]._xxx_field_to_index.keys())
            for row in results:
                self.dataset.append(Row(row._xxx_values, self.header))
        return len(self.dataset)
