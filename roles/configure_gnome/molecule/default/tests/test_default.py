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
