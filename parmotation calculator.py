def factorial(a):
    fact=1
    if a==0:
        return fact
    else:
        for i in range(1,a+1):
            fact=fact*i
        return fact
    
print("calculetor : nPr \ n")
n=int(input('Enter the value of n :'))
r=int(input('Emter the valueof r :'))
if n<r:
    print('\nMath Error')
else:
    result=factorial(n)/factorial(n-r)
    print('\n{}P{} is{}'.format(n,r,result))