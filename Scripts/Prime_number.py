def PrimeNum_check(num):
    if num < 2:
        return False # 1 and 0 only numbers less than 2 in natural numbers they are not prime
    
    # numbers greater than 2
    for i in range (2,int(num)):
        if num % i == 0:
            return False
    
    return True

if __name__ == "__main__":
    num = int(input("Enter a number: "))

    if PrimeNum_check(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
        