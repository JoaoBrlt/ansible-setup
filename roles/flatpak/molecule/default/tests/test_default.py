def test_flatpak_installed(host):
  flatpak = host.package("flatpak")
  assert flatpak.is_installed

def test_gnome_software_installed(host):
  gnome_software = host.package("gnome-software")
  assert gnome_software.is_installed
