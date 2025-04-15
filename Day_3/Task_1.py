import re

def is_palindrome(s: str) -> bool:
    s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal, Panama")) 
print(is_palindrome("Hello"))