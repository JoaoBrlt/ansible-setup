def test_flatpak_installed(host):
  flatpak = host.package("flatpak")
  assert flatpak.is_installed
