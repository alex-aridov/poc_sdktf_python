from abc import ABC, abstractmethod

from pydantic import BaseModel
from typing import List

class VpcDto(BaseModel):
    name: str
    cidr: str
    azs: List[str]
    private_subnets: List[str]
    public_subnets: List[str]
    enable_nat_gateway: bool

class Network(ABC):

    @abstractmethod
    def create_vpc(self, dto: VpcDto) -> None:
        pass

    @abstractmethod
    def get_public_subnet(self, index: int) -> str:
        pass