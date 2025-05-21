def test_pinta_installed(host):
  app_id = "com.github.PintaProject.Pinta"
  result = host.run("flatpak list --app --columns=application")
  assert result.rc == 0
  assert app_id in result.stdout.splitlines()
