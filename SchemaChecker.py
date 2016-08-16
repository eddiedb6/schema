import os
import sys
import logging

from SchemaConst import *
from SchemaLogger import *
from SchemaRule import *
from SchemaSchema import *

class SchemaChecker:
    def __init__(self, configPath, schemaPath, defPath = None):
        self.__config = None
        self.__schema = None
        self.__configPath = configPath
        self.__schemaPath = schemaPath
        self.__defPath = defPath

    def Check(self):
        if self.__checkSchemaFile():
            return self.__checkConfigFile()
        return False

    def __checkSchemaFile(self):
        self.__schema = self.__evalFile(self.__schemaPath)        
        if not self.__schema:
            Error("Check schema failed")
            return False
        return CheckSchema(SchemaRoot, self.__schema, MetaSchema)

    def __checkConfigFile(self):
        self.__config = self.__evalFile(self.__configPath)
        if not self.__config:
            Error("Check config failed")
            return False
        return CheckSchema(SchemaConfigRoot, self.__config, self.__schema)

    def __evalFile(self, path):
        if self.__defPath is not None:
            if not os.path.exists(self.__defPath):
                Error("Import file does not exist: " + self.__defPath)
                return None
            modulePath = os.path.split(os.path.abspath(self.__defPath))[0]
            moduleName = os.path.basename(os.path.splitext(os.path.abspath(self.__defPath))[0])
            sys.path.append(modulePath)
            locals()[moduleName] = __import__(moduleName)
        if not os.path.exists(path):
            Error("Eval file does not exist: " + path)
            return None
        return eval(open(path).read())
