def test_zsh_installed(host):
  zsh = host.package("zsh")
  assert zsh.is_installed

def test_zsh_default_shell(host):
  variables = host.ansible.get_variables()
  user = variables.get("ansible_user", "root")
  default_shell = host.run("getent passwd " + user + " | cut -d : -f 7")
  assert default_shell.rc == 0
  assert default_shell.stdout.strip() == "/bin/zsh"

def test_oh_my_zsh_installed(host):
  env_vars = host.environment()
  install_dir = host.file(env_vars["HOME"] + "/.oh-my-zsh")
  assert install_dir.exists
  assert install_dir.is_directory

def test_oh_my_zsh_zsh_autosuggestions_installed(host):
  env_vars = host.environment()
  plugin_dir = host.file(env_vars["HOME"] + "/.oh-my-zsh/custom/plugins/zsh-autosuggestions")
  assert plugin_dir.exists
  assert plugin_dir.is_directory

def test_oh_my_zsh_zsh_syntax_highlighting_installed(host):
  env_vars = host.environment()
  plugin_dir = host.file(env_vars["HOME"] + "/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting")
  assert plugin_dir.exists
  assert plugin_dir.is_directory

def test_powerlevel10k_installed(host):
  env_vars = host.environment()
  theme_dir = host.file(env_vars["HOME"] + "/.oh-my-zsh/custom/themes/powerlevel10k")
  assert theme_dir.exists
  assert theme_dir.is_directory

def test_powerlevel10k_configured(host):
  env_vars = host.environment()
  config_file = host.file(env_vars["HOME"] + "/.p10k.zsh")
  assert config_file.exists
  assert config_file.is_file

def test_sdkman_installed(host):
  env_vars = host.environment()
  install_dir = host.file(env_vars["HOME"] + "/.sdkman")
  assert install_dir.exists
  assert install_dir.is_directory

def test_maven_installed(host):
  maven = host.package("maven")
  assert maven.is_installed
