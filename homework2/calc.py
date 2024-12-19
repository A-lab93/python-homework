num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Enter the operation (+, -, *, /): ") 

def add(num1, num2):
    return num1+num2
def sub(num1, num2):
    return num1-num2
def mult(num1, num2):
    return num1*num2
def div(num1, num2):
    return num1/num2

print("Result:")
if op=="+":
    print(f"{num1} + {num2} =", round(add(num1,num2)))
elif op=="-":
    print(f"{num1} - {num2} =",round(sub(num1,num2)))
elif op=="*":
    print(f"{num1} x {num2} =",round(mult(num1,num2)))
elif op=="/":
    print(f"{num1} : {num2} =",round(div(num1,num2)))
else:
    print("Enter the operation '+', '-', '*', '/' ")
print()