
def BinarySearch(array,x,low,high):
    sorted_array = sorted(array)
    # print(sorted_array) # [0, 1, 2, 3, 4, 5, 7, 7, 8, 9, 12, 14, 22, 34]
    while low <= high: # low = 0  and high = len(array) 
        mid = low+(high-low) //2 # mid = 6 "0+(13-0)//2"" 
        # sorted_array[mid] == 12 if "True" it returns mid index 
        # but mid is 7 "False"
        if sorted_array[mid] == x:
            return mid
        elif sorted_array[mid] < x: # mid index value is less then pointer incremented to right from low = 7 "(6+1)""
            low = mid+1 # array becomes in first iteration [7, 8, 9, 12, 14, 22, 34]
        else: # mid index value higher than required element pointer decremented to 1
            high = mid-1 # example : 6-1 = 5
    return -1
# final iteration mid = 7+(13-7)//2 = 10

if __name__ == "__main__":
    array = [1,4,2,5,7,34,12,3,7,8,0,9,14,22]
    x=9
    result = BinarySearch(array,x,0,len(array)-1)
    if result == -1:
        print("No such element found")
    else:
        print(result)