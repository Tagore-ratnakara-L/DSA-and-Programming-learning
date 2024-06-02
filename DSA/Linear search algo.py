# finding the element in array Linear incremented index way
def Linear_search(array,element):
    for i in array:
        if element == i:
            return array.index(i)
    return -1 # search element not found

# finding the element in array reverse decremented index way
def Linear_search1(array,element):
    for i in range(len(array),0,-1):
        # print(array[i-1])
        if array[i-1] == element:
            return array.index(element)
        
    return -1 # search element not there


if __name__ == "__main__":
    array = [3,6,8,9,5,4,2]
    element = 13
    result1 = Linear_search(array,element)
    result2 = Linear_search1(array,element)
    if result1==-1 and result2==-1:
        print("No such Element found")
    else:
        print(result1)

