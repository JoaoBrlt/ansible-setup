# Development

## Requirements

- [Git](https://git-scm.com/)
- [Python 3](https://www.python.org/)
- [QEMU](https://www.qemu.org/)
- [KVM](https://linux-kvm.org/)
- [libvirt](https://libvirt.org/)
- [Vagrant](https://www.vagrantup.com/)
- [Vagrant Libvirt Plugin](https://vagrant-libvirt.github.io/vagrant-libvirt/)

## Setup

- Clone the repository:

```bash
git clone https://github.com/JoaoBrlt/ansible-setup.git
```

- Create a virtual environment:

```bash
python3 -m venv .venv
```

- Activate the virtual environment:

```bash
source .venv/bin/activate
```

- Install the dependencies:

```bash
pip3 install -r requirements.txt
```

## Lint

- Lint the code:

```bash
ansible-lint
```

## Test

- Test a role:

```bash
cd roles/...
molecule test
```

- Test the playbook:

```bash
molecule test
```
