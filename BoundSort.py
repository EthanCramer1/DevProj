def insertion_sort(array, left=0, right=None):

    if right is None:
        
        right = len(array) - 1

    for i in range(left + 1, right + 1):

        key_item = array[i]
        j = i - 1

        while j >= left and array[j] > key_item:

            array[j + 1] = array[j]
            j -= 1

        array [j + 1] = key_item

    return array


def bound_sort(array, bound):

    boundedArray = array[bound[0]:bound[1]+1]
    leftovers = array[bound[1]+1:len(array)]

    sortedBoundedArray = insertion_sort(boundedArray)
    sortedBoundedArray.extend(leftovers)

    sortedUnboundedArray = insertion_sort(array)

    if sortedBoundedArray == sortedUnboundedArray:

        return True

    else:

        return False
    

testArray = [[1, 5, 4, 3, 8, 9],[1, 4, 3, 6, 7, 8],[2, 6, 3, 5, 1, 4, 10]]
testBounds = [0,3]

for i in range(len(testArray)):
    results = bound_sort(testArray[i], testBounds)
    print(results)









