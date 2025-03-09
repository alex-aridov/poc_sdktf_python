from cdktf import TerraformHclModule, TerraformIterator

from cloud.aws import AwsCloud
from cloud.base.Instance import Instance, InstancesDto


class AwsInstance(Instance):
    def __init__(self, cloud: AwsCloud):
        self.instance = None
        self.cloud = cloud

    def create_instances(self, dto: InstancesDto) -> None:
        self.instance = TerraformHclModule(
            self.cloud.scope, "ec2_instance",
                                 source="terraform-aws-modules/ec2-instance/aws",
                                 for_each=TerraformIterator.from_list(dto.instances),
                                 variables={
                                     "name": dto.name,
                                     "instance_type": dto.instance_type,
                                     "subnet_id": dto.subnet_id})
