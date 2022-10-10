# def sorted_numbers(sequence):
#     results = sorted(sequence)
#     return results
#
# numbers = [int(i) for i in input().split()]
# print(sorted_numbers(numbers))

def sorted_numbers(sequence):
    results = sorted(sequence)
    return results

numbers = list(map(int, input().split()))
print(sorted_numbers(numbers))