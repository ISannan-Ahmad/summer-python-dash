def count_frequency(s: str) -> int:
    char_dict = {}

    for idx in s:
        if idx in char_dict:
            char_dict[idx] += 1
        else:
            char_dict[idx] = 1

    return char_dict

def first_unique_char(s : str) -> int:
    freq_dict = count_frequency(s)
    for idx, char in enumerate(s):
        if freq_dict[char] == 1:
            return idx 

    return -1