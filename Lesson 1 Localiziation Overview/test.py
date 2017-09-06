def move(p, motion):
    q = []
    # Spalten verschieben
    for i in range(len(p)):
        r = []
        for n in range(len(p[i])):
            r.append(p[i][(n - motion[1]) % len(p[i])])
        q.append(r)
    # Zeilen verschieben
    r = []
    for i in range(len(q[i])):
        r.append(q[i - motion[0] % len(p[i])])
    return r

p = [[1.1, 1.2, 1.3],
     [2.1, 2.2, 2.3],
     [3.1, 3.2, 3.3]]
motion = [-1,1]

p = move(p, motion)
for i in range(len(p)):
    print(p[i])