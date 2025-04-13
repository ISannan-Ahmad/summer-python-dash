def count_frequency(lst: list) -> int:
    num_dict = {}
    max_freq = 0
    max_freq_num = None

    for idx in lst:
        if idx in num_dict:
            num_dict[idx] += 1
        else:
            num_dict[idx] = 1

    for idx in num_dict:
        if num_dict[idx] > max_freq:
            max_freq_num = idx
            max_freq = num_dict[idx]

    return max_freq_num

result = count_frequency([1,2,3,1,4,12,312,4121,1,1,12,1,21,22,2,1,21,22,2,2,2,2,2,2,1,11,1,1])
print(result) 
