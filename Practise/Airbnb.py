from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class Airbnb():
    def test(self):


        binary = FirefoxBinary("C:\Program Files (x86)\Mozilla Firefox\Firefox.exe")
        baseURL = "https://www.airbnb.com/"
        driver = webdriver.Firefox(firefox_binary= binary)
        driver.get(baseURL)
        driver.maximize_window()
        driver.implicitly_wait(10)


        where = driver.find_element(By.XPATH, ".//*[@id='search-location']")
        where.send_keys("Chennai, Tamil Nadu, India")
        print ("Entered the place where we wanted to go ")
        time.sleep(3)

        check_in = driver.find_element(By.ID, "startDate")
        check_in.send_keys("01/24/2017")
        print ("Entered the start Date ")
        time.sleep(3)

        check_out = driver.find_element(By.ID, "endDate")
        check_out.send_keys("02/13/2017")
        print ("Entered the Check out date ")
        time.sleep(3)

        guests = driver.find_element(By.XPATH, "//div[@class= 'SearchForm__guests text-left']")
        print ("Select the number of Guests")
        guests.click()
        time.sleep(3)

        adult = driver.find_element(By.XPATH, "//button[@aria-label='Increment number of adults']")
        adult.click()
        print ("1 adult Selected")

        children = driver.find_element(By.XPATH, "//button[@aria-label='Increment number of children']")
        children.click()
        print ("1 Children Selected")

        search_button = driver.find_element(By.XPATH, "//button[@type ='submit']")
        search_button.click()
        time.sleep(2)









ff = Airbnb()
ff.test()


