# Longest Palindrome in given string "ababcd"

def LongestPalindrome(string):
    res = ""
    reslen = 0
    for i in range(len(string)):
        # odd length
        l,r = i,i 
        while  l >= 0 and r < len(string) and string[l] == string[r]:
            if (r - l + 1) > reslen:
                res = string[l:r+1]
                reslen =  r-l + 1
            l = l-1
            r = r+1

        # even length
        l,r = i, i+1
        while l >= 0 and r< len(string) and string[l] == string[r]:
            if (r-l+1) > reslen:
                res = s[l:r+1]
                reslen = r-l+1
            l = l-1
            r = r+1
    return res
    
if __name__ == "__main__":
    string = "abcdcbc"
    print(LongestPalindrome(string))
