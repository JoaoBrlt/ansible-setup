def test_vagrant_libvirt_installed(host):
  vagrant_plugins = host.run("vagrant plugin list")
  assert vagrant_plugins.rc == 0
  assert "vagrant-libvirt" in vagrant_plugins.stdout
