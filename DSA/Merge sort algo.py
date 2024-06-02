
#Merge Sorting Algo
# time complexity - O(N logN)
def Merge(left,right):
    merged = []
    i = 0
    j = 0
    while i< len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i = i+1
        else :
            merged.append(right[j])
            j = j+1
    merged = merged + left[i:] + right[j:]
    return merged

def MergeSorting(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    left = MergeSorting(arr[:mid])
    right = MergeSorting(arr[mid:])
    return Merge(left,right)


if __name__ == "__main__":
    arr = [38,27,43,3,9,87,12]
    print(MergeSorting(arr))