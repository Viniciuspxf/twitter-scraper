from driver.dom_explorer import DOMExplorer


class Element(DOMExplorer):
    def __init__(self, element, timeout):
        super().__init__(element, timeout)

    def buildElement(self, webDriverElement):
        return Element(webDriverElement, self.timeout)
    
    def click(self):
        self.element.click()
    
    def send_keys(self, keys):
        self.element.send_keys(keys)

    def get_attribute(self, key):
        return self.element.get_attribute(key)
    
    def get_text(self):
        return self.element.text



