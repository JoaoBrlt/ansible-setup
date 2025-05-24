def test_terraform_installed(host):
  terraform = host.package("terraform")
  assert terraform.is_installed
