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
