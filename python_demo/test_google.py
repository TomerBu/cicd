# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


import time


def test_title():
  driver = webdriver.Chrome()
  driver.get("http://www.google.com")
  assert driver.title == "Google"
  time.sleep(5)
  driver.quit()

# remove python_demo/__pycache__/test_google.cpython-311-pytest-8.1.1.pyc from git:
# remove the entire folder python_demo/__pycache__ from git:
# git rm -r python_demo/__pycache__