str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
abc = {"a":"c", "b":"d", "c":"e", "d":"f", "e":"g", "f":"h", "g":"i", "h":"j", "i":"k", "j":"l", "k":"m", "l":"n", "m":"o", "n":"p", "o":"q", "p":"r", "q":"s", "r":"t", "s":"u", "t":"v", "u":"w", "v":"x", "w":"y", "x":"z", "y":"a", "z":"b"}

lista = str.split()

while len(lista) != 0:
  lista1=[]
  lista2=""
  a = lista.pop(0)
  for x in a:
    if x.isalpha():
      lista2 += abc[x]
    else:
      lista2 += x
  lista1.append(lista2)
  z = " ".join(lista1)
  print(z)




int= "abcdefghijklmnopqrstuvwxyz"
ont="cdefghijklmnopqrstuvwxyzab"

sre = str.maketrans(int, ont)
sri= str.maketrans(abc)

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(str.translate(sre))
print(str.translate(sri))