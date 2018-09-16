
def sum_of_squares2(n):
    return sum([k * k for k in range(0, n) if k % 2 != 0])


print(sum_of_squares2(8))
