sum = 1
fac_count = 0
for i in range(2, 12376):
	sum = sum + i
	for j in range(1,i+1):
		if(sum % j == 0):
			fac_count += 1
if fac_count > 500:
		print(sum)
