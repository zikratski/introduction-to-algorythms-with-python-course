import random
randr = [str(i) for i in list(range(1,10))]
random.shuffle(randr)
r = ''.join(randr)[:4]
print('I\'ve thought of a 4-digit number. Try to guess it.')
trials = 0
while True:
        try:
            guess = input(f'\nEnter your guess(to stop write \'show\'): ')
            trials += 1
            if guess == 'show':
                print(f"the number is {r}")
            if guess == r:
                print(f"You won! It took {trials} trials.")
                break
            bulls, cows = 0, 0
            for i in range(len(guess)):
                if guess[i] in r:
                    if guess[i] == r[i]:
                        bulls +=1
                    else:
                        cows +=1
            print(f"Bulls: {bulls}")
            print(f"Cows: {cows}")
        except:
            print(f'Error: something went wrong.')