from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
import time

class RadioandCheckbox():
    def test(self):

        baseURL = 'https://letskodeit.teachable.com/p/practice'
        binary = FirefoxBinary ('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
        driver = webdriver.Firefox(firefox_binary= binary)
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)


        bmwradiobtn = driver.find_element_by_id("bmwradio")
        bmwradiobtn.click()
        time.sleep(2)

        benzradiobtn = driver.find_element_by_id("benzradio")
        benzradiobtn.click()
        time.sleep(2)

        bmwcheckbox = driver.find_element_by_id("bmwcheck")
        bmwcheckbox.click()
        time.sleep(2)

        benzcheckbox = driver.find_element_by_id("benzcheck")
        benzcheckbox.click()
        time.sleep(2)


        print ("BMW RB Selected ? " + str(bmwradiobtn.is_selected()))
        print ("Benz RB Selected ? " +  str (benzradiobtn.is_selected()))
        print ("BMW Check box Selected? " + str(bmwcheckbox.is_selected()))
        print ("Benz Check box selected? " +str(benzcheckbox.is_selected()))


ff = RadioandCheckbox()
ff.test()