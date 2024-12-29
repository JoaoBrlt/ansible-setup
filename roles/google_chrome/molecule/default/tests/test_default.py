def test_google_chrome_installed(host):
  google_chrome = host.package("google-chrome-stable")
  assert google_chrome.is_installed
