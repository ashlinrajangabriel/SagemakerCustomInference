provider "aws" {
  region = var.aws_region
}

locals {
  model_image = "${var.ecr_registry_uri}:${var.container_tag}"
}

module "endpoint" {
  source = "terraform-aws-modules/sagemaker/aws"

  name = "endpoint-name"
  model_image = local.model_image
  instance_type = "ml.t2.medium"
  initial_instance_count = 1
  autoscaling_enabled = true
  variant_a_weight = 0.5
  variant_b_weight = 0.5
  role_arn = var.role_arn
  endpoint_config_name = "endpoint-config-name"
}

variable "aws_region" {
  type = string
}

variable "ecr_registry_uri" {
  type = string
}

variable "container_tag" {
  type = string
}

variable "role_arn" {
  type = string
}