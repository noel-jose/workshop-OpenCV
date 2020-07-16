""" 
print the pattern 
       *
      ***
     *****
"""
num = 2
for i in range(1,6,2):
    print(" " * num,"*" * i)
    num = num - 1