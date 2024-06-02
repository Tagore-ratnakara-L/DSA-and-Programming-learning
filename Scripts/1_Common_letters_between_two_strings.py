def Common_letters():
    str1 = str(input("Enter first String: "))
    str2 = str(input("Enter second String: "))
    s1 = set(str1)
    s2 = set(str2)
    lst = s1 & s2
    print(lst)
    # result_string = list(s1.intersection(s2))
     
    # print(result_string)
if __name__ == '__main__':
    Common_letters()
