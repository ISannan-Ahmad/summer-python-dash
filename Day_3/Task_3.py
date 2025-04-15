def second_largest(lst: list[int]) -> int | None:
    if len(lst) < 2:
        return None

    first = second = float('-inf')

    for num in lst:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second if second != float('-inf') else None