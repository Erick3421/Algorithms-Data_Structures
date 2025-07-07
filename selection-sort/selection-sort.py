def searchSmaller(arr):
    lower = arr[0]
    lower_index = 0

    for i in range(1, len(arr)):
        if arr[i] < lower:
            lower = arr[i]
            lower_index = i
    
    return lower_index

def selectionSort(arr):
    new_array = []

    for i in range(len(arr)):
        menor = searchSmaller(arr)
        new_array.append(arr.pop(menor))
    
    return new_array

array = [5,3,6,2,10]

print(selectionSort(array))