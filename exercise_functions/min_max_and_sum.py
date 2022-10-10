def minimum(sequence):
    return min(sequence)

def maximum(sequence):
    return max(sequence)

def summ(sequence):
    return sum(sequence)

numbers = list(map(int, input().split()))

print(f"The minimum number is {minimum(numbers)}")
print(f"The maximum number is {maximum(numbers)}")
print(f"The sum number is: {summ(numbers)}")
