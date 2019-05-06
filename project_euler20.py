def factorial(n):
	return n * factorial(n - 1)
p = factorial(100)
while(p != 0):
	rem = p % 10
	sum = sum + rem
	p = p // 10
print(sum)
