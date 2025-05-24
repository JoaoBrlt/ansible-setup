# Vagrant Libvirt Plugin

Installs the [vagrant-libvirt](https://vagrant-libvirt.github.io/vagrant-libvirt/) plugin.

## Dependencies

- [libvirt](https://libvirt.org/)
- [Vagrant](https://developer.hashicorp.com/vagrant)

## Examples

```yaml
- name: Install the Vagrant Libvirt Plugin
  hosts: all
  roles:
    - vagrant_libvirt
```
