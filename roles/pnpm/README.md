# pnpm

Installs [pnpm](https://pnpm.io/).

## Variables

| Name                 | Description                           | Required | Default |
|----------------------|---------------------------------------|----------|---------|
| `pnpm_node_versions` | The list of Node versions to install. | `false`  | `[]`    |

## Examples

```yaml
- name: Install pnpm
  hosts: all
  roles:
    - role: pnpm
      pnpm_node_versions:
        - { version: 22 }
        - { version: 24, default: true }
```
