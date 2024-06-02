# display the contents based on customer string input 
# cust inp : mo, mou , mous, mouse
# list input : ["mobile","mouse","moneypot","monitor","mousepad"]

# Suggestions for custom input in a list of strings


def Cust_suggestion(str1,custinp):
    str1 = sorted(str1)
    combstr = {}
    str2 = []
    for i in  range(1,len(custinp)+1):
        str2.append(custinp[0:i])
    print(str2)
    j = len(str1)
    r = ["mo","mou",'mouse']
    # for i in r:
        
    #     if i in 'mousepad':
    #         combstr[i] = "mousepad"
    #         combstr[i] = [combstr[i]]+ ["mouse"]
    #         print(combstr)
    #     else:
    #         print(combstr.keys())

    for i in str2[1:len(str2)]:
        key = str(i)
        combstr[key] = []
        for j in str1:   
            if i in j:
                combstr[i] = combstr[i]+[j]
    for key,value in combstr.items():
        if len(key) == 2 :
            value = combstr[key]
            print(value[0:3])
        elif len(key) > 2:
            print(combstr[key],end="\n")

if __name__ == "__main__":
    str1= ["mobile","mouse","moneypot","monitor","mousepad"]
    custinp = "mouse"
    Cust_suggestion(str1,custinp)