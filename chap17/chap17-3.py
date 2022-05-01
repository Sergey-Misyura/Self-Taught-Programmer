# 3
import re

line = 'Привидение прошуршало и исчезло в углу.'

m = re.findall("\w*ло",
               line,
               re.IGNORECASE)

m2 = re.findall(".ло",
               line,
               re.IGNORECASE)
print(m, m2)