from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class ClickandType():
    def test(self):


        binary = FirefoxBinary("C:\Program Files (x86)\Mozilla Firefox\Firefox.exe")
        driver = webdriver.Firefox(firefox_binary= binary)
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)



        textbox = driver.find_element_by_id("displayed-text")
        final = textbox.is_displayed()
        print ("Is it displayed " + str(final))
        time.sleep(2)


        final2 = driver.find_element_by_id("hide-textbox").click()
        final = textbox.is_displayed()
        print ("Is Hide Button displayed" + str (final))
        time.sleep(2)


        final3 = driver.find_element_by_id("show-textbox").click()
        final = textbox.is_displayed()
        print ("Is Show Button Displayed" + str(final))
        time.sleep(2)







ff = ClickandType()
ff.test()