def Move_zero(list):
    for i in list:
        if i == 0:
            list.remove(i)
            list.append(i)
    return list

if __name__ == '__main__':
    list = [1,2,0,3,0,6,9]
    print(Move_zero(list))
    list = [1,2,3,0,6,9,7,6,5]
    print(Move_zero(list))