# Enter three numbers in the same line and the average is printed 
num1,num2,num3 = map(int,input().split(" "))
sum = num1 + num2 + num3
avg = sum / 3
print(avg)
