def palindrome(a):
    a=a.replace(" "," ")
    if(a==a[::-1]):
        print("Given string is a palindrome")
    else:
        print("Given string is Not a palindrome")

a=input("Enter a string:").lower()
palindrome(a)