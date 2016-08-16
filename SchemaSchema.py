from SchemaConst import *
from SchemaRule import *

MetaSchema = {
    SchemaRoot: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            HasKey(SchemaConfigRoot)
        ]
    },
    SchemaType: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            ValueIn(SchemaTypes)
        ]
    },
    SchemaRule: {
        SchemaType: SchemaTypeArray
    },
    SchemaInherit: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            NotEmpty(SchemaTypeString)
        ]
    },
    SchemaAnyOther: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            KeyIn(SchemaKeys),
            AtLeastOneKey(SchemaType, SchemaInherit)
        ]
    }
}
