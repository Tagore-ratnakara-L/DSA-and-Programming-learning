# insertion sort algorithm 

def Insertion_sort(array):
    for i in range(1,len(array),1):
        key = array[i]
        j = i-1

        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key


if __name__ == "__main__":
    array = [9,2,5,3,7,6,8,1,4,0]
    Insertion_sort(array)
    print(array)