def test_java_installed(host):
  java = host.package("temurin-21-jdk")
  assert java.is_installed

def test_maven_installed(host):
  maven = host.package("maven")
  assert maven.is_installed
