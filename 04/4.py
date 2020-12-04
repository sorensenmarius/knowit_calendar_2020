import requests

kjopsliste = requests.get('https://julekalender-backend.knowit.no/challenges/4/attachments/leveringsliste.txt').content.decode().split('\n')

data = {
    'melk': 0,
    'sukker': 0,
    'mel': 0,
    'egg':0
}

for linje in kjopsliste:
    for entry in linje.split(', '):
        name, value = entry.split(': ')
        data[name] += int(value)

print(min(data['melk']//3, data['sukker']//2, data['mel']//3, data['egg']))