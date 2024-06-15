Code_Kaizen.Kitsune Run Role
========================

A brief description of the role goes here.

Requirements
------------

This role requires the `community.crypto` collection to be installed. You can install it by running the following command:

```bash
ansible-galaxy collection install community.crypto
```

Role Variables
--------------

The role expects the following variables to be set:

- `kitsune_ssh_key_install_from_privatekey_privatekey_src`: The path to the private key file.

The following variables are optional:

- `kitsune_ssh_key_install_from_privatekey_privatekey_mode`: The mode of the private key file to use when copying. Default is `0600`.
- `kitsune_ssh_key_install_from_privatekey_privatekey_remote_src`: A boolean flag to indicate if the private key file is already present on the target. Default is `false`.
- `kitsune_ssh_key_install_from_privatekey_regenerate`: An enumerated value to indicate if the private key should be regenerated. See [community.crypto.openssh_keypair](https://docs.ansible.com/ansible/latest/collections/community/crypto/openssh_keypair_module.html). Default is `never`.
- `kitsune_ssh_key_install_from_privatekey_keypair_mode`: The final mode of both keys (private/public) after copy. See [community.crypto.openssh_keypair](https://docs.ansible.com/ansible/latest/collections/community/crypto/openssh_keypair_module.html). Default is `0644`.
- `kitsune_ssh_key_install_from_privatekey_keypair_owner`: The final owner of both keys (private/public) after copy. Default is `ansible_user`.
- `kitsune_ssh_key_install_from_privatekey_keypair_group`: The final group of both keys (private/public) after copy. Default is `ansible_user`.

Example Playbook
----------------

Copy private ssh keys from the control node to the target node and install them under the user home directory:

```yaml
- name: Install private keys from control node to remote nodes
  hosts: target_hosts
  tasks:
    - name: Loop over ssh_keys_paths and include the role
      include_role:
        name: code_kaizen.kitsune.ssh_key_install_from_privatekey
      with_fileglob:
        - "ssh_keys/*"
      vars:
        kitsune_ssh_key_install_from_privatekey_privatekey_src: "{{ item }}"
```

Another way to consume this role would be to pre-copy or mount the private ssh keys to the target node and use this role to install them under the user home directory:

```yaml
---
- name: Install private keys that already live on remote targets
  hosts: target_hosts
  tasks:
    - name: Get private ssh keys that live on remote target
      find:
        paths: "{{ ansible_env.HOME }}/mounted_ssh_keys_dir"
      register: ssh_keys
    - name: Loop over ssh_keys and include the role to install them under the user home directory
      include_role:
        name: code_kaizen.kitsune.ssh_key_install_from_privatekey
      with_items: "{{ ssh_keys.files }}"
      vars:
        kitsune_ssh_key_install_from_privatekey_privatekey_remote_src: true
        kitsune_ssh_key_install_from_privatekey_privatekey_src: "{{ item.path }}"

```

Another way to consume this role would be to run it against localhost to install private ssh keys that live on the control node under the user home directory:

```yaml
---
- name: Install private keys that live on local target
  hosts: localhost
  connection: local
  tasks:
    - name: Get private ssh keys that live on local target
      find:
        paths: "{{ ansible_env.HOME }}/mounted_ssh_keys_dir"
      register: ssh_keys
    - name: Loop over ssh_keys and include the role to install them under the user home directory
      include_role:
        name: code_kaizen.kitsune.ssh_key_install_from_privatekey
      with_items: "{{ ssh_keys.files }}"
      vars:
        kitsune_ssh_key_install_from_privatekey_privatekey_src: "{{ item.path }}"
```


License
-------

GNU General Public License v3.0 or later

Author Information
------------------

andrewjamesdawes@gmail.com
