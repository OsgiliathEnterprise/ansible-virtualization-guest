Ansible virtualization Guest
=========

* Galaxy: [![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_virtualization_guest-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_virtualization_guest)
* Lint & requirements: ![Molecule](https://github.com/OsgiliathEnterprise/ansible-virtualization-guest/workflows/Molecule/badge.svg)
* Tests: [![Build Status](https://travis-ci.com/OsgiliathEnterprise/ansible-virtualization-guest.svg?branch=master)](https://travis-ci.com/OsgiliathEnterprise/ansible-virtualization-guest)
* Chat: [![Join the chat at https://gitter.im/OsgiliathEnterprise/platform](https://badges.gitter.im/OsgiliathEnterprise/platform.svg)](https://gitter.im/OsgiliathEnterprise/platform?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This role is a wrapper on top of The [StackHpc VM guest](https://github.com/stackhpc/ansible-role-libvirt-vm) role and permit to deploy a Virtual Machine on libvirt/kvm.
The cool thing with this role is that you can grab any box you want from vagrant cloud: it will download it, start it with libvirt/kvm, override the `vagrant` default user and it's ssh key by the one of the user executing to the role on the guest.
It will copy its ssh key and add it to sudoers/nologin.
Finally, it will configure firewalld on the host to let you have access to the guest machine

Requirements
------------

tox -e pipdep and check [pip requirements] (./requirements.txt) or [pip dev requirements] (./requirements-dev.txt)

Role Variables
--------------

Same as the one of the [original role](https://github.com/stackhpc/ansible-role-libvirt-vm)

Also, your should reference some remotely hosted libvirt compliant boxes

```
    virtualization_guest_boxes:
      - name: fedoraGuestVM
        url: https://download.fedoraproject.org/pub/fedora/linux/releases/33/Cloud/x86_64/images/Fedora-Cloud-Base-Vagrant-33-1.2.x86_64.vagrant-libvirt.box
        memory_mb: 2048
        vcpus: 1
        recreate_machine: true # mandatory should recreate or not?
        ssh_port_on_host: 6752 # port configured as NATTED on the host (port 6752 on the host will be redirected to port 22 on the guest)
        vm_ssh_key_url: # URL of the key insecure packer key to download
        ansible_groups:
          - directory
          - openid
        size: 3GB # Optionnal
        interfaces:
          - network: default
      - name: fedoraGuestVM2
        url: https://download.fedoraproject.org/pub/fedora/linux/releases/33/Cloud/x86_64/images/Fedora-Cloud-Base-Vagrant-33-1.2.x86_64.vagrant-libvirt.box
        memory_mb: 2048
        vcpus: 1
        recreate_machine: true # mandatory should recreate or not?
        vm_ssh_key_url: # URL of the key insecure packer key to download
        size: 3GB # Optionnal
        interfaces:
          - type: bridge
            source:
              dev: eth0

``` 
More information on the according variables in [molecule test](./molecule/default/converge.yml) and [defaults variables](./defaults/main.yml)

These boxes will be unpacked in `/var/lib/libvirt/images/{{ box.name }}.img` so that you'll be able to reference it to create your vm

## Known strange behaviours
 - This role won't recreate vm that are not taggued by `recreate_machine: true` even if they are marked as undefine in virsh. It will persist the list of created VM in a persistent fact that you should edit/remove `/etc/ansible/facts.d/ansible_virtualization_guest.fact`.

Dependencies
------------

See: [requirements collection](./requirements-collections.yml) and [requirements standalone](./requirements-standalone.yml)

Example Playbook
----------------

* See [StackHpc VM guest](https://github.com/stackhpc/ansible-role-libvirt-vm)

License
-------

[Apache-2](https://www.apache.org/licenses/LICENSE-2.0)

Author Information
------------------

* Twitter [@tcharl](https://twitter.com/Tcharl)
* Github [@tcharl](https://github.com/Tcharl)
* LinkedIn [Charlie Mordant](https://www.linkedin.com/in/charlie-mordant-51796a97/)

