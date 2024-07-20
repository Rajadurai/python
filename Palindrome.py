
#Write one function in python to check whether we can form any palindrome string from the input or not.
#sample input to the function: 
#1st input  "aabbccde"
#2nd input  "aabbccd"

def isPalindrome(s1,s2):
    s3 = s1+s2[::-1]
    print(s3)
    return s3
    


print("String Palindrome")
print("=================")
print("")

value1 = input("Enter the string name 1: ")
value2 = input("Enter the string name 2: ")
result = isPalindrome(value1,value2)
print 
if result:
    print("yes")
else:
    print("no")