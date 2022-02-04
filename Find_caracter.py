
stra = "abcdddffffffffd"

asd = {}

for x in stra:
    total = stra.count(x)
    asd[x]= asd.get(x,0) + 1

print(asd)