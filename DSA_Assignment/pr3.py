# Q3. Write a program to check if two strings are a rotation of each other?
def rotation(str1):
    if str1==str1[::-1]:
        return True
    else:
        return False

str1=input("enter your string value ")
print(rotation(str1))

