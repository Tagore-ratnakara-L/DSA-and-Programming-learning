def merge_the_tools(string, k):
    
    for i in range(0,len(string),k):
        # string iterates to 3 steps 
        list1=[]
        for word in string[i:i+k]:
            # every 3 character sring iterated from 0 to 2 indices
            if word not in list1:
                # appends the word that is not in individual set 
                list1.append(word)
        print("".join(list1))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

"""
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3
"""