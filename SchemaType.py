from SchemaConst import *

# Foreach type:
#     Index [0]: type
#     Index [1]: empty functor

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
