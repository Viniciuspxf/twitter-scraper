from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class Driver:
    def __init__(self, timeout = 10, scrollDownWaitTime = 6):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--lang=en')
    
        self.browser = webdriver.Chrome(options=options)
        self.timeout = timeout
        self.scrollDownWaitTime = scrollDownWaitTime

    def goToUrl(self, url):
        self.browser.get(url)

    def findByXPathAndWrite(self, selector, text):
        element = self.findByXPath(selector)
        element.send_keys(text)
        

    def findByCSSAndWrite(self, selector, text):
        element = self.findByCSS(selector)
        element.send_keys(text)

    def findByCSSAndClick(self, selector):
        element = self.findByCSS(selector)
        element.click()
    
    def findByXPathAndClick(self, selector):
        element = self.findByXPath(selector)
        element.click()
    
    def findByXPathAndClick(self, selector, index):
        element = self.findElementsByXPath(selector)[index]
        element.click()

    def findByCSS(self, selector):
        return WebDriverWait(self.browser, timeout=self.timeout).until(
            lambda d: d.find_element(By.CSS_SELECTOR, selector))
        
    def findByXPath(self, selector):
        return WebDriverWait(self.browser, timeout=self.timeout).until(
            lambda d: d.find_element(By.XPATH, selector))
    
    def findElementsByCSS(self, selector):
        return WebDriverWait(self.browser, timeout=self.timeout).until(
            lambda d: d.find_elements(By.CSS_SELECTOR, selector))
        
    def findElementsByXPath(self, selector):
        return WebDriverWait(self.browser, timeout=self.timeout).until(
            lambda d: d.find_elements(By.XPATH, selector))

    def scrollDown(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(self.scrollDownWaitTime)

    def getPageHeight(self):
        return self.browser.execute_script("return document.body.scrollHeight")
