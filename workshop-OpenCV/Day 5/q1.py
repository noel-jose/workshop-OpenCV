#program finds the sum of elements in a list using a function
def sum(list):
    sum = 0
    for i in list:
        sum = sum + i 
    return sum

list1 = [11,5,17,18,23]
print("Sum of the elements ",sum(list1))
