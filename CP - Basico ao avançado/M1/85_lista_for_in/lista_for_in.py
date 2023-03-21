nomes = ["maria", "lucas", "helena"]
c = 0
for i in nomes:
    print(c, i)
    c += 1

nomes = ["maria", "lucas", "helena"]
indices = range(len(nomes))

for i in indices:
    print(i, nomes[i])