n=int(input())
count=int(input())
s=str(n)
l=len(s)
print(l)
li=[]
def valid(num):
    if(int("".join(sorted(str(num))))==num):
       return 1
    return 0
li=[i for i in range(10**(l-1), 10**l) if valid(i)]
print(li)
a=li.index(n)
def prev_num(li,a):
    print(li[a-1])
def next_num(li,a):
    if(a == len(li)-1):
        print(li[0])
    else:
        print(li[a+1])
def nth_next(count,li,a):
    print(li[a+count])
def nth_prev(count,li,a):
    if((a+count) > len(li)):
        print(li[count-(len(li)-a)])
    else:
        print(li[a-count])
def diff(m,n):
    return li.index(n)-li.index(m)
prev_num(li,a)
next_num(li,a)
nth_next(count,li,a)
nth_prev(count,li,a)
