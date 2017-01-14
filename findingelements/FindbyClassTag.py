from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import  FirefoxBinary

class FindbyClassTag():
    def test(self):
        binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
        # C:\\Program Files (x86)\\Mozilla Firefox\\Firefox.exe
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(firefox_binary= binary)
        driver.get(baseURL)
        elementbyClassTag = driver.find_element_by_class_name("displayed-class")
        elementbyClassTag.send_keys("Testing this Link")
        if elementbyClassTag is not None:
            print ("We found an element by Class Name")

        elementbyTagName = driver.find_element_by_tag_name("h1")
        text = elementbyTagName.text

        if  elementbyTagName is not None:
            print ("We found an element by Tag Name is: " + text)


ff = FindbyClassTag()
ff.test()