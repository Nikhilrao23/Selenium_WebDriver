from selenium import webdriver
import os



#https://sites.google.com/a/chromium.org/chromedriver/downloads
#https://chromedriver.storage.googleapis.com/index.html?path=2.21/
driverLocation = "C:\\Users\\Nikhil\\PycharmProjects\\libs\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] =driverLocation

driver = webdriver.Chrome(driverLocation)
driver.get("http:\\www.google.com")