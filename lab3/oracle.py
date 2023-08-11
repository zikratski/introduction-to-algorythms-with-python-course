import sys, random
n = int(sys.argv[1])
print(f'Please think of a number between 1 and {n}. Guess it.')
trials = 0
maxn = n+1
minn = 0
while True:
    try:
        # midn = (maxn - minn) // 2
        guess = (maxn + minn) // 2
        print(f"My guess is: {guess}")
        print(f"[0 = number < {guess}, 1 = number > {guess}, 2 = I guessed it]")
        trials += 1
        userval = int(input())
        if (userval == 1):
            if maxn == minn or guess == maxn:
                print("Mistake")
            else:
                minn = guess
            # print(f'My number is less than {guess}.')
        elif (userval == 0):
            if minn == maxn or minn == guess:
                print("Mistake")
            else:
                maxn = guess
            # print(f'My number is greater than {guess}.')
        elif (userval == 2):
            print(f'Your number is {guess}. It took {trials} trials.')
            break
        print()
    except KeyboardInterrupt:
        break
    except ValueError:
        print(f'Error: it\'s not a number.')
    except:
        print(f'Error: something went wrong.')