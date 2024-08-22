terraform {
  backend "remote" {
    organization = "NoteGenius"
    workspaces {
      name = var.workspace_name
    }
  }
}

variable "workspace_name" {
  description = "The name of the Terraform Cloud workspace to use"
  type        = string
}