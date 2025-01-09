def test_guake_installed(host):
  guake = host.package("guake")
  assert guake.is_installed
