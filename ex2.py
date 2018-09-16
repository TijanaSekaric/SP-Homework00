
def sum_of_the_squares(n):
    n -= 1
    sum = 0
    while n > 0:
        sum += n * n
        n -= 1
    return sum

print(sum_of_the_squares(3))