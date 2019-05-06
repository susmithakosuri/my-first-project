sum = 0
for i in range(100,1000):
	for j in range(100,1000):
		product = i * j
		if is_palin(product):
		
		
			rem = product % 10
			sum = (sum * 10) + rem
			product /= 10
		if sum == res:
			print(sum)
