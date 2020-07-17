#program to find the largest of two numbers entered by the user 
print("Enter two numbers")
num1,num2 = map(int,input().split())
if num1 > num2 :
    print(num1," is largest")
else :
    print(num2," is largest")