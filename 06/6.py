import requests
import numpy as np
pakker = list(map(int, requests.get('https://julekalender-backend.knowit.no/challenges/6/attachments/godteri.txt').content.decode().split(',', )))

totale_biter = sum(pakker)

alver = 127

for pakke in pakker[::-1]:
    if (totale_biter - pakke) % alver != 0:
        totale_biter -= pakke
    else:
        break

print(totale_biter // alver)