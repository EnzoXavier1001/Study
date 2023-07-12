emojis = "👿👹👺🤡👽👾🤖"
codes = []

for emoji in emojis:
    codes.append(ord(emoji))

print(codes)
print(chr(codes[4]))  # por conta do retorno do ord()

# Outra forma
codes = [ord(emoji) for emoji in emojis]
# pega um emoji e percorre como emoji a lista emojis

print(codes)
print(chr(codes[4]))  # por conta do retorno do ord()

####################################

team = ['Rebeca', 'Tomas', 'Stefan', 'Sindy', 'Donald']
dream_team = [name for name in team if name[0] == 'S']
print(dream_team)
