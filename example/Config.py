# Config Rule:
#     1. The key name should be uniq
#     2. Support dict, array, and basic type only
#     3. If use "ImportFile", the file path is relative to root config file path

{
    Const.UI: {
        Const.Name: "App",
        Const.Type: Const.UIApp,
        Const.Path: "C:/Windows/System32/calc.exe",
        Const.SubUI: [
            ImportFile("ConfigDesktop.py")
        ]
    },

    Const.Action: {
        Const.SubAction: [
            ImportFile("ConfigScript.py"),
            ImportPartial("PartialScript.py")
        ]
    },

    Const.PartialImport: ImportPartial("PartialUI.py")
}
