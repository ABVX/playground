variable "name" {
  default = "archiver"
}

variable "cores" {
  default = "2"
}

variable "memory" {
  default = "4"
}



resource "yandex_compute_instance" "archiver" {
  name = var.name
  resources {
    cores = var.cores
    memory = var.memory
  }
  boot_disk {
    initialize_params {
      image_id = "ubuntu"
    }
  }
}
