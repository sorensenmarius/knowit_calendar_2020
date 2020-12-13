import requests

bokstaver = list(requests.get('https://julekalender-backend.knowit.no/challenges/13/attachments/text.txt').text)

teller = {}
for i, c in enumerate(bokstaver):
    if c not in teller:
        teller[c] = 0
    teller[c] += 1

    if teller[c] != (ord(c) - 96):
        bokstaver[i] = ''

for i, c in enumerate(bokstaver):
    if c == '':
        continue

    if teller[c] < (ord(c) - 96):
        bokstaver[i] = ''

print(''.join(bokstaver))