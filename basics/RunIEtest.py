from selenium import webdriver
import os

driverLocation = "C:\\Users\\Nikhil\\PycharmProjects\\libs\\MicrosoftWebDriver.exe"
os.environ["webdriver.ie.driver"] =driverLocation

driver = webdriver.Ie(driverLocation)
driver.get("http:\\www.google.com")