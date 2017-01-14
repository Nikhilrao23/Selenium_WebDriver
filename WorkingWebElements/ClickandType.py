from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
import time


class BrowserInteraction():
    def test(self):

        baseURL = 'https://letskodeit.teachable.com/p/practice'
        binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
        driver = webdriver.Firefox(firefox_binary= binary)
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)


        findlogin = driver.find_element(By.XPATH, '//a[@href = "/sign_in"]')
        findlogin.click()

        useremail = driver.find_element(By.ID, "user_email")
        useremail.send_keys("test")

        time.sleep(3)

        userpasswd = driver.find_element(By.ID, "user_password")
        userpasswd.send_keys("test")

        time.sleep(3)

        useremail.clear()

        useremail.send_keys("Nikhil")







ff = BrowserInteraction()
ff.test()

