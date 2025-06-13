provider "google" {
  project = var.project_id
  region  = var.region
}

terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.39.0"
    }
  }

  backend "gcs" {
    # This will be configured dynamically in GitHub Actions
  }
}