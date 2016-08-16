import sys
import logging
sys.path.append("..")

from SchemaChecker import *

checker = SchemaChecker("Config.py", "Schema.py", "Const.py")
if checker.Check():
    print "Check successfully"
else:
    print "Check failed"

