from SchemaConst import *

# 0. type
# 1. empty functor

MetaType = {
    SchemaTypeDict:
    [
        dict,
        lambda v: len(v) == 0
    ],
    SchemaTypeArray:
    [
        list,
        lambda v: len(v) == 0
    ],
    SchemaTypeString:
    [
        str,
        lambda v: v == "" or v is None
    ],
    SchemaTypeInteger:
    [
        int,
        lambda v: False
    ]
}
