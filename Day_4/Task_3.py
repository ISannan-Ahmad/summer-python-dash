def is_anagram(s : str, t : str) -> bool:
    
    s = ''.join(sorted(s))
    t = ''.join(sorted(t))

    if s == t:
        return True    

    return False

print(is_anagram("hello", "hlelo"))