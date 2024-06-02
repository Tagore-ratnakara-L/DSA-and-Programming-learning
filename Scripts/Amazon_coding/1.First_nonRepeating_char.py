# Find first non repeating character in a string ?
def Non_repeat_char(str1):
    frequency = {}

    for x in str1:
        # adding the each characters to dict it added by its repetition 
        frequency[x] = frequency.get(x,0) + 1 # get returns X value to dict as key .

    for i in str1:
        if frequency[i] == 1:
            return i
    return "_"

def Non_rep_char_2(str1):
    dict = {}
    size = len(str1)
    for i in range(size):
        key = str1[i]
        if key not in dict:
            dict[key] = 1
        else:
            dict[key] = dict[key]+1
    
    count = 0
    for index in range(len(str1)):
        # this check each element in str1 to dict key equals to 1
        if (dict[str1[index]]==1):
            return str1[index],count
        count = count + 1




if __name__ == "__main__":
    str1 = 'abdsbdhasd'
    print(Non_repeat_char(str1))
    print(Non_rep_char_2(str1))

