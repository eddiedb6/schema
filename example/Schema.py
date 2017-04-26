{
    SchemaConfigRoot: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            HasKey(Const.UI, Const.Action)
        ]
    },
    Const.UI: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            HasKey(Const.Name, Const.Type),
            CheckAsTypeFromKey(Const.Type)
        ]
    },
    Const.UIRoot: {
        SchemaType: SchemaTypeDict
    },
    Const.UIApp: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            HasKey(Const.Path)
        ]
    },
    Const.UIWeb: {
        SchemaInherit: Const.UIApp
    },
    Const.AppRoot: {
        SchemaType: SchemaTypeDict
    },
    Const.AppButton: {
        SchemaInherit: Const.AppRoot
    },
    Const.AppForm: {
        SchemaInherit: Const.AppRoot
    },
    Const.Path: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            NotEmpty(SchemaTypeString)
        ]
    },
    Const.Name: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            NotEmpty(SchemaTypeString)
        ]
    },
    Const.Type: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            ValueIn(Const.UIType)
        ]
    },
    Const.SubUI: {
        SchemaType: SchemaTypeArray,
        SchemaRule: [
            CheckForeachAsType(Const.UI)
        ]
    },
    Const.Caption: {
        SchemaType: SchemaTypeString
    },
    Const.BreakTime: {
        SchemaType: SchemaTypeInteger
    },
    Const.Text: {
        SchemaType: SchemaTypeString
    },
    Const.Script: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            NotEmpty(SchemaTypeString)
        ]
    },
    Const.Action: {
        SchemaType: SchemaTypeDict
    },
    Const.SubAction: {
        SchemaType: SchemaTypeArray,
        SchemaRule: [
            CheckForeachAsType(Const.Action)
        ]
    },
    Const.Ignore: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            IgnoreChildSchema()
        ]
    }
}
