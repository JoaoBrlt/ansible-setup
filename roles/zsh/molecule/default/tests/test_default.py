def test_zsh_installed(host):
  zsh = host.package("zsh")
  assert zsh.is_installed

def test_zsh_default_shell(host):
  variables = host.ansible.get_variables()
  user = variables.get("ansible_user", "root")
  default_shell = host.run("getent passwd " + user + " | cut -d : -f 7")
  assert default_shell.rc == 0
  assert default_shell.stdout.strip() == "/bin/zsh"
