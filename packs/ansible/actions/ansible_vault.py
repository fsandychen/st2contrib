#!/usr/bin/env python

import sys
from lib.ansible_base import AnsibleBaseRunner

__all__ = [
    'AnsibleVaultRunner'
]


class AnsibleVaultRunner(AnsibleBaseRunner):
    """
    Runs Ansible vault commands: encrypt/decrypt.
    See: https://docs.ansible.com/playbooks_vault.html
    """
    BINARY_NAME = 'ansible-vault'

if __name__ == '__main__':
    AnsibleVaultRunner(sys.argv).execute()
