import sys

scores = list(map(int, sys.argv[1:])) if len(sys.argv) > 1 else list(map(int, input("Enter scores separated by space: ").split()))

if not scores:
    raise ValueError("Enter at least one score")

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)