from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class BrowserInteraction():
    def test(self):


        binary = FirefoxBinary("C:\Program Files (x86)\Mozilla Firefox\Firefox.exe")
        driver = webdriver.Firefox(firefox_binary= binary)
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver.get(baseURL)

        #Maximize Window
        driver.maximize_window()
        print("Window is maximized")

        #Open the URL
        driver.get(baseURL)

        #Current URL
        currentURL = driver.current_url
        print ("The Current URL is " + str(currentURL))

        #Browser Refresh
        driver.refresh()
        print("Page is Refreshed")

        #Browser Refresh

        driver.get(currentURL)

        #Open another URL

        driver.get("https://www.google.com")
        print ("Google Page")

        #Browser Back

        driver.back()
        print ("Browser is Gone back by one step")

        #Browser Forward

        driver.forward()
        print ("Browser is Forwarded")


        #Page Source

        pagesource = driver.page_source
        print (pagesource)

        #Browser Quit/Close
        driver.close()
        driver.quit()






ff = BrowserInteraction()
ff.test()