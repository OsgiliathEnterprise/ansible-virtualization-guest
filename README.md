Ansible virtualization Guest
=========

* Galaxy: [![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_virtualization_guest-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_virtualization_guest)
* Lint & requirements: ![Molecule](https://github.com/OsgiliathEnterprise/ansible-virtualization-guest/workflows/Molecule/badge.svg)
* Tests: [![Build Status](https://travis-ci.org/OsgiliathEnterprise/ansible-virtualization-guest.svg?branch=master)](https://travis-ci.org/OsgiliathEnterprise/ansible-virtualization-guest)
* Chat: [![Join the chat at https://gitter.im/OsgiliathEnterprise/platform](https://badges.gitter.im/OsgiliathEnterprise/platform.svg)](https://gitter.im/OsgiliathEnterprise/platform?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This role is a wrapper on top of The [StackHpc VM guest](https://github.com/stackhpc/ansible-role-libvirt-vm) role and permit to deploy a Virtual Machine on libvirt/kvm 

Requirements
------------

executing `.configure` will download requirements for the role

Role Variables
--------------

Same as the one of the [original role](https://github.com/stackhpc/ansible-role-libvirt-vm)

Also, your should reference some remotely hosted libvirt compliant boxes

```
    virtualization_guest_boxes:
      - name: fedora-31-cloud
        url: https://download.fedoraproject.org/pub/fedora/linux/releases/31/Cloud/x86_64/images/Fedora-Cloud-Base-Vagrant-31-1.9.x86_64.vagrant-libvirt.box
``` 
These boxes will be unpacked in `/var/lib/libvirt/images/{{ box.name }}.img` so that you'll be able to reference it to create your vm:

```
    libvirt_vms:
      - state: present
        name: 'fedoraGuestVM'
        memory_mb: 512
        vcpus: 1
        volumes:
          - name: 'fedora-31-cloud.img'
            type: 'file'
            device: 'cdrom'
            format: 'raw'
            target: 'hda'  # first device on ide bus
``` 

Dependencies
------------

* [StackHpc VM guest](https://github.com/stackhpc/ansible-role-libvirt-vm)


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

