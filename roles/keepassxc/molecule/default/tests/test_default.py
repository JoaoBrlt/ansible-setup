def test_keepassxc_installed(host):
  keepassxc = host.package("keepassxc")
  assert keepassxc.is_installed
