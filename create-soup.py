from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get('http://python.org')

html_doc  = driver.page_source

soup = BeautifulSoup(html_doc, 'lxml')

print soup.prettify()

driver.quit()