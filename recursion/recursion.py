def increase_recursion(num):
    print(num)

    if num <= 1:
        return
    else:
        increase_recursion(num - 1)

print(increase_recursion(10))


def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x - 1)

print(fat(5))