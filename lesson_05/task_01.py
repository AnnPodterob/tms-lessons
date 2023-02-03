def is_palindrome(string: str):
    reversed_string = ''.join(reversed(string))
    if reversed_string == string:
        print(string, "is Palindrome")
    else:
        print(string, "Not a Palindrome")


is_palindrome('python')
is_palindrome('hihiihih')
