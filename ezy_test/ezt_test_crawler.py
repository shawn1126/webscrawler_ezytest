# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows.

# Python program to demonstrate
# selenium

from selenium import webdriver
from time import sleep
driver=webdriver.Chrome('./chromedriver.exe')
driver.get('https://easytest.yzu.edu.tw')
searchbar=driver.find_element_by_class_name('navbar-left')
login_button=searchbar.find_element_by_tag_name('a')
login_button.click()

sleep(1)
account=driver.find_element_by_name('cust_id')
password=driver.find_element_by_name('cust_pass')
account.send_keys("Unknown")
password.send_keys("Unknown")

driver.find_element_by_id("send").click()
