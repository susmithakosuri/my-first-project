sum = 0
count = 0
for i in range(1, 2000000):
	count = 0
	for j in range(1, i + 1):
		if i % j is 0:
			count += 1
	if count == 2:
		sum += i
print(sum)
