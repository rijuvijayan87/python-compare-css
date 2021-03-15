from util.Application import Application
from Setup import Setup
import math
import numpy as np


class CompareApps(Setup):
    def __init__(self):
        super().__init__()
        self.apps = [Application(self.driver, self.app1), Application(self.driver, self.app2)]

    def finish(self):
        self.selenium_teardown()

    def levenshtein_ratio_and_distance(self, s, t, ratio_calc = False):
        """ levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t
    """
    # Initialize matrix of zeros
        rows = len(s)+1
        cols = len(t)+1
        distance = np.zeros((rows,cols),dtype = int)

        # Populate matrix of zeros with the indeces of each character of both strings
        for i in range(1, rows):
            for k in range(1,cols):
                distance[i][0] = i
                distance[0][k] = k

        # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
        for col in range(1, cols):
            for row in range(1, rows):
                if s[row-1] == t[col-1]:
                    cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
                else:
                    # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                    # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                    if ratio_calc == True:
                        cost = 2
                    else:
                        cost = 1
                distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                    distance[row][col-1] + 1,          # Cost of insertions
                                    distance[row-1][col-1] + cost)     # Cost of substitutions
        if ratio_calc == True:
            # Computation of the Levenshtein Distance Ratio
            Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
            return Ratio
        else:
            # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
            # insertions and/or substitutions
            # This is the minimum number of edits needed to convert string a to string b
            return "The strings are {} edits away".format(distance[row][col])

    def compare(self, css_app1, css_app2):
        self.css_app1 = css_app1
        self.css_app2 = css_app2
        
        for i in range(0, len(self.css_app1)):
            ratio = self.levenshtein_ratio_and_distance(self.css_app1[i].getDictionaryValues(), self.css_app2[i].getDictionaryValues(), ratio_calc = True)
            print(ratio)
            if self.css_app1[i].getDictionaryValues() == self.css_app2[i].getDictionaryValues():
                print("Same Object")
            else:
                print("Different Object")
                print("##### APP 1 : Counter - ", i , " | ", self.css_app1[i].getDictionaryValues())
                print("*******************************************")
                print("*******************************************")
                print("*******************************************")
                print("##### APP 2 : Counter - ", i , " | ", self.css_app2[i].getDictionaryValues())

    def cosine_similarity(self, vec1,vec2):
        print(vec1)
        print(vec2)
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
