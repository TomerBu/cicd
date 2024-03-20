  # selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.core.os_manager import ChromeType

def chrome():
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  return driver

def firefox():
  driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
  return driver 

def chromium():
  driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
  return driver




import time


def test_title():
  driver = chromium()
  driver.get("http://www.google.com")
  assert driver.title == "Google"
  time.sleep(5)
  driver.quit()

# remove python_demo/__pycache__/test_google.cpython-311-pytest-8.1.1.pyc from git:
# remove the entire folder python_demo/__pycache__ from git:
# git rm -r python_demo/__pycache__