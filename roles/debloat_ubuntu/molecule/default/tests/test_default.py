def test_ubuntu_report_uninstalled(host):
  ubuntu_report = host.package("ubuntu-report")
  assert not ubuntu_report.is_installed

def test_apport_uninstalled(host):
  apport = host.package("apport")
  assert not apport.is_installed

def test_whoopsie_uninstalled(host):
  whoopsie = host.package("whoopsie")
  assert not whoopsie.is_installed

def test_update_notifier_uninstalled(host):
  update_notifier = host.package("update-notifier")
  assert not update_notifier.is_installed

def test_snapd_uninstalled(host):
  snapd = host.package("snapd")
  assert not snapd.is_installed

def test_ubuntu_session_uninstalled(host):
  ubuntu_session = host.package("ubuntu-session")
  assert not ubuntu_session.is_installed

def test_gnome_session_installed(host):
  gnome_session = host.package("gnome-session")
  assert gnome_session.is_installed
