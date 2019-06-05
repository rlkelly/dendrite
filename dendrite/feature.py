from abc import ABCMeta, abstractmethod


class Feature(metaclass=ABCMeta):
    def perform_transform(self, row):
        try:
            return self.transform(row)
        except Exception as e:
            raise Exception(e)

    @staticmethod
    @abstractmethod
    def transform(row):
        pass

    def execute(self, row):
        return self.perform_transform(row)
