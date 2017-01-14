from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import  FirefoxBinary

class FindIdName():
    def test(self):
        binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
        # C:\\Program Files (x86)\\Mozilla Firefox\\Firefox.exe
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(firefox_binary= binary)
        driver.get(baseURL)
        elementbyID = driver.find_element_by_id("name")

        if elementbyID is not None:
            print ("We found an element by id")

        elementbyname = driver.find_element_by_name("show-hide")

        if elementbyname is not None:
            print ("We found an element by name")


ff = FindIdName()
ff.test()