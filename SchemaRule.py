from SchemaLogger import *
from SchemaConst import *
from SchemaType import *

def CheckSchema(key, value, schema):
    return _check(key, value, schema)

def _checkType(key, value, keySchema):
    if keySchema[SchemaType] not in MetaType:
        Error("Schema type is not defined: " + keySchema[SchemaType])
        return False
    if not isinstance(value, MetaType[keySchema[SchemaType]][0]):
        Error("Config type and value is not matched: " + key)
        return False
    return True

def _check(key, value, schema):
    if key not in schema:
        if SchemaAnyOther not in schema:
            Error("Key does not defined in schema: " + key)
            return False
        else:
            key = SchemaAnyOther
    keySchema = _cloneSchema(schema[key], schema)
    if keySchema is None:
        Error("Could not get schema for key: " + key)
        return False
    return _doCheck(key, value, keySchema, schema)

def _doCheck(key, value, keySchema, schema):
    if not _checkType(key, value, keySchema):
        return False
    if SchemaRule in keySchema:
        for rule in keySchema[SchemaRule]:
            if not rule.Check(key, value, schema):
                return False
    if isinstance(value, dict):
        for k in value:
            if not _check(k, value[k], schema):
                return False
    return True

def _cloneSchema(schemaToClone, schema):
    result = {}
    for key in schemaToClone:
        if key != SchemaInherit:
            result[key] = schemaToClone[key]
    if SchemaInherit in schemaToClone:
        inheritKey = schemaToClone[SchemaInherit]
        if inheritKey not in schema:
            Error("Inherit key is not defined in schema: " + inheritKey)
            return None
        inheritSchema = _cloneSchema(schema[inheritKey], schema)
        if inheritSchema is None:
            return None
        for key in inheritSchema:
            if key not in result:
                result[key] = inheritSchema[key]
    return result

class BaseRule:
    def __init__(self):
        pass
    def Check(self, key, value, schema):
        return True

class KeyIn(BaseRule):
    def __init__(self, collection):
        self._collection = collection
    def Check(self, key, value, schema):
        for k in value:
            if k not in self._collection:
                Error("Key is not in specified collection: " + k)
                return False
        return True
    
class ValueIn(BaseRule):
    def __init__(self, collection):
        self._collection = collection
    def Check(self, key, value, schema):
        for v in self._collection:
            if value == v:
                return True
        Error("Value is not in specified collection: " + value)
        return False
    
class HasKey(BaseRule):
    def __init__(self, *args):
        self._keys = args
    def Check(self, key, value, schema):
        for k in self._keys:
            if k not in value:
                Error("Key is not defined: " + k + ", " + key)
                return False
        return True

class AtLeastOneKey(BaseRule):
    def __init__(self, *args):
        self._keys = args
    def Check(self, key, value, schema):
        for k in value:
            if k in self._keys:
                return True
        Error("None of required key is defined: " + key)
        return False

class CheckAsTypeFromKey(BaseRule):
    def __init__(self, key):
        self._key = key
    def Check(self, key, value, schema):
        if self._key not in value:
            Error("Key of type is not defined: " + self._key, + ", " + key)
            return False
        typeFromKey = value[self._key]
        if typeFromKey not in schema:
            Error("Type is not defined in schema: " + typeFromKey)
            return False
        keySchema = _cloneSchema(schema[typeFromKey], schema)
        if keySchema is None:
            return False
        return _doCheck(key, value, keySchema, schema)

class NotEmpty(BaseRule):
    def __init__(self, dataType):
        self._dataType = dataType
    def Check(self, key, value, schema):
        if self._dataType not in MetaType:
            Error("Schema data type is not defined: " + self._dataType)
            return False
        if MetaType[self._dataType][1](value):
            Error("Value is empty: " + key)
            return False
        return True

class CheckForeachAsType(BaseRule):
    def __init__(self, schemaKey):
        self._schemaKey = schemaKey
    def Check(self, key, value, schema):
        if self._schemaKey not in schema:
            Error("Schema key is not defined in schema when check for each: " + self._schemaKey)
            return False
        keySchema = _cloneSchema(schema[self._schemaKey], schema)
        if keySchema is None:
            return False
        for v in value:
            if not _doCheck(key, v, keySchema, schema):
                return False
        return True
