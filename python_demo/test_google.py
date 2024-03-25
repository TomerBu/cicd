import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_title():
  options = Options()
  options.binary_location = "/usr/bin/chromium"
  options.add_argument("--headless")

  s = Service("/usr/local/bin/chromedriver")

  driver = webdriver.Chrome(service=s, options=options)
  driver.get("http://www.google.com")
  assert driver.title == "Google"
  time.sleep(5)
  driver.quit()
