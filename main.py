#!/usr/bin/env python
from cdktf import App, TerraformStack
from constructs import Construct

from cloud.base.Instance import InstancesDto
from cloud.base.Network import VpcDto
from cloud.CloudFactory import CloudFactory


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        cloud = CloudFactory.get_cloud(scope=self)
        vpc_dto = VpcDto(name="my-vpc",
                     cidr="10.0.0.0/16",
                     azs=["eu-central-1a", "eu-central-1b", "eu-central-1c"],
                     private_subnets=["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"],
                     public_subnets=["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"],
                     enable_nat_gateway=True
                     )
        cloud.get_network().create_vpc(vpc_dto)

        instances_dto = InstancesDto(
            instances=["one", "two"],
            name="instance-${each.key}",
            instance_type="t2.micro",
            subnet_id=cloud.network.get_public_subnet(0)
        )
        cloud.get_instance().create_instances(instances_dto)

app = App()
MyStack(app, "pocPythonTf")

app.synth()
