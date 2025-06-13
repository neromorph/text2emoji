output "kubernetes_cluster_name" {
  value       = google_container_cluster.primary.name
  description = "GKE Cluster Name"
}

output "kubernetes_cluster_location" {
  value       = google_container_cluster.primary.location
  description = "GKE Cluster Location"
}

output "artifact_registry_repository" {
  value       = "${var.region}-docker.pkg.dev/${var.project_id}/${google_artifact_registry_repository.repo.name}"
  description = "Artifact Registry Repository URL"
}

output "load_balancer_ip" {
  value       = "Access your model at: http://<EXTERNAL-IP> (available after deployment)"
  description = "Load Balancer External IP Instruction"
}