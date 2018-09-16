

def minmax(data):
    largest = data[0]
    smallest = data[0]
    for i in data:
        if i > largest:
            largest = i
        elif i < smallest:
            smallest = i
    return smallest, largest


date = [1, 8, 16, 44, 5, 5, 7, 100, 9]

print(minmax(date))
