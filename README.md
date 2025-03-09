Work order:
1) execute the command `CLOUD="aws" cdktf synth --hcl`, which will generate Terraform configuration for AWS (in this case)
2) `tofu apply` to apply the configuration

Structure:
1) `main.py` - entrypoint
2) `cloud` - package with classes to describe cloud infrastructure
3) `cloud/base` - abstraction model
4) `cloud/aws` - AWS implementation

Generated Terraform code: `cdk.tf` (not beautiful, but it works)