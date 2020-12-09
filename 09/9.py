import copy
import requests

alver = requests.get('https://julekalender-backend.knowit.no/challenges/9/attachments/elves.txt').text.split('\n')[:-1]

def naboer(y, x):
    nm = [[alver[i][j] if  i >= 0 and i < len(alver) and j >= 0 and j < len(alver[0]) else 0
                for j in range(x-1, x+2)]
                    for i in range(y-1, y+2)]
    return [nm[0][1], nm[1][0], nm[1][2], nm[2][1]]

for i, row in enumerate(alver):
    alver[i] = list(row)
    
done = False
counter = 0
while not done:
    indices = []
    for row in alver:
        indices.append([i for i, ltr in enumerate(row) if ltr == 'F'])

    dagens_alver = copy.deepcopy(alver)
    done = True
    for y, row_indexes in enumerate(indices):
        for x in row_indexes:
            if naboer(y, x).count('S') >= 2:
                dagens_alver[y][x] = 'S'
                done = False
    
    alver = copy.deepcopy(dagens_alver)
    counter += 1
print(counter)