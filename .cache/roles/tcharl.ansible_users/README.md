Ansible user
=========

* Galaxy: [![Ansible Galaxy](https://img.shields.io/badge/galaxy-tcharl.ansible_users-660198.svg?style=flat)](https://galaxy.ansible.com/tcharl/ansible_users)
* Lint, Tests & requirements: ![Molecule](https://github.com/OsgiliathEnterprise/ansible-users/workflows/Molecule/badge.svg)
* Chat: [![Join the chat at https://gitter.im/OsgiliathEnterprise/platform](https://badges.gitter.im/OsgiliathEnterprise/platform.svg)](https://gitter.im/OsgiliathEnterprise/platform?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

This is a wrapper role over [robertdebock.users](https://galaxy.ansible.com/robertdebock/users) in order to use it within the overall platform

Requirements
------------

Run `./configure` in order to download the role dependency. Also of course install Ansible :-).

Role Variables
--------------

Exactly the same as [robertdebock.users](https://galaxy.ansible.com/robertdebock/users): this role is forwarding the instruction.
However, to avoid conflicts, the lists has been renamed:
`local_users_user_list` and `local_users_group_list`

In addition to that roles variables, we have added the notion of system users, ex:

```yaml
    local_systemusers_user_list:
      - name: systemuser
        group: cmordante
        groups: wheel
        create_home: yes # defaults to false
        home: "/system" # defaults to "/" 
```

Also, this role manages the FreeIPA roles
```yaml
    company_domain: "osgiliath.test" # That server's hostname will be  ipa."{{ company_domain }}"
    company_realm_password: '123ADMin'
    company_ad_password: '123ADmPass'
    ipa_users_group_list:
      - name: cmordante
      - name: wheel
    ipa_users_user_list:
      - name: cmordant
        first: Charlie
        last: Mordant
        pwd: "123123123"
        update_password: on_create
        passwordexpiration: "2023-01-19 23:59:59" # Optional
        group: cmordante
        groups: wheel

```
Dependencies
------------

[robertdebock.users](https://galaxy.ansible.com/robertdebock/users)


License
-------

[Apache-2](https://www.apache.org/licenses/LICENSE-2.0)

Author Information
------------------

* Twitter [@tcharl](https://twitter.com/Tcharl)
* Github [@tcharl](https://github.com/Tcharl)
* LinkedIn [Charlie Mordant](https://www.linkedin.com/in/charlie-mordant-51796a97/)
