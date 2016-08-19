# Config Rule:
#     1. The key name should be uniq
#     2. Support dict, array, and basic type only

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
        {
            Const.Script: "scripts/Test.py"
        }]
    }
}
