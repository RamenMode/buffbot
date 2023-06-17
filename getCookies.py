import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://buff.163.com/goods/857578")

# Here, you must login to steam from the automated browser. Wait for the browser to exit and the cookies will be saved in the specified location

time.sleep(120) # wait for manual login which will save cookies
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb")) #if want to write cookies

driver.quit()