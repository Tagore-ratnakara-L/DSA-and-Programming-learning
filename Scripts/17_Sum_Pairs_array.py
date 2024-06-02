# Find out the pairs with given sum value of an array?
def Sum_two(arr,sum):
    arr.sort() # sorting the given Array
    left = 0
    right = len(arr)-1 # len of array = 8 right = 7
    while (left<=right):
        # right array decemented if sum is lesser than total
        if (arr[left]+arr[right]>sum):
            right = right-1
        # left array incremented if sum is greater than total
        elif(arr[left]+arr[right]<sum):
            left=left+1
        # if sum = total the values of certail index will print 
        elif(arr[left]+arr[right]==sum):
            print("Values of pairs are {} & {}".format(arr[left],arr[right]))
            right = right-1
            print(right)
            left = left+1
            print(left)
if __name__ == "__main__":
    arr = [2,3,6,8,7,9,16,19]
    sum = 17
    Sum_two(arr,sum)
    # arr1 = [3,2,4]
    # sum1 = 6
    # Sum_two(arr1,sum1)
    
