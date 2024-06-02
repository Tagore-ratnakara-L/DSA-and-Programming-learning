def Anagram_list(list1):
    dict = {}
    
    for str1 in list1:
        s= "".join(sorted(str1))
        if s in dict:
            dict[s].append(str1)
        else:
            dict[s]= [str1]
    print(list(dict.values()))

if __name__ == "__main__":
    list1 = ['eat','ate','tea','bat','tab']
    Anagram_list(list1)