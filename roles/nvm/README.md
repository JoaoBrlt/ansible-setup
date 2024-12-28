# Node Version Manager

Installs [Node Version Manager](https://github.com/nvm-sh/nvm).

## Variables

| Name                | Description                           | Required | Default |
|---------------------|---------------------------------------|----------|---------|
| `nvm_node_versions` | The list of Node versions to install. | `false`  | `[]`    |

## Examples

```yaml
- name: Install NVM
  hosts: all
  roles:
    - role: nvm
      nvm_node_versions:
        - { version: 20 }
        - { version: 22, default: true }
```
