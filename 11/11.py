import requests

hintene = requests.get('https://julekalender-backend.knowit.no/challenges/11/attachments/hint.txt').text.split('\n')[:-1]
passord = 'eamqia'

for hint in hintene:
    historie = []
    for i, _ in enumerate(hint):
        historie.append(list(hint))
        
        hint = historie[i][1:]
        hint = list(map(lambda c: chr((ord(c.lower()) - ord('a') + 1) % 26 + ord('a')) if c.isalpha() else '' , hint))

        for j, c in enumerate(hint):
            hint[j] = chr((((ord(historie[i][j]) + ord(hint[j])) - 2 * ord('a')) % 26) + ord('a'))
    
    for j in range(len(historie[0])):
        if passord in ''.join([rad[j] for rad in historie[:-j]]):
            print(''.join(historie[0]))
            break