from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By


class ElementsState():
    def test(self):


        baseURL = 'http://www.google.com'
        binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
        driver = webdriver.Firefox(firefox_binary= binary)
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseURL)

        e1 = driver.find_element_by_id("gs_htif0")
        e1state = e1.is_enabled()
        print ("E1 is enabled? " +str(e1state))

        e2 = driver.find_element_by_id("gs_taif0")
        e2state = e2.is_enabled()
        print("E2 is enabled? " + str(e2state))

        e3 = driver.find_element_by_id("gs_sc0")
        e3state = e3.is_enabled()
        print("E1 is enabled? " + str(e3state))

        e3.send_keys("LetsKodeit")


ff = ElementsState()
ff.test()
