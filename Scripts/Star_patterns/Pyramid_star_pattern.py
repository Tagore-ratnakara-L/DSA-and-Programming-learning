# Printing the Pyramid by star patterns by guven ROW count

def Pyramid_pattern(n):
   # getting row count now running loop within range of n 
    for i in range(n):
        # to print the beginning Spaces 
        for j in range(n-i-1):
            print(" ",end="")
        # to print the star at particular places
        for j in range(i+1):
            print("*",end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Enter the number of Rows: "))
    Pyramid_pattern(n)    
