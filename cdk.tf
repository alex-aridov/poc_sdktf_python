terraform {
  required_providers {
    aws = {
      version = "5.90.0"
      source  = "aws"
    }
  }
  backend "local" {
    path = "/home/aleksandr/Developer/pocPythonTf/terraform.pocPythonTf.tfstate"
  }


}

provider "aws" {
  region = "eu-central-1"
}
module "Vpc" {
  name = "my-vpc"
  cidr = "10.0.0.0/16"
  azs = [
    "eu-central-1a",
    "eu-central-1b",
    "eu-central-1c",
  ]
  private_subnets = [
    "10.0.1.0/24",
    "10.0.2.0/24",
    "10.0.3.0/24",
  ]
  public_subnets = [
    "10.0.101.0/24",
    "10.0.102.0/24",
    "10.0.103.0/24",
  ]
  enable_nat_gateway = true
  source             = "terraform-aws-modules/vpc/aws"
  providers = {
    aws = "aws"
  }
}
module "ec2_instance" {
  name          = "instance-${each.key}"
  instance_type = "t2.micro"
  subnet_id     = "${element(module.Vpc.public_subnets, 0)}"
  source        = "terraform-aws-modules/ec2-instance/aws"
  for_each      = "${toset(["one", "two"])}"
}