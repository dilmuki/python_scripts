# # name = input("Please enter your name:  ")
# # age = int(input("How old are you, {0}?  ".format(name)))
# # print(age)
# #
# # if age >= 18:
# #     print("You are old enough to vote!")
# #     print("Please put X in the box!")
# # else:
# #     print("Please come back in {0} years".format(18-age))
#
# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# # if guess < 5:
# #     print ("Please guess higher")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guess it")
#     else:
#         print("Sorry, you have not guessed correctly!")
# elif guess >5:
#     print("Please guess lower:")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guess it")
#     else:
#         print("Sorry, you have not guessed correctly!")
# else:
#     print("You got it first time")

# if guess != 5:
#     if guess <5:
#         print("Please guess higher number: ")
#     else: # guess must be greater than 5
#         print("Please guess lower.")
#
#     guess = int(input())
#     if guess == 5:
#         print("Well done! You guessed it")
#     else:
#         print("You have not guessed it correctly")
# else:
#     print("You got it first time")

age = int(input("How old are you? "))

# #if (age >=16) and (age <=65):
# if 16 <= age <= 65:  # or if 15 < age < 65: will work too
#     print("How are great day at work!")

if (age <16) or (age >65):
    print("Enjoy your free time.")
else:
    print("Have a good day at work!")

