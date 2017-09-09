# order of execution
# 1. exponent (3 ** 2)
# 2. division and multiplication are in the same order.
#   The first from left is executed first (10/5)
# 3. Adding and subtracting are last
print(20 - 10/5 * 3 ** 2)
# Add brackets to change default order
print((20 - 10) / (5 * 3 ** 2))
