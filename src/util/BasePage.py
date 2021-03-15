from util.CSSPropertyList import CSSProperties

class BasePage(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def get_css_properties(self, locator):
        self.object = self.driver.find_element_by_xpath(locator)
        self.properties = self.driver.execute_script('return window.getComputedStyle(arguments[0], null);', self.object)

    # def create_css_dictionary(self):
    #     cssList = []
    #     print(self.properties)
    #     print(self.object.value_of_css_property("backgroundColor"))
    #     for property in self.properties:
    #         if property in CSSProperties.GET:
    #             print(property, "|", self.object.value_of_css_property(property))
    #             cssList.append(self.object.value_of_css_property(property))
    #     return cssList

    def create_css_dictionary(self):
        cssList = []
        for css in CSSProperties.GET:
            try:
                cssList.append(css + "|" + self.object.value_of_css_property(css))
            except print(0):
                cssList.append("")
        return cssList