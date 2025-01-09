def test_discord_installed(host):
  app_id = "com.discordapp.Discord"
  result = host.run("flatpak list --app --columns=application")
  assert result.rc == 0
  assert app_id in result.stdout.splitlines()
