import re 
def validtest(string):

    e_format=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    #comparing user email with the format
    if(re.match(e_format,string)):
        print("valid email")
    else:
        print("invalid email")  


string=input("enter a email: ")

validtest(string)