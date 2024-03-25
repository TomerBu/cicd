import time
from selenium import webdriver

def test_title():
  # headless mode
  options = webdriver.ChromeOptions()
  options.add_argument("--headless")
  driver = webdriver.Chrome(options=options)
  driver.get("http://www.google.com")
  assert driver.title == "Google"
  time.sleep(5)
  driver.quit()
