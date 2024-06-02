#Selection sorting of Array 
def Selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1,len(array)):
            if array[j] < array[min_index]:
                min_index = j

        # swap 2 elements
        array[i] , array[min_index]  = array[min_index], array[i]


if __name__ == "__main__":

    array = [6,2,4,5,7,8,1,9,0,3]
    Selection_sort(array)
    print(array)