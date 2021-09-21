
# number = int(input("enter the number  :"))
#
# reverse_num = 0
#
# while number > 0:
#
#     reminder = number%10
#     reverse_num = (reverse_num*10) + reminder
#     number = number//10
#
# print(number)
#
# print(reverse_num)
# if reverse_num == number:
#
#     print("palindrome")
# else:
#     print("not palindrome")


# Ask for enter the number from the use
number = int(input("Enter the integer number: "))

# Initiate value to null
revs_number = 0

# reverse the integer number using the while loop
temp = number
while (temp > 0):
    # Logic

    remainder = temp % 10
    revs_number = (revs_number * 10) + remainder
    temp = temp // 10

# Display the result
# print("The  temp number is : {}".format(temp))
# print("The reverse number is : {}".format(revs_number))

# print("The reverse number is : {}".format(revs_number))


if revs_number == number:

    print("palindrome")
else:
    print("not palindrome")




