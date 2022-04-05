import re

def validity(password):
    pattern="(.*(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$]).*){6,12}"
    res=re.search(pattern,password)
    if res :
        return True
    else:
        return False

#username=input('Enter your username : ')
password=input('Enter your password : ')

print(validity(password))