#program prints the elements in the first list if it is present in the second list 
list1 = ['India','CHile','SPain','UK','Iran'] 
list2 = ['US','chiLE','spaiN','India','irAn']

for i,j in zip(list1,list2):
    if(i.lower()==j.lower()):
        print(i)
