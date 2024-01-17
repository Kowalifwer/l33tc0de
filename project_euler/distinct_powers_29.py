# https://projecteuler.net/problem=29

# 2 <= a <= 5
# 2 <= b <= 5
# a ^ b
nums = set()
for a in range(2, 101):
    for b in range(2, 101):
        nums.add(a ** b)

print(len(nums))

# EXPECTED_ANS = 9183