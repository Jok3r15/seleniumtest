from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
#in case I want the browser to open in the background
options.headless = False

service = Service('PATH_TO_THE_DRIVER')
driver = webdriver.Firefox(options=options)
#openin firefox and going to twitter
driver.get("https://twitter.com/login")
time.sleep(3)
#creating username and password variables and also login form user and password variables
username = 'username'
password = 'password.'
usernamefield = driver.find_element_by_css_selector('div.css-1dbjc4n:nth-child(6) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)')
passwordfield = driver.find_element_by_css_selector('div.css-1dbjc4n:nth-child(7) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)')
#typing the user and password into the twitter login form
usernamefield.send_keys(username)
passwordfield.send_keys(password)
#click login
driver.find_element_by_css_selector('.r-jwli3a').click()
time.sleep(5)
#go to messages
driver.find_element_by_css_selector('a.css-1dbjc4n:nth-child(4) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)').click()
time.sleep(3)
#go to specific messages with specific person
driver.find_element_by_css_selector('.r-1iusvr4').click()
time.sleep(5)
#message1
driver.find_element_by_css_selector('.public-DraftStyleDefault-block').click()
actions = ActionChains(driver)
actions.send_keys('How')
actions.perform()
driver.find_element_by_css_selector('div.r-13hce6t:nth-child(3) > div:nth-child(1) > svg:nth-child(1)').click()
#message2
driver.find_element_by_css_selector('.public-DraftStyleDefault-block').click()
actions.send_keys('are')
actions.perform()
driver.find_element_by_css_selector('div.r-13hce6t:nth-child(3) > div:nth-child(1) > svg:nth-child(1)').click()
#message3
driver.find_element_by_css_selector('.public-DraftStyleDefault-block').click()
actions.send_keys('you')
actions.perform()
driver.find_element_by_css_selector('div.r-13hce6t:nth-child(3) > div:nth-child(1) > svg:nth-child(1)').click()
#closing browser window
driver.close()