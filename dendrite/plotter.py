from abc import ABCMeta, abstractmethod


class Plotter(metaclass=ABCMeta):
    @abstractmethod
    def calc(self, parent, **kwargs):
        pass

    @abstractmethod
    def plot(self, parent, **kwargs):
        pass
