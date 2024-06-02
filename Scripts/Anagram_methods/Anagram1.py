# Python program to check given strings are anagrams 
# using built in functions
def Anagram_built(str1,str2):
    #converting strings into lower case 
    str1 = str1.lower()
    str2 = str2.lower()
    # check if length is same 
    if len(str1) == len(str2):

        # Sort teh strings
        sort_str1 = sorted(str1)
        sort_str2 = sorted(str2)

        # compare sorted arrays are same
        if sort_str1 == sort_str2:
            print(f"{str1} and {str2} are anagrams")
        else:
            print(f"{str1} and {str2} are not anagrams")
    else:
        print(f"Given {str1} and {str2} are not anagrams")

if __name__ == "__main__":
    Anagram_built("abdce","bdaec")
