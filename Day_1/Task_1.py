def my_max(list : list) -> int:
    max = list[0]
    for num in list:
        if num > max:
            max = num
    return max


print(my_max([1,2,5,12,3,51,23,15,12,3123,1,23,12541,23,1,2,14,212]))
