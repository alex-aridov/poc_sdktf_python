from abc import ABC, abstractmethod
from typing import List

from pydantic import BaseModel


class InstancesDto(BaseModel):
    instances: List[str]
    name: str
    instance_type: str
    subnet_id: str


class Instance(ABC):

    @abstractmethod
    def create_instances(self, dto: InstancesDto) -> None:
        pass
