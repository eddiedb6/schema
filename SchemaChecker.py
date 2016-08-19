import os
import sys
import logging

from SchemaConst import *
from SchemaLogger import *
from SchemaRule import *
from SchemaSchema import *
from SchemaImporter import ImportFile

class SchemaChecker:
    def __init__(self, configPath, schemaPath, defPath = None):
        self.__config = None
        self.__schema = None
        self.__defPath = defPath
        self.__configPath = os.path.abspath(configPath)
        self.__schemaPath = os.path.abspath(schemaPath)


    def Check(self):
        if self.__checkSchemaFile():
            return self.__checkConfigFile()
        return False, None

    def __checkSchemaFile(self):
        result, self.__schema = self.__evalFile(self.__schemaPath)        
        if not result:
            Error("Check schema failed")
            return False
        result, self.__schema = self.__doImport(self.__schema)
        if not result:
            Error("Import schema failed")
            return False
        return CheckSchema(SchemaRoot, self.__schema, MetaSchema)

    def __checkConfigFile(self):
        result, self.__config = self.__evalFile(self.__configPath)
        if not result:
            Error("Check config failed")
            return False, None
        result, self.__config = self.__doImport(self.__config)
        if not result:
            Error("Import config failed")
            return False, None
        return CheckSchema(SchemaConfigRoot, self.__config, self.__schema), self.__config

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
            return False, None
        return True, eval(open(path).read())

    def __doImport(self, config):
        result = True
        configCopy = None
        if isinstance(config, dict):
            configCopy = {}
            for k in config:
                kResult, configCopy[k] = self.__doImport(config[k])
                result &= kResult
        elif isinstance(config, list):
            configCopy = []
            for v in config:
                vResult, vConfig = self.__doImport(v)
                result &= vResult
                configCopy.append(vConfig)
        elif isinstance(config, ImportFile):
            importPath = os.path.join(os.path.split(self.__configPath)[0], config.GetImportPath())
            result, importConfig = self.__evalFile(importPath)
            if result:
                result, configCopy = self.__doImport(importConfig)
        else:
            configCopy = config            
        return result, configCopy
