def Vowels_consonents(list1):
    list1= list1.replace(" ","")
    print(list1)
    list1= list1.lower()
    Vcount = 0
    Ccount = 0
    vowel = ['a','e','i','o','u']
    list1 = list(list1)
    for i in range(len(list1)):
        if list1[i] in vowel:
            Vcount= Vcount+1
        else:
            Ccount = Ccount+1
    print('Number of vowels is :{},Number of consonents is :{}'.format(Vcount,Ccount))

if __name__ == "__main__":
    list1 = "i am Ratnakar"
    Vowels_consonents(list1)
    Vowels_consonents("Do you need any help")