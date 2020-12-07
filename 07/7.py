# Lang og stygg men den er min <3
skog = open('skog.txt', 'r')

skog = skog.read().split('\n')[::-1][1:]

def sjekk_tre(i):
    for j in range(35):
        denne = skog[j][i - 1 : i + 2]

        if denne == ' # ' and j > 2:
            return True
        
        if not sjekk_grein(i, j):
            return False

def sjekk_grein(i, j):
    grein_lengde = 1
    siste = "#"
    while True:
        if siste == ' ' and skog[j][i - grein_lengde] == ' ' and skog[j][i + grein_lengde] == ' ':
            return True

        if skog[j][i - grein_lengde] != skog[j][i + grein_lengde]:
            return False

        siste = skog[j][i - grein_lengde]
        grein_lengde += 1

teller = 0
for i, tegn in enumerate(skog[0]):
    if tegn == '#' and sjekk_tre(i):
        teller += 1

print(teller)