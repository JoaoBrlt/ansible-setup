# Development

## Requirements

- [Git](https://git-scm.com/)
- [Python 3](https://www.python.org/)
- [Docker](https://docs.docker.com/engine/install/)

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

## Linting

- Lint the code:

```bash
ansible-lint
```

## Testing

- Test a role:

```bash
cd roles/...
molecule test
```

- Test the playbook:

```bash
molecule test
```
