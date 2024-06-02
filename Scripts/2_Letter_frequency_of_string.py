def word_frequency():
    str1 = input("Enter a string :") # hi i am ratna how many times it got repeated how it worked
    Valued_list = str1.split() # <class 'list'>: ['hi', 'i', 'am', 'ratna', 'how', 'many', 'times', 'it', 'got', 'repeated', 'how', 'it', 'worked']
    Empty_dictionary = {} # <class 'dict'>: {'Key' : value ......}
    for i in Valued_list:
        # if i not in Empty_dictionary.keys():
        #     Empty_dictionary[i]=0
        # Empty_dictionary[i]=Empty_dictionary[i]+1

        Empty_dictionary[i]=Empty_dictionary.get(i,0)+1
    print(Empty_dictionary)

if __name__ == '__main__':
    word_frequency()