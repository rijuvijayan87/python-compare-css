from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\riju.vijayan\\1LAB\\SELENIUM_SERVER\\chromedriver.exe")

driver.get("https://www.waikato.ac.nz/")
driver.maximize_window()

logo = driver.find_element_by_class_name('col-md-12')
properties = driver.execute_script('return window.getComputedStyle(arguments[0], null);', logo)

for property in properties:
    print("PROPERTY: " + property + " VALUE: " + logo.value_of_css_property(property))

driver.close()