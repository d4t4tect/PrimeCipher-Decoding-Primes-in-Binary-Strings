import time


def is_valid_binary(binary_str):
    """Check if the string contains only '0' and '1'."""
    for char in binary_str:  # Avoid set creation overhead
        if char not in '01':
            return False
    return True


def check_prime(num, prime_cache):
    """Determine if a number is prime with caching."""
    if num in prime_cache:
        return prime_cache[num]
    if num < 2:
        prime_cache[num] = False
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime_cache[num] = False
            return False
    prime_cache[num] = True
    return True


def find_prime_substrings(binary_str, N):
    """Find unique prime numbers from binary substrings less than N efficiently."""
    if not is_valid_binary(binary_str):
        return "0: Invalid binary strings"

    n = len(binary_str)
    unique_primes = set()
    prime_cache = {}  # Cache for primality results
    max_len = 0

    # Early exit: find max substring length where value < N
    for i in range(n, 0, -1):
        if int('1' * i, 2) < N:
            max_len = i
            break
    if max_len == 0:
        return "0: "

    # Incremental decimal calculation
    for start in range(n):
        curr_num = 0
        for length in range(1, min(max_len + 1, n - start + 1)):
            # Update current number incrementally
            curr_num = (curr_num << 1) + (ord(binary_str[start + length - 1]) - ord('0'))
            if curr_num >= N:
                break
            if check_prime(curr_num, prime_cache):
                unique_primes.add(curr_num)

    primes = sorted(unique_primes)
    if len(primes) < 6:
        return f"{len(primes)}: {','.join(str(p) for p in primes)}"
    else:
        return f"{len(primes)}: {','.join(str(p) for p in primes[:3])},...,{','.join(str(p) for p in primes[-3:])}"


# Input handling
print("Enter a binary string (containing only 0s and 1s):")
binary_input = input().strip()

print("Enter the upper limit N (a positive integer):")
while True:
    try:
        N_input = int(input().strip())
        if N_input > 0:
            break
        print("Please enter a positive integer:")
    except ValueError:
        print("Please enter a valid integer:")

# Process with timeout check
print("\nProcessing Input:")
print(f"Input: {binary_input}, {N_input}")
start = time.time()
result = find_prime_substrings(binary_input, N_input)
end = time.time()

print(f"Output: {result}")
print(f"Running time: {end - start:.6f} seconds")
print("_" * 100)