# How to reverse words in a string and sentence ?
def Rev_str(str1):
    str1 = str1[::-1]
    return str1

def Rev_string_recursive(str1):
    size = len(str1)
    if (size == 0):
        return str1
    
    last_char = str1[size-1]
    print(last_char,end="")
    Rev_string_recursive(str1[0:size-1])


def Rev_words(str2):
    size = len(str2)
    if(size == 1):
        return str2
    str2=str2.split(" ")
    print(str2)
    i = len(str2)
    rev_word = []
    print(i)
    while i > 0:
        # rev_word.insert(i,str2[i-1])
        rev_word.append(str2[i-1])
        i = i-1
    print(" ".join(map(str,rev_word)))

def Rev_words_1(str3):
    n = len(str3)
    if (n==1):
        return str3
    str3 = str3.split(" ")
    size = len(str3)
    rev_all = ""
    for i in range(size):
        rev = reversed(str3[i])
        print(rev)
        rev_all = rev_all+rev+" "
    print(rev_all)
    print(reversed(rev_all))



if __name__ == "__main__":
    str1 = "SETOinT"
    print(Rev_str(str1))
    print(Rev_string_recursive(str1))
    str2 = "reverse a word in sentence"
    print(Rev_words(str2))
    str3 = "reverse a word in sentence"
    # Rev_words_1(str3)
