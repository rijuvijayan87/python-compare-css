class BasePage(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def get_css_properties(self, locator):
        self.object = self.driver.find_element_by_xpath(locator)
        self.properties = self.driver.execute_script('return window.getComputedStyle(arguments[0], null);', self.object)

    def create_css_dictionary(self):
        cssDict = dict()
        for property in self.properties:
            cssDict.update({property: self.object.value_of_css_property(property)})
        return cssDict