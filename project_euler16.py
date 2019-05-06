sum = 0
num = 2 ** 1000
while num != 0:
	rem = num % 10
	sum += rem
	num //= 10
print(sum)
