def test_solaar_installed(host):
  solaar = host.package("solaar")
  assert solaar.is_installed
