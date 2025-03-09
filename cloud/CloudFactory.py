import os

from cdktf import TerraformStack

from cloud.aws.AwsCloud import AwsCloud


class CloudFactory:
    @staticmethod
    def get_cloud(scope: TerraformStack):
        match os.environ['CLOUD']:
            case "aws":
                return AwsCloud(scope=scope)
            case _:
                raise NotImplementedError
