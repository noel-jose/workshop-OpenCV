#program finds the factorial of a number using recursion
fact = 1
def factorial(num):
    global fact 
    fact = fact * num
    num = num - 1 
    if num == 1 :
        print(fact)
    else :
        factorial(num)
num = int(input("ENter a number \n"))
factorial(num)