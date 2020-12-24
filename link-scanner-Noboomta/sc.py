from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://www.duckduckgo.com/"
browser = webdriver.Firefox(executable_path=r'C:\Users\NoBoomTa\Desktop\Coding\geckodriver.exe')
browser.get(url)

field_id = 'search_form_input_homepage'
input_field = browser.find_element_by_id(field_id)
input_field.send_keys("Kasetsart University")
input_field.send_keys(Keys.ENTER)

