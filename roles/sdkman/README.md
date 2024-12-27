# SDKMAN

Installs [SDKMAN](https://sdkman.io/).

## Variables

| Name                   | Description                           | Required | Default |
|------------------------|---------------------------------------|----------|---------|
| `sdkman_java_versions` | The list of Java versions to install. | `false`  | `[]`    |

## Examples

```yaml
- name: Install SDKMAN
  hosts: all
  roles:
    - role: sdkman
      sdkman_java_versions:
        - { version: 17 }
        - { version: 21, default: true }
```
