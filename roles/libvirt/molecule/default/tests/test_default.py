def test_libvirt_daemon_system_installed(host):
  libvirt_daemon_system = host.package("libvirt-daemon-system")
  assert libvirt_daemon_system.is_installed
