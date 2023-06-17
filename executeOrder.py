import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def purchase(driver, listing):
    driver.find_element(By.XPATH, '/html/body/div[7]/div/div[7]/table/tbody/tr[{}]/td[6]/a'.format(listing+2)).click() #used to purchase
    try:
        myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[24]/div[2]/div[4]/a')))
        driver.find_element(By.XPATH, '/html/body/div[24]/div[2]/div[4]/a').click()
        print('success')
    except TimeoutException:
        print("Loading took too much time!")

    try:
        myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[26]/div[2]/div/div[1]/a')))
        driver.find_element(By.XPATH, '/html/body/div[26]/div[2]/div/div[1]/a').click()
        print('success')
    except TimeoutException:
        print("Loading took too much time!")

    time.sleep(5)