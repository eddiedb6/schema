# Config Rule:
#     1. The key name should be uniq
#     2. Support dict, array, and basic type only

{
    Const.UI: {
        Const.Name: "App",
        Const.Type: Const.UIApp,
        Const.Path: "C:/Windows/System32/calc.exe",
        Const.SubUI: [
        {    
            Const.Name: "Desktop",
            Const.Type: Const.AppRoot,
            Const.SubUI: [
            {
                Const.Name: "Main",
                Const.Type: Const.AppForm,
                Const.Caption: "Calculator",
                Const.BreakTime: 2000,
                Const.SubUI: [
                {
                    Const.Name: "1",
                    Const.Type: Const.AppButton,
                    Const.Text: "1"
                },
                {
                    Const.Name: "2",
                    Const.Type: Const.AppButton,
                    Const.Text: "2"
                },
                {
                    Const.Name: "3",
                    Const.Type: Const.AppButton,
                    Const.Text: "3"
                }]
            }]
        }]
    },

    Const.Action: {
        Const.SubAction: [
        {
            Const.Script: "scripts/Test.py"
        }]
    }
}
