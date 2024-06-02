# using O(n)
numofletters  = 26
def areAnagrams(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) != len(s2):
        return False
    count=[0 for i in range(numofletters)]
    for i in range(len(s1)):
        count[ord(s1[i] - ord('a'))] +=1;
    for i in range(len(s1)):
        count[ord(s2[i]) - ord('a')] -=1;
    for i in range(numofletters):
        if(count[i] != 0):
            return False
    return True

if __name__ == "__main__":
    areAnagrams('ate','tea')