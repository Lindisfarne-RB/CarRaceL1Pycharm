'''1/1! + 2/2! + 3/3! + 4/4! +'''
'''
def fact(x):
    i=1
    factorial =1
    while(i<=x):
        factorial = factorial *i
        i+=1
    return factorial

i=1
sum=0
n=int(input("Enter n"))
while(i<=n):
    p=fact(i)
    term = i / p
    sum +=term
    i+=1
print(sum)
'''

#1 + 2*2 +3*3*3

i=1
p=1
sum=0
n=int(input("Enter n"))
while(i<=n):
    p=1
    j=1
    while(j<=i):
        p=p*i
        j+=1
    i+=1
    sum =sum +p
print(sum)


numofrounds=5
numofrounds = str(numofrounds)
if numofrounds.isdigit() == True:
    print("valid")
else:
    print("invalid")