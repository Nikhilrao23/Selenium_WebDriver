from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class WorkingwithElements():
    def test(self):


        binary = FirefoxBinary("C:\Program Files (x86)\Mozilla Firefox\Firefox.exe")
        driver = webdriver.Firefox(firefox_binary= binary)
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)



        radiobutton = driver.find_elements(By.XPATH,"//input[contains(@type, 'radio') and contains(@name, 'cars')]")
        size = len(radiobutton)
        print ("The lenght of the radio button is " + str(size))


        for radiobuttonex in radiobutton:
            isSelected = radiobuttonex.is_selected()

            if not isSelected:
                radiobuttonex.click()
                time.sleep(2)








ff = WorkingwithElements()
ff.test()