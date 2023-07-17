from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time

def scrape_illnesses():
    DRIVER_PATH = r'C:\Users\ishpe\PycharmProjects\ScienceFair2023-24\Data Collection\chromedriver.exe'
    driver = webdriver.Chrome()
    driver.get('https://www.nhsinform.scot/illnesses-and-conditions/a-to-z')
    #names = driver.find_elements(By.XPATH, "/html/body/main/div[2]/div/div/div/div[3]/ul/li[1]")
    #names = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div/div[3]/ul/li[1]/a")
    names = driver.find_elements(By.TAG_NAME, "li")
    valids = [i.text for i in names if i.text != "Back to top" and i.text != "" and len(i.text) != 1]
    for i in valids:
        print(i)
    with open('ListOfIllnesses.txt', 'w') as tfile:
        tfile.write('\n'.join(valids))
def scrape_symptoms():
    pass

scrape_illnesses()
