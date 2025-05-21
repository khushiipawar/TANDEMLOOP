def count_multiples(numbers):
    counts = {}
    for num in numbers:
        for i in range(1, 10):
            if num % i == 0:
                if i in counts:
                    counts[i] += 1
                else:
                    counts[i] = 1
    return counts

# Accepting user input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Calling the function and printing the result
result = count_multiples(numbers)
print(result)
