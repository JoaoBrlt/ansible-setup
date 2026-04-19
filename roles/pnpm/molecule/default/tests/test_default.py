def test_pnpm_installed(host):
  env_vars = host.environment()
  install_dir = host.file(env_vars["HOME"] + "/.local/share/pnpm")
  assert install_dir.exists
  assert install_dir.is_directory
