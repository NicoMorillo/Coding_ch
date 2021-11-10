def solve(dep):
    dic= {}
    for x in dep:
        dic[x] = 0
    for i in dep:
        dic[i] += 1


    v = list(dic.values())
    k = list(dic.keys())
    
    print (k[v.index(max(v))], max(v))













solve(["Matematicas","Lengua","Ingles","E.F.", "Lengua"])