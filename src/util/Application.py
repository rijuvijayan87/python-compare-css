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
        headerCSS = header.get_css()
        footer = Footer(self.driver)
        footerCSS = footer.get_css()
        return [headerCSS, footerCSS]
