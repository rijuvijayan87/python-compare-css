from section.Application import Application
from Setup import Setup

class CompareApps(Setup):
    def __init__(self):
        super().__init__()
        self.apps = [Application(self.driver, self.app1), Application(self.driver, self.app2)]


e = CompareApps()

e.apps[0].navigate()
    
