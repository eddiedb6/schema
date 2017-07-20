class ImportFile:
    def __init__(self, path):
        self.__path = path

    def GetImportPath(self):
        return self.__path
    
class ImportPartial:
    def __init__(self, path):
        self.__path = path

    def GetPartialPath(self):
        return self.__path
