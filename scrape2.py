
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service('/opt/homebrew/bin/chromedriver')  
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.freshdirect.com')

print(driver.title)
soup = BeautifulSoup(driver.page_source, 'html.parser')
f = open("myfile3.txt", "x")
f.write(str(soup))
f.close()
driver.quit()
