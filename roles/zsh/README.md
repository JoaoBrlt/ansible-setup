# Zsh

Installs [Zsh](https://www.zsh.org/).

## Variables

| Name                | Description                              | Required | Default |
|---------------------|------------------------------------------|----------|---------|
| `zsh_default_shell` | Whether to set Zsh as the default shell. | `false`  | `false` |

## Examples

```yaml
- name: Install Zsh
  hosts: all
  roles:
    - role: zsh
      zsh_default_shell: true
```
