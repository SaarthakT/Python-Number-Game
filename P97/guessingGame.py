import random

chances = 6

print("You have 5 chances to guess the correct number")
 
number = random.randrange(1, 9)
print(number)
 
guess = int(input("Enter your guess: "))
 
while chances > 5:
    if guess == number:
        print("Congratulations, You Won!!!!!!!!!!")
        break
    elif guess < number:
        print("Your guess is too low")
        break
    else:
        print("Your guess is too high")
        break

if not chances > 5:
    print("YOU LOSE!!! The number is ", number)




# import random

# chances=0

# choices=[1,2,3,4,5,6,7,8,9]

# rand_idx = random.randint(0, len(choices)-1)
# number = choices[rand_idx]

# print (number)

# print("You have 5 chances to guess the correct number")

# guess=input ('Enter your guess: ')
# print (guess)

# while chances > 5:
#     if guess == number:
#         print("Congratulations, You Won!!!!!!!!!!")
#         break

# if not chances < 5:
#     print("YOU LOSE!!! The number is ", number)
