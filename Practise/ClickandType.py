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

        lgin = driver.find_element(By.XPATH,"//div[@id = 'navbar']//a[@href = '/sign_in']")
        lgin.click()


        usermail = driver.find_element(By.ID,".//*[@id='user_email']")
        usermail.send_keys("test")
        time.sleep(3)

        userpwd = driver.find_element(By.ID,".//*[@id='user_password']")
        userpwd.send_keys("test")
        time.sleep(3)

        usermail.clear()
        usermail.send_keys("NikhilRao")
        time.sleep(3)

        driver.quit()





ff = ClickandType()
ff.test()