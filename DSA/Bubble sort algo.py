def Bubblesorting(array):
    for i in range(len(array)): # travresing the whole array
        for j in range(0,len(array)-i-1):# comparison

            if array[j] > array[j+1]:
                # swap two elements
                array[j],array[j+1] = array[j+1],array[j]
    return array


if __name__ == "__main__":
    array = [1,4,2,5,7,34,12,3,7,8,0,9,14,22]
    result = Bubblesorting(array)
    print(result)