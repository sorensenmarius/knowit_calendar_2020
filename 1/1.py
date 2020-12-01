import numpy as np
import requests

r = requests.get("https://julekalender-backend.knowit.no/challenges/1/attachments/numbers.txt")
data = r.content

data = np.sort(np.fromstring(data, dtype=np.int, sep=','))

for i, num in enumerate(data):
    if(num != i + 1):
        print(num - 1)
        break