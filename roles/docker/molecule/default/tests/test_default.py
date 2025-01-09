def test_docker_installed(host):
  docker = host.package("docker-ce")
  assert docker.is_installed
