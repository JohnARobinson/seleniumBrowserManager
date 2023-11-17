import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#url = 'http://docs.python.org/'
#url = 'https://www.sosi1.com/my/dashboard/main-dashboard'

# Windows
#chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#webbrowser.get(chrome_path).open(url)

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('http://www.google.com/')
driver.set_window_position(0, 0)
driver.set_window_size(970, 1080)
time.sleep(5) # Let the user actually see something!
driver.quit()
#driver.manage().window().setSize(new Dimension(300,500));