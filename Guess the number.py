import random
want_to_play = str(input(" if you want to play enter \'yes\' else  enter \'no\':"))
num = random.randint(0, 10)
count = 1
while want_to_play.lower() == 'yes':
    guess_num = int(input("Enter number between 0 to 10"))

    if guess_num == num:
        print("Wow!, you guessed it right in " + str(count) + " guesses")
        break
    elif guess_num > num:
        print("Correct number is lower")
    elif guess_num < num:
        print("Correct number is higher")
    count += 1
