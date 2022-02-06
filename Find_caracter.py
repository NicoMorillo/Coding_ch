
stra = "abcdddffffffffd"
strm = open ('Level2.txt')
strma = strm.read()

def check(mss):
    asd = {}
    for x in mss:
        total = mss.count(x)
        asd[x]= asd.get(x,0 ) +1
    return(asd)

a = check(strma)

for z,c in a.items():
    if c == 1:
        print(z)