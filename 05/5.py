import numpy as np
import requests

moves = requests.get('https://julekalender-backend.knowit.no/challenges/5/attachments/rute.txt').content.decode()
possible_moves = {
    'O': [-1, 0],
    'H': [0, 1],
    'N': [1, 0],
    'V': [0, -1]
}
edges = [(0, 0)]
for move in moves:
    edges.append(np.add(edges[-1], possible_moves[move]))

area = 0.5 * abs(sum(x0*y1 - x1*y0 for ((x0, y0), (x1, y1)) in zip(edges, edges[1:] + [edges[0]])))
print(area)