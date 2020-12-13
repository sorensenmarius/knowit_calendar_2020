import requests

familie = requests.get('https://julekalender-backend.knowit.no/challenges/12/attachments/family.txt').text.split(' ')

gen = 0
teller = {}
for person in familie:
    if '(' in person:
        gen += 1
    
    if gen not in teller:
        teller[gen] = 0
    teller[gen] += 1

    gen -= person.count(')')

print(max(teller.values()))