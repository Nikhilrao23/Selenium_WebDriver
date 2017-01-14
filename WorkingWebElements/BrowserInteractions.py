from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class BrowserInteractions():
    def test(self):

        baseURL = 'https://letskodeit.teachable.com/p/practice'
        binary = FirefoxBinary ('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
        driver = webdriver.Firefox(firefox_binary= binary)

        # Window Maximize
        driver.maximize_window()

        # Open the URl
        driver.get(baseURL)

        #Get Title
        title = driver.title
        print ("The title of the page is ", title)

        # Current URL
        currentURL = driver.current_url
        print ("The current URL is " , currentURL)

        # Browser Refresh
        driver.refresh()

        # Browser Refresh 2
        driver.get(driver.current_url)

        # Open another URL
        driver.get('https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1')

        # Browser Back
        driver.back()

        # Forward
        driver.forward()

        driver.get(baseURL)

        # Get Page Source
        page_source = driver.page_source
        print (page_source)

        # Browser Close  /Quit

        #driver.close()
        driver.quit()

ff = BrowserInteractions()
ff.test()
