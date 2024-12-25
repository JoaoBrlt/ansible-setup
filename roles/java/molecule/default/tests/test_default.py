def test_java_installed(host):
  java = host.package("temurin-21-jdk")
  assert java.is_installed
