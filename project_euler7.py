li = [2]
def is_prime(n):
	c = 0
	for i in range(1,n + 1):
		if(n % i == 0):
			c += 1
	if c == 2:
		return True
	return False 
def nth_prime(num):
	c = 0
	for i in range(1, 100):
		if(is_prime(i)):
			c += 1
		if c == num:
			return i
			break	
print(nth_prime(10001))
