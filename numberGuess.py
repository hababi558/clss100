import random

r = random.randint(1,9)

print('Number guessing game')
print('Guess a number (between 1 to 9)')

chance=0

while chance < 5:
    guess=int(input('Enter ur Guess: '))

    if guess == r :
        print('Congratulation u won')

    elif guess < r :
        print('your guess was too low. guess a number higher than ',guess)
    else:
        print('your guess was too high. guess a number lower than ', guess)
    chance=chance+1
    
if not chance < 5 :
    print('You lose the number is: ',r)