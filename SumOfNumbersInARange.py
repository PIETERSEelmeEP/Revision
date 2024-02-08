"""Output the integers from 20 to 25 inclusive and their sum.
"""

for i in range(20, 26):
    print(i)

numbers = list(range(20, 26))
total_sum = sum(numbers)
print("Sum", total_sum)
