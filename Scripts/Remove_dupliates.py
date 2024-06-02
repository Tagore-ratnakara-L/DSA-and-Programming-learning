def Duplicates_rem(list):
    dup_items = set()
    uniq_items = []

    for i in list:
        if i not in dup_items:
            uniq_items.append(i)
            dup_items.add(i)
    
    print(sorted(dup_items))

if __name__ == "__main__":
    list = ['10','10','20','30','20','40']
    Duplicates_rem(list)
