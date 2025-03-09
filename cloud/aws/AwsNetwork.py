from cdktf import TerraformHclModule, Fn

from cloud.aws import AwsCloud
from cloud.base.Network import Network, VpcDto


class AwsNetwork(Network):

    def __init__(self, cloud: AwsCloud):
        self.vpc_module = None
        self.cloud = cloud

    def create_vpc(self, dto: VpcDto) -> None:
        self.vpc_module = TerraformHclModule(self.cloud.scope, "Vpc",
                                             source="terraform-aws-modules/vpc/aws",
                                             variables={
                                                 "name": dto.name,
                                                 "cidr": dto.cidr,
                                                 "azs": dto.azs,
                                                 "private_subnets": dto.private_subnets,
                                                 "public_subnets": dto.public_subnets,
                                                 "enable_nat_gateway": dto.enable_nat_gateway,
                                             },
                                             providers=[self.cloud.provider]
                                             )

    def get_public_subnet(self, index: int) -> str:
        if self.vpc_module is None:
            raise Exception("vpc module not set")
        return Fn.element(self.vpc_module.get_list("public_subnets"), index)
