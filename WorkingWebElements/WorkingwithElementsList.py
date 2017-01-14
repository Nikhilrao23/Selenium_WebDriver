from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
import time

class WorkingWithElementlist():
    def test(self):

        baseURL = 'https://letskodeit.teachable.com/p/practice'
        binary = FirefoxBinary ('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
        driver = webdriver.Firefox(firefox_binary= binary)
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)


        radiobuttonex = driver.find_elements(By.XPATH, "//input[contains(@type ,'radio')and contains(@name,'cars')]")
        size = len(radiobuttonex)
        print ("The size of the radio button are " + str(size))



        for radiobutton in radiobuttonex:
            isSelected = radiobutton.is_selected()

            if not isSelected:
                radiobutton.click()
                time.sleep(2)



ff = WorkingWithElementlist()
ff.test()