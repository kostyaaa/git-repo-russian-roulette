grill = ('X...',
 '..X.',
 'X..X',
 '....')

# размер решетки 4*4. надо определить координаты Х. Их всего 4
# grill - кортеж строк
coords = []
counter = 0
for i in range(0, 4):
    z = grill[i]
    while y != -1:
        y = z.find("X")
        if y != -1:
            coords.append((i, y))
            counter += 1
print(coords, counter)
