from os import name, times
from typing import List
from selenium import webdriver
import sys
import requests

url = "https://covidtracker-isp.herokuapp.com/"
browser = webdriver.Firefox(executable_path=r'C:\Users\NoBoomTa\Desktop\Coding\geckodriver.exe')
browser.get(url)
username_id = 'form.id_username'
password_id = 'form.id_password'
id_input_field = browser.find_element_by_id(username_id)
id_input_field.send_keys("noboomta")
pass_input_field = browser.find_element_by_id(password_id)
pass_input_field.send_keys("Boom3741")
pass_input_field.submit()

browser.implicitly_wait(5) 
country_field = browser.find_element_by_id("country")
country_field.send_keys("Thailand")
country_field.submit()

sp_dan = browser.find_element_by_class_name("text-danger")
total_comfirm = browser.find_element_by_id("Total-comfirm")

print(total_comfirm)
print(sp_dan)