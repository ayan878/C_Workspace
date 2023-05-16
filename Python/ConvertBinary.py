def reverse_number(num):
    rev = 0
    if(num==0):
        return 0
        # digit = num % 10
        # rev = rev * 10 + digit
        # num = num // 10
    rev=num%2+10*reverse_number(num/2)
    return rev

# Get input number from user
num = int(input("Enter a number: "))

# Call the reverse_number function and print the result
binary = reverse_number(num)
# print(f"The reverse of {num} is rev_num) #f-strings
print(binary)
