def test_maven_installed(host):
  maven = host.package("maven")
  assert maven.is_installed
