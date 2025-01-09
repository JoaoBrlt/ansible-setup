def test_gnome_tweaks_installed(host):
  gnome_tweaks = host.package("gnome-tweaks")
  assert gnome_tweaks.is_installed

def test_gnome_extension_manager_installed(host):
  gnome_shell_extension_manager = host.package("gnome-shell-extension-manager")
  assert gnome_shell_extension_manager.is_installed
