combo = []
c = 0
for a in range(2,101):
    for b in range(2,101):
        c = a**b
        if combo.count(c)<1:
            combo.append(c)

print len(combo)
