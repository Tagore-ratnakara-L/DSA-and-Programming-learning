def Amstrong(num):
    original = num
    s1 = 0
    exp = len(str(num))
    Ams = 0
    while num > 0:
        s1 = num%10
        Ams += s1**exp
        num = num//10
    print(Ams)
    if Ams == original:
        print(True)
    else:
        print(False)
      
if __name__ == "__main__":
    Amstrong(1632)