from abc import ABC, abstractmethod

from cloud.base.Instance import Instance
from cloud.base.Network import Network


class Cloud(ABC):

    @abstractmethod
    def get_network(self) -> Network:
        pass

    @abstractmethod
    def get_instance(self) -> Instance:
        pass
