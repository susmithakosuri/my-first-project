sum = 0
a = 1
b = 2
c = 0
while (c < 4000000):
	c = a + b
	if c % 2 is 0:
		sum += c
		print(sum + 2)
	a = b 
	b = c
