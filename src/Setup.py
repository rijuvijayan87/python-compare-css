from selenium import webdriver
import configparser

class Setup:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('conf.ini')
        self.app1 = self.config['application']['APP_URL1']
        self.app2 = self.config['application']['APP_URL2']
        self.selenim_setup()

    def selenim_setup(self):
        self.driver = webdriver.Chrome(executable_path=self.config['selenium']['CHROME_DRIVER'])
        self.driver.maximize_window()