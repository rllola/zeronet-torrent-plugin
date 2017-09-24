# -*- mode: ruby -*-
# vi: set ft=ruby :

###############################################################################
#                                                                             #
# Vagrantfile project: Torrent plugin                                         #
# Description:                                                                #
# Will start a ubuntu 16.04 box with Zeronet install and the torrent ready    #
# for use.                                                                    #
# Author: Lola                                                                #
#                                                                             #
###############################################################################

Vagrant.require_version ">= 1.8.0"
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "ubuntu/xenial64"

  # Forwarding zeronet ports
  config.vm.network "forwarded_port", guest: 43110, host: 43110
  config.vm.network "forwarded_port", guest: 15441, host: 15441

  config.vm.provider "virtualbox" do |vb|
     vb.name = "Torrent plugin dev"
     vb.customize ["modifyvm", :id, "--memory", "2048"]
     vb.customize ["modifyvm", :id, "--nicpromisc2", "allow-all"]
  end

  config.vm.synced_folder ".", "/home/ubuntu/ZeroNet-master/plugins/Torrent"

  # Install Zeronet and load all the requirements
  config.vm.provision :shell, path: "provision.sh", privileged: false

end
