import datetime as data

data_today = data.datetime.today()
data_formated = data_today.strftime('%d-%m-%Y')

print(data_today)
print(data_formated)

print(' * ---------------------------- * ')

import re

text = 'aula_pythone1-01-2020.py'
result = re.search('[a-z_]*', text)
text_founded = result.group()

print(result)
print(text_founded)