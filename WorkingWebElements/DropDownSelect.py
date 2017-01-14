from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DropDownSelect():
    def test(self):

        baseURL = 'https://letskodeit.teachable.com/p/practice'
        binary = FirefoxBinary ('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
        driver = webdriver.Firefox(firefox_binary= binary)
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)


        element = driver.find_element_by_id("carselect")
        sel = Select(element)

        sel.select_by_value("benz")
        print ("Select Benz by value")
        time.sleep(2)

        sel.select_by_index("2")
        print ("Select Benz by Value")
        time.sleep(2)

        sel.select_by_visible_text("BMW")
        print ("Select BMW by visible text")
        time.sleep(2)

        sel.select_by_index(2)
        print ("Select Honda by Index")
        time.sleep(2)



ff = DropDownSelect()
ff.test()