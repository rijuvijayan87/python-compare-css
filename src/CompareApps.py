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

    def listToString(self, s):  
        str1 = ""  
        for ele in s:  
            str1 += ele   
        return str1  


    def compare(self, css_app1, css_app2):

        total_properties = 0
        total_differences = 0
        
        for i in range(0, len(css_app1)):
            list_difference = []
            for css in css_app1[i]:
                if css in css_app2[i]:
                    pass
                else:
                    list_difference.append(css)
                total_properties += 1
            total_differences = total_differences + len(list_difference)
        return (total_properties - total_differences)/total_properties
try:
    e = CompareApps()
    e.apps[0].navigate()
    css_app1 = e.apps[0].extract_css()

    e.apps[1].navigate()
    css_app2 = e.apps[1].extract_css()

    comp = e.compare(css_app1, css_app2)
    print ("CSS Similarity index of two applications is ", comp * 100 , "%")
except print(0):
    pass
finally:
    e.selenium_teardown()

