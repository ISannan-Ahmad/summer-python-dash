
def find_pairs(arr: list[int], target: int) -> list[tuple[int, int]]:
    pairs_list = []
    n = len(arr)
    visited = set()
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                pair = tuple(sorted((arr[i], arr[j])))
                if pair not in visited:
                    pairs_list.append(pair)
                    visited.add(pair)
    return pairs_list


print(find_pairs([1, 3, 2, 2, 4, 6, 0], 4))