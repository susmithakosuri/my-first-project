rows = int(input())
columns = int(input())
a = []
li = []
c = 0
for i in range(rows):
	a.append(input())
print("Across")
for i in a:
	i = i.split('*')
	while '' in i:
		i.remove('')
	for j in i:
		print(j)
print("down")
sum = a[0][0]
for j in range(0,columns):
	sum = a[0][j]
	for i in range(1, rows):
		sum = sum + a[i][j]
	sum = sum.split('*')
	while '' in sum:
		sum.remove('')
	for l in sum:
		print(l)
	
