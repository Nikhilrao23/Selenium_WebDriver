from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class HiddenElements():
    def test(self):
        baseURL = 'https://letskodeit.teachable.com/p/practice'
        binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
        driver = webdriver.Firefox(firefox_binary=binary)
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        textbox = driver.find_element_by_id("displayed-text")
        final = textbox.is_displayed()
        print ("Text box is Displayed " + str(final))
        time.sleep(3)

        driver.find_element_by_id("hide-textbox").click()
        final = textbox.is_displayed()
        print ("Is it hidden " + str(final))
        time.sleep(3)

        driver.find_element_by_id("show-textbox").click()
        final = textbox.is_displayed()
        print ("Its Show Visible " + str(final))
        time.sleep(3)


ff = HiddenElements()
ff.test()
