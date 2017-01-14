from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import  FirefoxBinary
from selenium.webdriver.common.by import By

class ByDemo():
    def test(self):
        binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
        # C:\\Program Files (x86)\\Mozilla Firefox\\Firefox.exe
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(firefox_binary= binary)
        driver.get(baseURL)

        elementbyID = driver.find_element(By.ID, "name")
        if elementbyID is not None:
            print ("We found the ID")

        elementbyXpath = driver.find_element(By.XPATH, ".//input[@id='displayed-text']")
        if elementbyXpath is not None:
            print ("We found the elementbyXpath")

        elementbyLinkText = driver.find_element(By.LINK_TEXT, "Login")
        if elementbyLinkText is not None:
            print ("We found the element by Link Text")


ff = ByDemo()
ff.test()