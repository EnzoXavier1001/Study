import requests

# Utilizando API => http://open-notify.org/Open-Notify-API/
info = requests.get('http://api.open-notify.org/astros.json')

dado_01 = info.text
dado_02 = info.json()

# print(type(dado_01))
# print(dado_01)

print(type(dado_02))
print(dado_02)

