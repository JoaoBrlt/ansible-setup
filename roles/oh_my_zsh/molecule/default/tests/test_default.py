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
