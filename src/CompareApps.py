from util.Application import Application
from Setup import Setup

class CompareApps(Setup):
    def __init__(self):
        super().__init__()
        self.apps = [Application(self.driver, self.app1), Application(self.driver, self.app2)]

    def finish(self):
        self.selenium_teardown()

    def compare(self, css_app1, css_app2):
        self.css_app1 = css_app1
        self.css_app2 = css_app2
        for i in range(0, 1):
            sim = self.cosine_similarity(self.css_app1[i], self.css_app2[i])
            print(sim)
        
    def cosine_similarity(self, vec1,vec2):
        sum11, sum12, sum22 = 0, 0, 0
        for i in range(len(vec1)):
            x = vec1[i]; y = vec2[i]
            sum11 += x*x
            sum22 += y*y
            sum12 += x*y
        return sum12/math.sqrt(sum11*sum22)

e = CompareApps()

e.apps[0].navigate()
css_app1 = e.apps[0].extract_css()

e.apps[1].navigate()
css_app2 = e.apps[1].extract_css()

e.compare(css_app1, css_app2)



e.selenium_teardown()
    
