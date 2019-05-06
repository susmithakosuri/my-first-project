#num = int(input())
#li = [x for x in range(12, 90) if(x % 10) > (x // 10)]
#print(li)
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'july', 'aug', 'sep', 'oct', 'nov', 'dec']
print([x for x in months if months.index(x) % 2 == 0])

