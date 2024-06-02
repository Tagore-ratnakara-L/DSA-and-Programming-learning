def Swapping_two_num():
    x = int(input("Enter 1st number: "))
    y = int(input("Enter 2nd number: "))

    x,y = y,x
    print("The value of x after swapping: ",x)
    print("The value of y after swapping: ",y)

if __name__ == "__main__":
    Swapping_two_num()