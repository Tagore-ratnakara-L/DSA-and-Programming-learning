def fabonacci_series(n):
    if n == 0:
        print(f"Given number is {n} Please ennter grater than: ",n)
    elif n == 1:
        print(f"Given {n} Fabonacci series is:\n", n-1, n)
    else:
        print(f"Given {n} Fabonacci series is: ")
        n1,n2,n3 = 0,1,0
        for i in range (0,n): 
            print(n3,end=" ")
            n1,n2 = n2,n3 
            n3 = n1+n2

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    fabonacci_series(n)