Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-18.04"
  config.vm.provider "vmware_fusion" do |v|
    v.memory = 2048
    v.cpus = 2
  config.vm.synced_folder "mgmt/", "/opt/"
  config.ssh.forward_agent = true
  end
   config.vm.provision "shell", inline: <<-SHELL
     apt-get update
     apt-get install -y software-properties-common
     apt-add-repository ppa:ansible/ansible
     apt-get update
     apt-get install -y ansible
   SHELL
   config.vm.provision "file", source: "~/.ssh/known_hosts", destination: "$HOME/.ssh/known_hosts"
end
