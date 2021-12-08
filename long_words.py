def long_word(sen):
  str2 = ""

  for x in sen:
    if x.isalpha() or x == " ":
      str2 +=x

  str2= str2.split()

  maxi = len(str2[0])
  fia = str2[0]

  for z in str2:
    if len(z) > maxi:
      maxi = len(z)
      fia = z

  return(fia)


# keep this function call here 
print(long_word("2sdda aaaa1 baed444  oooo4"))