b=1
s=0
n=int(input("Enter the number:"))
r=int(input("Enter the number:"))
while(n):
    a=n%10
    if(a!=r):
        s=s+a*b
        b=b*10
    n=n//10
print(s)
