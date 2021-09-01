terraform {
  required_providers {
    virtualbox = {
      source  = "terra-farm/virtualbox"
      version = "0.2.1-alpha.1"
    }
  }
}

# https://registry.terraform.io/providers/terra-farm/virtualbox/latest/docs/resources/vm
resource "virtualbox_vm" "node" {
  count     = 2
  name      = format("node-%02d", count.index + 1)
  image     = "https://app.vagrantup.com/ubuntu/boxes/bionic64/versions/20180903.0.0/providers/virtualbox.box"
  cpus      = 2
  memory    = "512 mib"
  user_data = file("${path.module}/user_data")

  network_adapter {
    type           = "hostonly"
    host_interface = "vboxnet1"
  }
}