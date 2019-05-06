def prime(num):
	if num == 2 or num == 3:
		return true
	if(num % 2 == 0):
		return False
	for i in range(5,num):
		if(num % i == 0):
			return False
		return True
li = []
num2 = 13195
def fact():
	for k in range(2,num // 2):
		if(prime(k)):
			if(num2 % k == 0):
				li.append(k)
print(li)
