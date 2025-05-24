# Libvirt

Installs [QEMU](https://www.qemu.org/), [KVM](https://linux-kvm.org/) and [libvirt](https://libvirt.org/).

## Examples

```yaml
- name: Install libvirt
  hosts: all
  roles:
    - libvirt
```
