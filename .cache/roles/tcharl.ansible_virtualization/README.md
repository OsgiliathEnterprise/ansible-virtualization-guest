Virtualization
=========


* Galaxy: [![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_virtualization-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_virtualization)
* Lint & requirements: ![Molecule](https://github.com/OsgiliathEnterprise/ansible-virtualization/workflows/Molecule/badge.svg)
* Tests: [![Build Status](https://travis-ci.org/OsgiliathEnterprise/ansible-virtualization.svg?branch=master)](https://travis-ci.org/OsgiliathEnterprise/ansible-virtualization)
* Chat: [![Join the chat at https://gitter.im/OsgiliathEnterprise/platform](https://badges.gitter.im/OsgiliathEnterprise/platform.svg)](https://gitter.im/OsgiliathEnterprise/platform?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


Configure virtualization on the host.
It's a simple wrapper over the community-provided [libvirt role](https://github.com/stackhpc/ansible-role-libvirt-host)

Requirements
------------

executing `.configure` will download requirements for the role

Role Variables
--------------

Same as the one of the [original role](https://github.com/stackhpc/ansible-role-libvirt-host)

Dependencies
------------

The [original role](https://github.com/stackhpc/ansible-role-libvirt-host) Thanks stack HPC as well as the [LVM one](https://github.com/OsgiliathEnterprise/ansible-volumes)  

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

[Apache-2](https://www.apache.org/licenses/LICENSE-2.0)

Author Information
------------------

* Twitter [@tcharl](https://twitter.com/Tcharl)
* Github [@tcharl](https://github.com/Tcharl)
* LinkedIn [Charlie Mordant](https://www.linkedin.com/in/charlie-mordant-51796a97/)
