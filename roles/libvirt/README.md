# Libvirt

Installs libvirt, its dependencies and tools:
- [QEMU](https://www.qemu.org/)
- [KVM](https://linux-kvm.org/)
- [libvirt](https://libvirt.org/)
- [virt-manager](https://virt-manager.org/)

## Examples

```yaml
- name: Install libvirt
  hosts: all
  roles:
    - libvirt
```
