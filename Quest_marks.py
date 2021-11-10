def check(txt):
	z = False
	n_dig = 0
	num_l = []
	if txt.count("?")%3 ==0:
		z = True
	else:
		for x in txt:
			if x.isdigit():
				n_dig += 1
				num_l.append(int(x))
	
		if len(num_l)%2 ==0:
			if sum(num_l)%10 ==0:
				z = True
			else:
				z = False		
		else:
			z = False	
	return z
try1= check("acc?7??sss?3rr1??????5")
print(try1)