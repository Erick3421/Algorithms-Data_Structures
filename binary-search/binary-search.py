import math

def binary_search(list_itens, target):
    lower = 0;
    upper = len(list_itens) - 1;

    while lower <= upper:
        mid = math.floor((lower + upper) / 2)
        guess = list_itens[mid]

        if guess == target:
            return mid
        if guess > target:
            upper = mid - 1
        else:
            lower = mid + 1
    return -1

my_list = [1,3,5,7,9]
search = binary_search(my_list, 3)
print(search)