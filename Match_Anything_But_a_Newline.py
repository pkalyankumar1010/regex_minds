# 
# Task
# 
# You have a test string S .
# Your task is to write a regular expression that matches only and exactly strings of form: abc.def.ghi.klm , where each variable of S can be any single character except the newline.


regex_pattern = r"^.{3}\..{3}\..{3}\..{3}$"

import re
import sys

test_string = input()

match = re.match(regex_pattern,test_string) is not None


print(str(match).lower())
