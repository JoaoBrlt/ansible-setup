def test_vagrant_installed(host):
  vagrant = host.package("vagrant")
  assert vagrant.is_installed
