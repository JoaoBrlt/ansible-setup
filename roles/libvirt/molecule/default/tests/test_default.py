def test_libvirt_daemon_system_installed(host):
  libvirt_daemon_system = host.package("libvirt-daemon-system")
  assert libvirt_daemon_system.is_installed

def test_virt_manager_installed(host):
  virt_manager = host.package("virt-manager")
  assert virt_manager.is_installed
