import sys
import logging
sys.path.append("..")

from SchemaChecker import *

checker = SchemaChecker("Config.py", "Schema.py", "Const.py")
checkResult, checkSchema = checker.Check()
if checkResult:
    print "Check successfully"
else:
    print "Check failed"

