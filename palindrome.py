#This code will check whether a given word is a palindrome or not.

def palindrome(x):
    x = x.lower()
    y = x[::-1]
    if x==y:
        print("Palindrome!")
    else:
        print("Not Palindrome")
        
#Sethu C A "Start calling youself to be a beginner in learning programming when you write a code to identify palindromes.":)
