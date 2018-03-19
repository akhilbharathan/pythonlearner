#This code will check whether a given world is a palindrome or not.

def palindrome(x):
    x = x.lower()
    y = x[::-1]
    if x==y:
        print("Palindrome!")
    else:
        print("Not Palindrome")
#Call youself to be a beginner in learning any programming when you write a code to identify palindromes.:)
