from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import  FirefoxBinary

class FindbyLinkText():
    def test(self):
        binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
        # C:\\Program Files (x86)\\Mozilla Firefox\\Firefox.exe
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(firefox_binary= binary)
        driver.get(baseURL)
        elementbyLinkText = driver.find_element_by_link_text("Login")
        if elementbyLinkText is not None:
            print ("We found an element by Link Text")

        elementbyPartialLinkText = driver.find_element_by_partial_link_text("Pract")
        if  elementbyPartialLinkText is not None:
            print ("We found an element by Partial Link Text")

        driver.get("")
        driver.find_element_by_id("")


ff = FindbyLinkText()
ff.test()