from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class FFtest():
    def test(self):

        binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')

        #C:\\Program Files (x86)\\Mozilla Firefox\\Firefox.exe

        driver = webdriver.Firefox(firefox_binary=binary)
        driver.get("http://www.google.com")
ff = FFtest()
ff.test()