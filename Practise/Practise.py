from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time


class DropDownSelect():
    def test(self):


        binary = FirefoxBinary("C:\Program Files (x86)\Mozilla Firefox\Firefox.exe")
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(firefox_binary= binary)
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)

        element = driver.find_element(By.ID, "carselect")
        sel = Select(element)

        sel.select_by_value("bmw")
        print ("BMW selected by value ")
        time.sleep(2)

        sel.select_by_index("2")
        print ("Honda selected by index")
        time.sleep(2)

        sel.select_by_visible_text("Benz")
        print("Benz Selected by visible text")
        time.sleep(2)

        sel.select_by_index(2)
        print ("Select Honda by index")
        time.sleep(2)





ff = DropDownSelect()
ff.test()


