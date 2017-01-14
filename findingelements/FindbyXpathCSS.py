from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import  FirefoxBinary

class FindbyXpathCSS():
    def test(self):
        binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
        # C:\\Program Files (x86)\\Mozilla Firefox\\Firefox.exe
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(firefox_binary= binary)
        driver.get(baseURL)
        elementbyXpath = driver.find_element_by_xpath(".//input[@id='name']")

        if elementbyXpath is not None:
            print ("We found an element by Xpath")

        elementbyCSS = driver.find_element_by_css_selector("#displayed-text")

        if elementbyCSS is not None:
            print ("We found an element by CSS")

        driver.get("")
        driver.find_element_by_id("")


ff = FindbyXpathCSS()
ff.test()