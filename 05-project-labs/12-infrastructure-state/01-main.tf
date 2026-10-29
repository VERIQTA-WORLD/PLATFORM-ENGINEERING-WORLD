terraform {
  required_version = ">= 1.6.0, < 2.0.0"
}

variable "replicas" {
  type    = number
  default = 2
  validation {
    condition     = var.replicas >= 1 && var.replicas <= 4 && floor(var.replicas) == var.replicas
    error_message = "replicas must be an integer from 1 to 4."
  }
}

resource "terraform_data" "service_contract" {
  input = {
    name     = "checkout"
    owner    = "commerce"
    replicas = var.replicas
  }
}

output "service_contract" {
  value = terraform_data.service_contract.output
}
