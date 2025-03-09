from cdktf import TerraformStack
from cdktf_cdktf_provider_aws.provider import AwsProvider

from cloud.aws.AwsInstance import AwsInstance
from cloud.aws.AwsNetwork import AwsNetwork
from cloud.base.Cloud import Cloud
from cloud.base.Instance import Instance
from cloud.base.Network import Network


class AwsCloud(Cloud):

    def __init__(self, scope: TerraformStack):
        self.scope = scope
        self.provider = AwsProvider(
            scope, "aws",
            region="eu-central-1",
        )
        self.network: Network = AwsNetwork(self)
        self.instance: Instance = AwsInstance(self)

    def get_instance(self) -> Instance:
        return self.instance

    def get_network(self) -> Network:
        return self.network
