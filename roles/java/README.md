# Java

Installs the [Eclipse Temurin JDK](https://adoptium.net/temurin/) distributed by [Adoptium](https://adoptium.net/).

## Variables

| Name           | Description                   | Required | Default |
|----------------|-------------------------------|----------|---------|
| `java_version` | The major version to install. | `true`   | None    |

## Examples

```yaml
- name: Install JDK 21
  hosts: all
  roles:
    - role: java
      java_version: 21
```
