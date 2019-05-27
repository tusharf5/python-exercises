def is_multiple(n, m):
    print(n, ' is a multiple of ', m)
    if n % m == 0:
        return True
    return False


print(is_multiple(1, 9))
print(is_multiple(10, 2))
print(is_multiple(999, 2))
print(is_multiple(333, 3))
print(is_multiple(123123, 7))
