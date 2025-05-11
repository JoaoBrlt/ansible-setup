def test_firefox_installed(host):
  firefox = host.package("firefox")
  assert firefox.is_installed
