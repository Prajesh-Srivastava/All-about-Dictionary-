n=int(input('how many key u want to input '))
a={}
for i in range(n):
    a[input('enter the key ')]= input('enter the value ')
print(a)
w=input('enter the key to serch the phone no. ')
print(w,end=' = ')
d=a.get(w,'Not Found')
print(d)
    
