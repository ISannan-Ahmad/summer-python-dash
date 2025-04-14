def find_missing(list : list, n : int) -> int:
    
    expected_sum = n * (n + 1) // 2    
    return expected_sum - sum(list)


print(find_missing([1,4,2,5,8,6,7], 8))