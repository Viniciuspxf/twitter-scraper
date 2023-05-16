from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

from driver.dom_explorer import DOMExplorer
from driver.element import Element


class Driver(DOMExplorer):
    def __init__(self, timeout = 10, scrollDownWaitTime = 6):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--lang=en')
    
        self.browser = webdriver.Chrome(options=options)
        self.scrollDownWaitTime = scrollDownWaitTime

        super().__init__(self.browser, timeout)

    def buildElement(self, webDriverElement):
        return Element(webDriverElement, self.timeout)

    def goToUrl(self, url):
        self.browser.get(url)

    def scrollDown(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(self.scrollDownWaitTime)

    def getPageHeight(self):
        return self.browser.execute_script("return document.body.scrollHeight")
