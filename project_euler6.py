sum1 = 0
sum2 = 0
diff = 0
for i in range(101):
	product1 = i ** 2 
	sum1 += product1
	sum2 += i
product2 = sum2 *sum2
print(product2 - sum1)
