#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
from ansible.module_utils.basic import AnsibleModule
__metaclass__ = type

# https://blog.devops.dev/writing-ansible-modules-with-support-for-diff-mode-cae70de1c25f

DOCUMENTATION = '''
---
module: setup_ssh_keys
short_description: Install SSH keys from a folder
version_added: 0.0.1
description:
  - Installs SSH keys
attributes:
  check_mode:
    support: full
  diff_mode:
    support: full
options:
  src:
    description:
    - File path or pattern to search for SSH keys.
    details:
      - The module will search for files matching the pattern in the specified directory.
    type: str
    required: true
    version_added: "0.0.1"
  dest:
    description:
    - Destination directory to install the SSH keys.
    type: str
    required: true
    version_added: "0.0.1"
  owner:
    description:
    - User to install the SSH keys for.
    type: str
    required: true
    version_added: "0.0.1"
  group:
    description:
    - Group to install the SSH keys for.
    type: str
    required: true
    version_added: "0.0.1"
  mode:
    description:
    - Permissions to set on the SSH keys.
    type: str
    required: false
    default: "0600"
requirements:
author:
- Andrew Dawes (@andrewjdawes)
notes:
- N/A
seealso:
'''

EXAMPLES = '''
- name: Find SSH keys at /path/to/keys and install them for user 'ubuntu'
    setup_ssh_keys:
        src: /path/to/keys
        dest: /home/ubuntu/.ssh
        owner: ubuntu
        group: ubuntu
        mode: '0600'
'''

RETURN = '''
changed:
    description: Whether the SSH keys were installed.
    type: bool
    returned: always
    sample: True
files:
    description: List of SSH keys installed.
    type: list
    returned: always
    sample: ['/home/ubuntu/.ssh/id_rsa', '/home/ubuntu/.ssh/id_rsa.pub']
'''


def run_module(params: dict, check_mode: bool = False, diff_mode: bool = False):
    results = dict(
        changed=False,
        files=[],
    )
    # Proactively figure out if the results will change
    files_before = ['/path/to/keys/id_rsa', '/path/to/keys/id_rsa.pub']
    files_after = ['/path/to/keys/id_rsa', '/path/to/keys/id_rsa.pub',
                   '/path/to/keys/id_dsa', '/path/to/keys/id_dsa.pub']
    changed = files_before != files_after
    if changed:
        results['changed'] = True
        if diff_mode:
            results['diff'] = dict(
                before=files_before,
                after=files_after
            )
        if check_mode:
            return results
        else:
            # Do the thing
            pass

    return results


def main():
    module_args = dict(
        src=dict(type='str', required=True),
        dest=dict(type='str', required=True),
        owner=dict(type='str', required=True),
        group=dict(type='str', required=True),
        mode=dict(type='str', required=False, default='0600'),
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
        # required_together=[('username', 'password')],
        # required_one_of=[('username', 'access_token')],
        # mutually_exclusive=[('username', 'access_token')]
    )

    try:
        result = run_module(module.params, module.check_mode, module._diff)
        module.exit_json(**result)
    except Exception as e:
        module.fail_json(msg="Unexpected error. {0}".format(repr(e)))


if __name__ == '__main__':
    main()
