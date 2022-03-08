import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
account = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/my-account/']")
account.click()
email = driver.find_element_by_id("reg_email")
email.send_keys("st_helens@mail.ru")
password = driver.find_element_by_id("reg_password")
password.send_keys("Aa2301887!#")
register = driver.find_element_by_css_selector("input[name='register']")
register.click()
driver.quit()

import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.support.select import Select
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
account = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/my-account/']")
account.click()
username = driver.find_element_by_id("username")
username.send_keys("st_helens@mail.ru")
password = driver.find_element_by_id("password")
password.send_keys("Aa2301887!#")
login = driver.find_element_by_css_selector("input[name='login']")
login.click()
driver.quit()
