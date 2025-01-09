def test_signal_installed(host):
  signal = host.package("signal-desktop")
  assert signal.is_installed
