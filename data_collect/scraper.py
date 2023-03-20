from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

with webdriver.Firefox() as driver:
    driver.get(f'https://finance.yahoo.com/quote/AAPL/history')
    driver.implicitly_wait(0.5)
    # Skip the cookies popup
    scroll_button = driver.find_element('id', 'scroll-down-btn')
    scroll_button.click()
    cookie_button = driver.find_element(By.NAME, 'reject')
    cookie_button.click()

    ### Get the whole table as string
    #table = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table').text
    #print(table)
    #print(type(table))

    ### Getting each cell separatly
    # Obtain the number of rows and columns
    rows = 1+len(driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr'))
    cols = len(driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr[1]/td'))
    # Initiate variables used in the loop
    popup = True
    data = []
    data_by_row = []
    # Browse through the table and save the data as  
    for r in range(2, rows):
        data = []
        for p in range(1, cols+1):
            # Skip the signin popup once
            if popup:
                try:
                    signin_popup = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[4]/div/div/div[1]/div/div/div/div/div/section/button[2]')
                    signin_popup.click()
                    popup = False
                except:
                    pass
            # Skip the 'Dividend' lines
            if driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr['+str(r)+']/td[2]/span').text == "Dividend":
                pass
            # Get the text from each column of the table and save it in
            else:
                value = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[2]/div/div/section/div[2]/table/tbody/tr['+str(r)+']/td['+str(p)+']').text
                data.append(value)
        data_by_row.append(data)
    df = pd.DataFrame(data = data_by_row, columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj_Close', 'Volume'])

print(df.head())
df.to_csv('database/AAPL.csv')