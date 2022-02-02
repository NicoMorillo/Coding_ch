str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
str_list = str.split()
abc = {"a":"c", "b":"d", "c":"e", "d":"f", "e":"g", "f":"h", "g":"i", "h":"j", "i":"k", "j":"k", "k":"m", "l":"n", "m":"o", "n":"p", "o":"q", "p":"r", "q":"s", "r":"t", "s":"u", "t":"v", "u":"w", "v":"x", "w":"y", "x":"z", "y":"a", "z":"b"}


str1=["agh", "fg"]

def descf(lista,cod):
    nw_list=[]
    nw2_list = ""
    for ln in lista:
        z = len(ln)
        if z == 1:
            nw_list += cod[ln]
        else:
            for x in ln:
                nw2_list += cod[x]
    print(nw_list)

descf(str1,abc)

#def descr(q,p):
 # h=[]
  #for x in q:
   # if x.isalpha():
    #  h+=p[x]
    #else:
     # h+=x
  #print(" ".join(h))
#descr(z,abc)