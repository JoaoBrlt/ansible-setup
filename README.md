# Ansible Setup

## Requirements

- [Python 3](https://www.python.org/)
- [Pip 3](https://pypi.org/project/pip/)

## Install

- Create a virtual environment:

```bash
python -m venv venv
```

- Activate the virtual environment:

```bash
source venv/bin/activate
```

- Install the dependencies:

```bash
pip install -r requirements.txt
```

## Lint

- Lint the YAML files:

```bash
yamllint .
```

- Lint the Ansible files:

```bash
ansible-lint
```

## Run

- Run the playbook:

```bash
ansible-playbook main.yml
```

## Test

- Test the playbook:

```bash
molecule test
```
