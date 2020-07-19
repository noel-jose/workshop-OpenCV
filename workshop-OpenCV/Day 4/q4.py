#pogram prints the element in list1 if it is present in list2 in the same index
list1 = ["oranges","pineapple","mango","apple","bananas"]
list2 = ["oranges","dates","mango","grapes","jackfruit"]
for i,j in zip(list1,list2):
    if i  == j :
        print(i)