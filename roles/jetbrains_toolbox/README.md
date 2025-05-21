# JetBrains Toolbox

Installs [JetBrains Toolbox](https://www.jetbrains.com/toolbox-app/).

## Variables

| Name                        | Description                                                                                    | Required | Default  |
|-----------------------------|------------------------------------------------------------------------------------------------|----------|----------|
| `jetbrains_toolbox_version` | The version of JetBrains Toolbox to install. It can be `latest` to install the latest version. | `false`  | `latest` |

## Examples

```yaml
- name: Install JetBrains Toolbox (latest version)
  hosts: all
  roles:
    - jetbrains_toolbox
```

```yaml
- name: Install JetBrains Toolbox (latest version)
  hosts: all
  roles:
    - role: jetbrains_toolbox
      jetbrains_toolbox_version: latest
```

```yaml
- name: Install JetBrains Toolbox (specific version)
  hosts: all
  roles:
    - role: jetbrains_toolbox
      jetbrains_toolbox_version: 2.6.0
```
