Regex_Pattern = r"(\d{2}[^\d]){2}\d{4}"

import re

print(str(bool(re.search(Regex_Pattern,input()))).lower())
