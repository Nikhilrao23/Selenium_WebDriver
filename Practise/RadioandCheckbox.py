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

        driver1 = driver.find_element(By.XPATH , ".//*[@id='bmwradio']")
        driver1.click()
        time.sleep(2)

        driver2 = driver.find_element(By.XPATH , ".//*[@id='benzradio']")
        driver2.click()
        time.sleep(2)

        driver3 = driver.find_element(By.XPATH, ".//*[@id='bmwcheck']")
        driver3.click()
        time.sleep(2)

        driver4 = driver.find_element(By.XPATH, ".//*[@id='hondacheck']")
        driver4.click()
        time.sleep(2)


        print ("BMW Radio is enabled ?" + str(driver1.is_selected()))
        print ("Benz Radio is enabled? " + str(driver2.is_selected()))
        print ("BMW Check box is enabled? " + str(driver3.is_selected()))
        print ("Honda Check box is enabled? " + str(driver4.is_selected()))







ff = ClickandType()
ff.test()