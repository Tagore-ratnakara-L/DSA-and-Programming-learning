# Printing incrmented Alphabels in right triangle 

def Alpha_pattern(n):
    # ord is teh function to find the ASCII value of alphabets
    k = ord("A")
    print(k)
    for i in range(n):
    # i+1 since we need n+1 colums for respective row 
        for j in range(i+1):
            # end = " " since we need to print the values side by side insted of new line .
            print(chr(k),end=" ") # chr function is used to convert the values in to ASCII Character
            k = k+1 # here it increments k value inturn Character changes
        print()

if __name__ == "__main__":
    n = int(input("Enter the number of rows: "))
    Alpha_pattern(n)