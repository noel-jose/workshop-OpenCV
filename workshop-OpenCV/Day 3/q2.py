#program checks if a string is palindrome or not
string = input("Enter a string \n")
if(string[::-1] == string):
    print("Palindrome")
else :
    print("Not palindrome")