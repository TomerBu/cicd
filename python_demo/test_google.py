  # selenium 4
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.core.os_manager import ChromeType

def chrome():
  options = ChromeOptions()
  options.add_argument('--headless')
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options )
  return driver

def firefox():
  driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
  return driver 

def chromium():
  options = ChromeOptions()
  options.add_argument('--headless')
  driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=options)
  return driver

import time


def test_title():
  driver = chrome()
  driver.get("http://www.google.com")
  assert driver.title == "Google"
  time.sleep(5)
  driver.quit()

# remove python_demo/__pycache__/test_google.cpython-311-pytest-8.1.1.pyc from git:
# remove the entire folder python_demo/__pycache__ from git:
# git rm -r python_demo/__pycache__