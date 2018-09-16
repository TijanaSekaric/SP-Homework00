
def sum_of_squares2(n):
    n -= 1
    sum = 0
    while n > 0:
        if n % 2 != 0:
            sum += n * n
        n -= 1
    return sum

print(sum_of_squares2(8))
