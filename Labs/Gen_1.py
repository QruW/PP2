def our_range(start, stop):
    result = []
    a = 1
    while start < stop:
        result.append(a)
        start += 1
        a *= a
    return result

print(our_range(1, 10))