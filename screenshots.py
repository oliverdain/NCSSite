from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {'os': 'Windows', 'os_version': 'xp',
    'browser': 'IE', 'browser_version': '6.0',
    'browserstack.local': True}

driver = webdriver.Remote(
    command_executor='http://OliverD1:81a6QnV3XQZsc95aBXwo@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)

driver.get("http://localhost:8080")
print driver.title
driver.save_screenshot('ie6.png')
driver.quit()
