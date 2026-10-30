scores = list(map(int, input("Enter scores separated by space: ").split()))

total = sum(scores)
average = total / len(scores)

print("Sum of scores:", total)
print("Average of scores:", average)