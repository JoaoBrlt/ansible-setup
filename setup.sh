#!/usr/bin/env bash

# Check if git is installed
if ! command -v git &> /dev/null; then
  echo "Error: git is not installed."
  exit 1
fi

# Check if python3 is installed
if ! command -v python3 &> /dev/null; then
  echo "Error: python3 is not installed."
  exit 1
fi

# Check if python3-pip is installed
if ! command -v pip3 &> /dev/null; then
  echo "Error: python3-pip is not installed."
  exit 1
fi

# Check if python3-venv is installed
if ! python3 -m venv "/tmp/check-venv" &> /dev/null; then
  echo "Error: python3-venv is not installed."
  exit 1
fi

# Clone the repository
git clone https://github.com/JoaoBrlt/ansible-setup.git

# Move to the cloned repository
cd ./ansible-setup || exit

# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install the dependencies
pip3 install -r requirements.txt

# Run the Ansible playbook
ansible-playbook main.yml --ask-become-pass
