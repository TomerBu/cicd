from selenium import webdriver
import time

def test_title():
  driver = webdriver.Chrome()
  driver.get("http://www.google.com")
  assert driver.title == "Google"
  time.sleep(5)
  driver.quit()
