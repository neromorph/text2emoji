variable "project_id" {
  description = "The GCP project ID"
  type        = string
  default     = "iykra-aef2"
}

variable "region" {
  description = "The GCP region"
  type        = string
  default     = "us-central1"
}

variable "zone" {
  description = "The GCP zone"
  type        = string
  default     = "us-central1-a"
}

variable "cluster_name" {
  description = "The name of the GKE cluster"
  type        = string
  default     = "iykra-cluster"
}

variable "node_count" {
  description = "Number of nodes in the GKE cluster"
  type        = number
  default     = 2
}

variable "machine_type" {
  description = "Machine type for the GKE nodes"
  type        = string
  default     = "e2-standard-2"
}

variable "artifact_repository" {
  description = "Name of the Artifact Registry repository"
  type        = string
  default     = "iykra"
}