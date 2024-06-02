def ValidAnagram(str1,str2):
    if len(str1) != len(str2):
        return False
    freq1 = {}
    freq2 = {}
    for i in str1:
        if i in freq1:
            freq1[i] = freq1[i]+1
        else:
            freq1[i] = 1
    for j in str2:
        if j in freq2:
            freq2[j] = freq2[j]+1
        else:
            freq2[j] = 1
    for key in freq1:
        if key not in freq2 or freq2[key] != freq1[key]:
            return False
        
        return True

if __name__ == "__main__":
    str1= "freelance"
    str2 = "lancefree"
    if ValidAnagram(str1,str2) == True:
        print("Given strings are anagrams")
    else:
        print("Given strings are not anagrams")