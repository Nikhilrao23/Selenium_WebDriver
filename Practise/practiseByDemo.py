from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By


class FindIdName():
    def test(self):
        binary = FirefoxBinary("C:\Program Files (x86)\Mozilla Firefox\Firefox.exe")
        baseURL = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox(firefox_binary=binary)
        driver.get(baseURL)

        elementbyID = driver.find_element_by_id("displayed-text")
        if elementbyID is not None:
            print ("ID is present")

        elementbyName = driver.find_element_by_name("show-hide")
        if elementbyName is not None:
            print ("Name is Present")

        elementbyXpath = driver.find_element_by_xpath(".//input[@id='alertbtn']")
        if elementbyXpath is not None:
            print ("Xpath is Present")

        elementbyCSS = driver.find_element_by_css_selector("#displayed-text")
        if elementbyCSS is not None:
            print ("CSS is present")

        elementbyLinkTest = driver.find_element_by_link_text("Login")
        if elementbyLinkTest is not None:
            print ("Link Text is Present")

        elementbyPartialLinkTest = driver.find_element_by_partial_link_text("Prac")
        if elementbyPartialLinkTest is not None:
            print ("Partial Link Test is Present")

        elementbyClassName = driver.find_element_by_class_name("displayed-class")
        elementbyClassName.send_keys("Nikhil Rao Balaji")
        if elementbyClassName is not None:
            print("Class Name is present")

        elementbyTagName = driver.find_element_by_tag_name("h1")
        text = elementbyTagName.text
        if elementbyTagName is not None:
            print ("The Heading is " + text)


        elementforID = driver.find_element(By.ID, "displayed-text")
        if elementforID is not None:
            print ("ID is present")

        elementforXpath = driver.find_element(By.XPATH, ".//*[@id='hide-textbox']")
        if elementforXpath is not None:
            print ("Xpath is Present")

        elementforLinkText = driver.find_element(By.LINK_TEXT,"Login")
        if elementforLinkText is not None:
            print("Link Text is Preset")

        elementForTagName = driver.find_elements_by_tag_name("a")
        lenght2 = len(elementForTagName)
        if elementForTagName is not None:
            print ("The No of Anchor Tags is: " +str(lenght2))


ff = FindIdName()
ff.test()
