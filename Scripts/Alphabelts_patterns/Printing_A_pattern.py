"""0 1 2 3 4
0    * * *
1  *       *
2  * * * * *
3  *       *
4  *       *
"""
def Pattern_A(r,c):
    for row in range(r):

        for col in range(c):
           
            if (row == 0 and (col > 0 and col < 4)):
                print("*",end="")
            elif(row == int(5/2) ):
                print("*",end="")
            elif(row != 0 and (col == 0 or col == 4)):
                print("*",end="")
            else:
                print(end=" ")
        # after printing every star we need new line
        print()

if __name__ == "__main__":
    r = int(input("Enter row count: "))
    c = int(input("Enter Column count: "))
    Pattern_A(r,c)