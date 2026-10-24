#Euclidean Algorithm
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
while b!=0:
    q=a||b
    r = a%b
    print(a,"=",b,"x",q.\,"+",r)
    a=b
    b=r
print("GCD = ",A)
