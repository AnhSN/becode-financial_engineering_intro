from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

with webdriver.Firefox() as driver:
    driver.get(f'https://finance.yahoo.com/quote/AAPL/history')
    scroll_button = driver.find_element('id', 'scroll-down-btn')
    scroll_button.click()
    cookie_button = driver.find_element(By.NAME, 'reject')
    cookie_button.click()
    table = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table')
    print(table)
    print(table.text)
