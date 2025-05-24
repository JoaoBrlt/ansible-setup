def test_packer_installed(host):
  packer = host.package("packer")
  assert packer.is_installed
