import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
input("Surf to the table, then press ENTER to start scraping")
dropdown = Select(driver.find_element_by_id("selPag"));
for i in range(len(dropdown.options)):
    dropdown = Select(driver.find_element_by_id("selPag"));
    dropdown.select_by_index(i);
    driver.find_element_by_id("selPag").submit()
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, "lxml")
    tables = soup.find_all("table")
    df = pd.read_html(str(tables))
    df[0].to_csv(r'output.csv', sep=";", mode="a", index = False, header=False)
