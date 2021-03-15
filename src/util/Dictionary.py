class Dictionary:
    def __init__(self, cssproperties):
        self.cssproperties = cssproperties

    def getDictionaryLength(self):
        return len(self.cssproperties)
    
    def getDictionaryValues(self):
        return self.cssproperties
        