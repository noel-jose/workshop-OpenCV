# prints FIZZ for multiples of 2 and BUZZ for multiples of 7
count = 0
for i in range(1,101):
    if i % 2 == 0 :
        print("Fizz",end = "")
        count = 1
    
    if i % 7 == 0 :
        print("Buzz",end = "")
        count = 1

    if count == 0:
        print(i,end = "")
    
    count = 0
    print(end = ", ")
    