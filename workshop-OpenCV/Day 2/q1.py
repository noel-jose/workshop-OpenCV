#program reads three numbers and prints the average
print("Enter three numbers")
num1,num2,num3 = map(int,input().split())
sum = num1 + num2 + num3
avg = sum / 3
print(avg) 
