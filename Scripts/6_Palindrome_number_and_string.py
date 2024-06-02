def palindrome(num):
    original = str(num)
    if len(original) == 0 or len(original) == 1:
        print("Given number cannot specify as palindrome")
    elif type(num)== str:
        reverse_string = original[::-1]
        print(f"Given {reverse_string} is a palindrome ")
    else:
        a = 0
        b = 0
        i = len(original)
        while i > 0:
            a = (num)%10
            b = b*10+a
            num = num//10
            i -=1
        print(b)
        if b == original:
            print(f"Given {b} is a palindrome ")

if __name__ == "__main__":
    inp =input("Enter a palindrome No./String: ")
    if type(inp) == int:
        num = int(inp)
    else:
        num = str(inp)
    palindrome(num)
