def test_ubuntu_report_uninstalled(host):
  ubuntu_report = host.package("ubuntu-report")
  assert not ubuntu_report.is_installed

def test_apport_uninstalled(host):
  apport = host.package("apport")
  assert not apport.is_installed

def test_whoopsie_uninstalled(host):
  whoopsie = host.package("whoopsie")
  assert not whoopsie.is_installed

def test_update_notifier_uninstalled(host):
  update_notifier = host.package("update-notifier")
  assert not update_notifier.is_installed

def test_snapd_uninstalled(host):
  snapd = host.package("snapd")
  assert not snapd.is_installed

def test_ubuntu_session_uninstalled(host):
  ubuntu_session = host.package("ubuntu-session")
  assert not ubuntu_session.is_installed

def test_gnome_session_installed(host):
  gnome_session = host.package("gnome-session")
  assert gnome_session.is_installed

def test_flatpak_installed(host):
  flatpak = host.package("flatpak")
  assert flatpak.is_installed

def test_gnome_tweaks_installed(host):
  gnome_tweaks = host.package("gnome-tweaks")
  assert gnome_tweaks.is_installed

def test_gnome_extension_manager_installed(host):
  gnome_shell_extension_manager = host.package("gnome-shell-extension-manager")
  assert gnome_shell_extension_manager.is_installed

def test_gnome_software_installed(host):
  gnome_software = host.package("gnome-software")
  assert gnome_software.is_installed

def test_gnome_software_plugin_flatpak_installed(host):
  gnome_software_plugin_flatpak = host.package("gnome-software-plugin-flatpak")
  assert gnome_software_plugin_flatpak.is_installed

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

def test_guake_installed(host):
  guake = host.package("guake")
  assert guake.is_installed

def test_libvirt_daemon_system_installed(host):
  libvirt_daemon_system = host.package("libvirt-daemon-system")
  assert libvirt_daemon_system.is_installed

def test_virt_manager_installed(host):
  virt_manager = host.package("virt-manager")
  assert virt_manager.is_installed

def test_sdkman_installed(host):
  env_vars = host.environment()
  install_dir = host.file(env_vars["HOME"] + "/.sdkman")
  assert install_dir.exists
  assert install_dir.is_directory

def test_maven_installed(host):
  maven = host.package("maven")
  assert maven.is_installed

def test_nvm_installed(host):
  env_vars = host.environment()
  install_dir = host.file(env_vars["HOME"] + "/.nvm")
  assert install_dir.exists
  assert install_dir.is_directory

def test_docker_installed(host):
  docker = host.package("docker-ce")
  assert docker.is_installed

def test_vagrant_installed(host):
  vagrant = host.package("vagrant")
  assert vagrant.is_installed

def test_vagrant_libvirt_installed(host):
  vagrant_plugins = host.run("vagrant plugin list")
  assert vagrant_plugins.rc == 0
  assert "vagrant-libvirt" in vagrant_plugins.stdout

def test_jetbrains_toolbox_installed(host):
  env_vars = host.environment()
  install_dir = host.file(env_vars["HOME"] + "/.local/share/JetBrains/Toolbox")
  assert install_dir.exists
  assert install_dir.is_directory

def test_gitkraken_installed(host):
  app_id = "com.axosoft.GitKraken"
  result = host.run("flatpak list --app --columns=application")
  assert result.rc == 0
  assert app_id in result.stdout.splitlines()

def test_postman_installed(host):
  app_id = "com.getpostman.Postman"
  result = host.run("flatpak list --app --columns=application")
  assert result.rc == 0
  assert app_id in result.stdout.splitlines()

def test_google_chrome_installed(host):
  google_chrome = host.package("google-chrome-stable")
  assert google_chrome.is_installed

def test_firefox_installed(host):
  firefox = host.package("firefox")
  assert firefox.is_installed

def test_keepassxc_installed(host):
  keepassxc = host.package("keepassxc")
  assert keepassxc.is_installed

def test_solaar_installed(host):
  solaar = host.package("solaar")
  assert solaar.is_installed

def test_vlc_installed(host):
  vlc = host.package("vlc")
  assert vlc.is_installed

def test_pinta_installed(host):
  app_id = "com.github.PintaProject.Pinta"
  result = host.run("flatpak list --app --columns=application")
  assert result.rc == 0
  assert app_id in result.stdout.splitlines()

def test_color_picker_installed(host):
  app_id = "nl.hjdskes.gcolor3"
  result = host.run("flatpak list --app --columns=application")
  assert result.rc == 0
  assert app_id in result.stdout.splitlines()

def test_signal_installed(host):
  signal = host.package("signal-desktop")
  assert signal.is_installed

def test_slack_installed(host):
  app_id = "com.slack.Slack"
  result = host.run("flatpak list --app --columns=application")
  assert result.rc == 0
  assert app_id in result.stdout.splitlines()

def test_discord_installed(host):
  app_id = "com.discordapp.Discord"
  result = host.run("flatpak list --app --columns=application")
  assert result.rc == 0
  assert app_id in result.stdout.splitlines()
