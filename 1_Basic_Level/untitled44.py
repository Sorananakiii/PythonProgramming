
# Filtering with Lambda Functions
nums = list(range(100))
filtered = filter(lambda x: x % 3 == 0 or x % 7 == 0, nums)
print([*filtered])