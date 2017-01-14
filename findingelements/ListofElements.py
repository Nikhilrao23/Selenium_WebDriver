from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import  FirefoxBinary
from selenium.webdriver.common.by import By

class ListofElements():
    def test(self):
        binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
        # C:\\Program Files (x86)\\Mozilla Firefox\\Firefox.exe
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(firefox_binary= binary)
        driver.get(baseURL)

        elementbyClassName = driver.find_elements_by_class_name("inputs")
        length = len(elementbyClassName)

        if elementbyClassName is not None:
            print ("Size of the list is: " + str(length))

        elementbyTagName = driver.find_elements(By.TAG_NAME, "a")
        length2 = len(elementbyTagName)

        if elementbyTagName is not None:
            print ("Size of the list is: "+ str(length2))



ff = ListofElements()
ff.test()