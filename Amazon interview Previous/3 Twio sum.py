# finding the sum of two elements in gven list by target
def TwoSum(nums,target):
    dict_nums = {}
    for idx,num in enumerate(nums):
        dict_nums[num] = idx
    
    for idx,num in enumerate(nums):
        if (target - num in dict_nums) and (idx != dict_nums[target-num]):
            return [idx,dict_nums[target-num]]
        
"""
T = O(N)
S = O(N)
"""
if __name__ == "__main__":
    nums = [3,2,4]
    target = 7
    print(TwoSum(nums,target))



