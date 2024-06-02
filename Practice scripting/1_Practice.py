# list of anagram indexes in a given list
"""
input = ['god','dog','cat','act','tac']
output = {'dgo': [1, 2], 'act': [3, 4, 5]}
""" 
def Anagram_in_list(list):
    dict = {}
    for i in range(len(list)):
        word = ''.join(sorted(list[i]))
        if word not in dict:
            dict[word] = [i+1]
        else:
            dict[word].append(i+1)
    return dict

if __name__ == "__main__":
    list = ['god','dog','cat','act','tac']
    print(Anagram_in_list(list))