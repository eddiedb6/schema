SchemaRoot = "schemaroot" # Root of schema of config schema
SchemaConfigRoot = "schemaconfigroot" # Root of config schema
SchemaAnyOther = "schemaanyother" # Wildcard for config key
SchemaIgnoreSchema = "schemaignoreschema" # Ignore schema check for value under this key

# Schema Keys

# Key Start #
SchemaType = "schematype"
SchemaRule = "schemarule"
SchemaInherit = "schemainherit"
# Key End #

SchemaKeys = [
    SchemaType,
    SchemaRule,
    SchemaInherit
]

# Schema Types

# To add a new type:
#    1. Define type name here
#    2. Then add type name to "SchemaTypes" list
#    3. Add type define in SchemaType.py

# Type Start #
SchemaTypeDict = "schematypedict"
SchemaTypeArray = "schematypearray"
SchemaTypeString = "schematypestring"
SchemaTypeInteger = "schematypeinteger"
# Type End #

SchemaTypes = [
    SchemaTypeDict,
    SchemaTypeArray,
    SchemaTypeString, 
    SchemaTypeInteger
]
