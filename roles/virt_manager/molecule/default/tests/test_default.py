def test_virt_manager_installed(host):
  virt_manager = host.package("virt-manager")
  assert virt_manager.is_installed
