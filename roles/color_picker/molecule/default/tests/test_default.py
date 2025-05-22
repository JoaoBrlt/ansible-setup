def test_color_picker_installed(host):
  app_id = "nl.hjdskes.gcolor3"
  result = host.run("flatpak list --app --columns=application")
  assert result.rc == 0
  assert app_id in result.stdout.splitlines()
