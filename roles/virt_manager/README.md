# Virtual Machine Manager

Installs [virt-manager](https://virt-manager.org/).

## Dependencies

- [libvirt](https://libvirt.org/)

## Examples

```yaml
- name: Install Virtual Machine Manager
  hosts: all
  roles:
    - virt_manager
```
