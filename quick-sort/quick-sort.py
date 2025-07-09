def qsort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        less_pivo = [i for i in array[1:] if i <= pivo]
        higher_pivo = [i for  i in array[1:] if i > pivo]

    return qsort(less_pivo) + [pivo] + qsort(higher_pivo)

print(qsort([5,2,7,9,3]))