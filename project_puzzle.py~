n = int(input())
a = []
for k in range(3):
	for i in range(n):
 		a.append(input())
	print("enter directions")
	li = [x for x in input()]
	c = 0
	for i in range(n): 	
 		for j in range(n):
 			for d in li:
 				if c != 1:
 					if a[i][j] != 'z':
 						if a[i][j] == ' ':
 							if d == 'r':
 								a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]
 								i, j = i, j + 1
 							if d == 'l':
 								a[i][j], a[i][j - 1] = a[i][j - 1], a[i][j]
 								i, j = i, j - 1
 							if d == 'a':
 								a[i][j], a[i - 1][j] = a[i - 1][j], a[i][j]
 								i, j = i - 1, j
 							if d == 'b':
 								a[i][j], a[i + 1][j] = a[i + 1][j], a[i][j]
 								i, j = i + 1, j
 							if i == 5 or j == 5 or i < 0 or j < 0:
 								print("this puzzle has no final configuration.")
 								c = 1
 							if (d == '0'):
 								print("print #", k + 1, ":")
 								for i in range(n):
 									for j in range(n):
 										print(a[i][j], end = "")
 									print()
 									c = 1
 					else:
 						break							
