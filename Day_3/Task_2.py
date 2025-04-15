def largest_prime(n: int) -> int:
    for num in range(n, 1, -1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            return num
    return None

print(largest_prime(20))
