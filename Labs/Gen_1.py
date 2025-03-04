def square_generator(n):
    for i in range(n + 1):
        yield i ** 2

n = int(input())
print(list(square_generator(n)))