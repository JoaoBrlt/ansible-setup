# Ansible Setup

This repository contains the scripts to set up my personal workstation.

## Supported distributions

- [Ubuntu 24.04](https://ubuntu.com)

## Requirements

- [Git](https://git-scm.com/)
- [Python 3](https://www.python.org/)

## Installation

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

## Usage

- Run the playbook:

```bash
ansible-playbook main.yml --ask-become-pass
```

## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details.
