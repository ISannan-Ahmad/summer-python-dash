def reverse_words(s : str) -> str:
    words = s.split(' ')

    return ' '.join(words[::-1])

print(reverse_words("hello world"))