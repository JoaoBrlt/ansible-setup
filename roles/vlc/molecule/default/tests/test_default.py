def test_vlc_installed(host):
  vlc = host.package("vlc")
  assert vlc.is_installed
