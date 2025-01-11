xd = [0,1,2,3,4,5,-5,6,7,8,9,72,72,72]
legnagyobbak = []
max_resztvevo = 0

for sor in xd:
    if sor > max_resztvevo:
        max_resztvevo = sor
        legnagyobbak = []
    if sor == max_resztvevo:
        legnagyobbak.append(sor)
