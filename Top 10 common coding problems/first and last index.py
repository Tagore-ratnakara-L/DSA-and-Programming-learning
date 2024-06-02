# find the first and last index of sorted array of given target
"""
input 
arr = [2,4,5,6,7,7,7,7,9,9]
target = 5
output: [4,6]
"""
# Approach algorithm Linear search
def first_and_last(arr,target):
    for i in range(len(arr)):
        if target == arr[i]:
            start = i
            while i+1< len(arr) and target == arr[i+1]:
                i = i+1
            return [start,i]
    return [-1,-1]

# Approach algorithm Binary search 
def first_and_last_index(arr,target):
    def find_start(arr,target):
        if arr[0] == target:
            return 0
        left,right = 0,len(arr)
        while left<=right:
            mid = (left+right)//2
            if arr[mid] == target and arr[mid-1]<target:
                return mid
            elif arr[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1
    if len(arr) == 0:
        return [-1,-1]
    start = find_start(arr,target)
    if start == -1:
        return [-1,-1]
    end = start
    while end+1 < len(arr) and arr[end+1] == target:
        end +=1
    return [start,end]
        




if __name__ == "__main__":
    arr = [2,4,5,6,7,7,7,7,9,9]
    target = 7
    print(first_and_last(arr,target))