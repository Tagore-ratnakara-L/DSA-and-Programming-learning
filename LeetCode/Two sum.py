# two sum 
def Two_sum(array,x):
    hash_map = {}
    for idx,ele in enumerate(array):
        if ele in hash_map:
            return [hash_map[ele],idx]
        
        b = x-ele
        hash_map[b] = idx



if __name__ == "__main__":
    array = [2, 4, 6, 7, 12, 13, 14] #[2,4,5,7,12,13,14]
    array1 = sorted(array) # O(nlogn) [2, 4, 5, 7, 12, 13, 14] 
    x = 25
    print(Two_sum(array,x))
