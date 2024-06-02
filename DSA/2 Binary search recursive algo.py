def BinarySearch(array,x,low,high):
    
    if high >= low:
        mid = low+(high-low)//2

        if array[mid] == x:
            return mid
        elif array[mid] < x:
            return BinarySearch(array,x,mid+1,high)
        else:
            return BinarySearch(array,x,low,mid-1)
    else:
        return -1 # Element not found

if __name__ == "__main__":
    array = sorted([1,4,2,5,7,34,12,3,7,8,0,9,14,22]) # [0, 1, 2, 3, 4, 5, 7, 7, 8, 9, 12, 14, 22, 34]
    x=11
    result = BinarySearch(array,x,0,len(array)-1)
    if result == -1:
        print("No such element found")
    else:
        print(result)