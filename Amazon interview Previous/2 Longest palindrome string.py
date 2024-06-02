# MAX length pamidnrome in a given string
def LargestPalindromeString(string):
    def ExpendingCenter(string,left,right):
        substring = ""
        max_length = 0

        while left >= 0 and right < len(string) and string[left] == string[right]:
            if (right - left +1) > max_length:
                max_length = right - left +1
                substring = string[left:right+1]
            left = left -1
            right = right + 1

        return substring
    
    result = ""

    for i in range(len(string)):
        odd = ExpendingCenter(string,i,i)
        even = ExpendingCenter(string,i,i+1)

        if len(odd) > len(result):
            result = odd
        if len(even) > len(result):
            result = even
    return result

            
if __name__ == "__main__":
    string = "abcdcbc"
    string1 = "bccabc"
    print(LargestPalindromeString(string))
    print(LargestPalindromeString(string1))
