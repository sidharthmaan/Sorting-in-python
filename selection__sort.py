
def selection_sort(list_a):
    indexing_length = range(0, len(list_a) - 1)
    for i in indexing_length:
        min_value = i
        for j in range(i+1, len(list_a)):
            if list_a[min_value] > list_a[j]:
                min_value = j

        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

    return list_a

print(selection_sort([2,3,6,4,5,9,7,8,1,0])) 