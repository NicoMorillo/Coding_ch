def chec(array):
  lista_1=[]
  lista_2=[]
  lista_3=[]
  lista_4=[]

  for x in array:
    lista_1.append(x.replace(" ","").split(","))
  lista_2 = lista_1[0]
  lista_3 = lista_1[1]
  for z in lista_2:
    if z in lista_3:
      lista_4.append(z)

  fn = ",".join(lista_4)
  print(fn)
    
    


chec(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"])