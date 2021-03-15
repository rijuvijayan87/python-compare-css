from util.BasePage import BasePage


class Footer(BasePage):
    def __init__ (self, driver):
        self.driver = driver
        
    def page_objects(self):
        pass

    def get_css(self):
        self.get_css_properties('global-footer')
        self.create_css_dictionary()