from section.Application import Application
from Setup import Setup

class CompareApps(Setup):
    def __init__(self):
        super().__init__()
        self.apps = [Application(self.driver, self.app1), Application(self.driver, self.app2)]

    def finish(self):
        self.selenium_teardown()

e = CompareApps()

e.apps[0].navigate()
e.selenium_teardown()
    
