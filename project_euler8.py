num = 32145
li = []
while num != 0:
	rem = num % 10
	li.append(rem)
	num = num // 10
li2 = li[::-1]
num = len(li2)
for i in range(1,num - 13):
	product = 1
	for j in range(i, i + 13):
		pro = pro * li2[j]
	li3.append[pro]
print(max(li3))
