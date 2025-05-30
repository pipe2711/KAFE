from abc import abstractmethod

class Gesha:
    def __init__(self):
        pass

    @abstractmethod
    def fit(self):
        raise NotImplementedError()

    @abstractmethod
    def predict(self):
        raise NotImplementedError()

    @abstractmethod
    def summary(self):
        raise NotImplementedError()

    @abstractmethod
    def evaluate(self):
        raise NotImplementedError()

    @abstractmethod
    def compile(self):
        raise NotImplementedError()
