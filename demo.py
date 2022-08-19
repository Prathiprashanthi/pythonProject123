
p=1000
def myfunc():
    print("welcome")
print("demo module name is:",__name__)
print(dir(p))

n1=int(input("enter the number1:"))
n2=int(input("enter the number2:"))
n3=int(input("enter the number3:"))
if n1>n2 and n1>n3:
    largest =n1
elif n2>n1 and n2>n3:
    largest =n2
else:
    largest =n3
print("Largest among {}{} and {} is {}".format(n1,n2,n3,largest))

