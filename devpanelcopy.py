from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

desired_cap = {
    'platform': "Mac OS X 10.9",
    'browserName': "chrome",
    'version': "31",
}


driver = webdriver.Remote(
   command_executor='http://fiovit:9418f0f6-032b-4234-af8a-0ddc896eb84e@ondemand.saucelabs.com:80/wd/hub',
   desired_capabilities=desired_cap)


#driver = webdriver.Firefox()

driver.implicitly_wait(10)
driver.get("https://uiv2.devpanel.com/")
if not "DevPanel" in driver.title:
    raise Exception("Unable to load devpanel page!")
driver.find_element_by_partial_link_text('Login').click()
sleep(1)
passwd = driver.find_element_by_id('password')
passwd.send_keys("hello12344")
passwd.submit()
sleep(2)
print(driver.title)
driver.quit()