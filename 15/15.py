import requests

ordbok = requests.get('https://julekalender-backend.knowit.no/challenges/15/attachments/wordlist.txt').text.split('\n')
ordpar = requests.get('https://julekalender-backend.knowit.no/challenges/15/attachments/riddles.txt').text.split('\n')

limord = set()
for par in ordpar[:-1]:
    start, slutt = par.split(', ')
    start_filter = filter(lambda x: x.startswith(start), ordbok)
    for o in list(start_filter):
        o = o[len(start):]
        if o + slutt in ordbok and o in ordbok:
            limord.add(o)

teller = 0
for o in limord:
    teller += len(o)

print(teller)