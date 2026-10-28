def palindrome(x):
    x = str(x)
    return x == x[::-1]
print(palindrome("madam"))
print(palindrome(121))