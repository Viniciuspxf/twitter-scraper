from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class DOMExplorer:
    def __init__(self, element, timeout):
        self.element = element
        self.timeout = timeout
   
    def findByXPathAndWrite(self, selector, text):
        element = self.findByXPath(selector)
        element.send_keys(text)

    def findByCSSAndWrite(self, selector, text):
        element = self.findByCSS(selector)
        element.send_keys(text)

    def findByCSSAndClick(self, selector):
        element = self.findByCSS(selector)
        element.click()
    
    
    def findByXPathAndClick(self, selector, index = 0):
        element = self.findElementsByXPath(selector)[index]
        element.click()

    def findByCSS(self, selector):
        webDriverElement = WebDriverWait(self.element, timeout=self.timeout).until(
            lambda d: d.find_element(By.CSS_SELECTOR, selector))
        
        return self.buildElement(webDriverElement)
        
    def findByXPath(self, selector):
        webDriverElement = WebDriverWait(self.element, timeout=self.timeout).until(
            lambda d: d.find_element(By.XPATH, selector))
    
        return self.buildElement(webDriverElement)
    
    def findElementsByCSS(self, selector):
        webDriverElements = WebDriverWait(self.element, timeout=self.timeout).until(
            lambda d: d.find_elements(By.CSS_SELECTOR, selector))
        
        return list(map(lambda webDriverElement: self.buildElement(webDriverElement), webDriverElements))
        
    def findElementsByXPath(self, selector):
        webDriverElements = WebDriverWait(self.element, timeout=self.timeout).until(
            lambda d: d.find_elements(By.XPATH, selector))
        
        return list(map(lambda webDriverElement: self.buildElement(webDriverElement), webDriverElements))