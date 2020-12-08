import requests

data = requests.get('https://julekalender-backend.knowit.no/challenges/8/attachments/input.txt').text.split('\n')

steder = {}
teller = {}
for sted in data[:50]:
    s = sted.split(': ')
    koordinater = (int(s[1].split(', ')[0][1:]), int(s[1].split(', ')[1][:-1]))
    steder[s[0]] = koordinater
    teller[koordinater] = 0

def lengde(fra, til):
    return abs(fra[0] - til[0]) + abs(fra[1] - til[1])

def legg_til_sekunder(current):
    for koord in teller:
        l = lengde(current, koord)
        if l == 0:
            teller[koord] += 0
        elif l < 5:
            teller[koord] += 0.25
        elif l < 20:
            teller[koord] += 0.5
        elif l < 50:
            teller[koord] += 0.75
        else:
            teller[koord] += 1

def gå_til_sted(fra, navn):
    til = steder[navn]

    x, y = fra
    while x != til[0]:
        x += 1 if til[0] - x > 0 else -1
        legg_til_sekunder((x, y))
    
    while y != til[1]:
        y += 1 if til[1] - y > 0 else -1
        legg_til_sekunder((x, y))

    return(til)

current = (0, 0)
for sted in data[50:-1]:
    current = gå_til_sted(current, sted)

print(max(list(teller.values())) - min(list(teller.values())))