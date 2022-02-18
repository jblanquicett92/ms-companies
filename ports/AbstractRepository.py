import abc
import layers.domain.model as model

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, model: model):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference):
        raise NotImplementedError

    @abc.abstractmethod
    def list(self):
        raise NotImplementedError

#van todas las funciones abstractas del repositorio CRUD