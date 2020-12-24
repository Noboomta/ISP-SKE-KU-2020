from selenium import webdriver

# URL to fetch and display
url = "https://thehackernews.com"

# create a browser instance
driver = webdriver.Firefox(executable_path=r'C:\Users\NoBoomTa\Desktop\Coding\geckodriver.exe')
driver.get( url )