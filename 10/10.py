import requests

leker = requests.get('https://julekalender-backend.knowit.no/challenges/10/attachments/leker.txt').text.split('\n')
poeng = {}

for lek in leker:
    lek = lek.split(',')
    for plassering, alv in enumerate(lek):
        if alv not in poeng:
            poeng[alv] = 0
        poeng[alv] += len(lek) - (plassering + 1)

vinner = max(poeng, key=poeng.get)

print(f'{vinner} vant med {poeng[vinner]} poeng')