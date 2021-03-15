from util.Header import Header
from util.Footer import Footer
from util.Dictionary import Dictionary

class Application:

    def __init__ (self, driver, url):
        self.driver = driver
        self.url = url

    def navigate(self):
        self.driver.get(self.url)

    def extract_css(self):
        header = Header(self.driver)
        header.get_css()
        headerCSS = header.create_css_dictionary()
        footer = Footer(self.driver)
        footer.get_css()
        footerCSS = footer.create_css_dictionary()
        return [Dictionary(headerCSS), Dictionary(footerCSS)]
