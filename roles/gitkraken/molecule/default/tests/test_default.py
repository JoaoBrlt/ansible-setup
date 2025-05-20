def test_gitkraken_installed(host):
  app_id = "com.axosoft.GitKraken"
  result = host.run("flatpak list --app --columns=application")
  assert result.rc == 0
  assert app_id in result.stdout.splitlines()
