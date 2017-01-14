from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class ClickandType():
    def test(self):


        binary = FirefoxBinary("C:\Program Files (x86)\Mozilla Firefox\Firefox.exe")
        driver = webdriver.Firefox(firefox_binary= binary)
        baseURL = "https://www.google.com"
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver1 = driver.find_element(By.ID, "gs_htif0")
        sel1 = driver1.is_enabled()
        print ("Is this Enabled " + str(sel1))

        driver2 = driver.find_element(By.ID, "gs_taif0")
        sel2 = driver2.is_enabled()
        print ("Is this Enabled " + str(sel2))

        driver3 = driver.find_element(By.ID , "lst-ib")
        sel3 = driver3.is_enabled()
        print ("Is this enabled " + str(sel3))


        driver3.send_keys("Lets Kode it ")







ff = ClickandType()
ff.test()