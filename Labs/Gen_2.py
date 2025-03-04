def even_numbers_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())
print(", ".join(map(str, even_numbers_generator(n))))
