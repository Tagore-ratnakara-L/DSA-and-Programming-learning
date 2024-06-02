def Factorial(num):
    Fact = 1
    i = num
    if num < 0:
        print("Factorial doesn't exists for this number")

    elif num == 0:
        print("The factorial of 0 is 1")
    
    else:
        while i > 0:
            Fact = Fact*i
            i = i -1
        print(Fact)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    Factorial(num)

