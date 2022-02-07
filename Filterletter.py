#One small letter, surrounded by EXACTLY 
#three big bodyguards on each of its sides.
import re

ms = open("Level3.txt")
mss = ms.read()

s = "AASSDDFFFCasadasdASSDsasdCVsassSDa"
print(re.findall("[A-Z]{}",s))

#z = re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", mss)
#print("".join(z))      

