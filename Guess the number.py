import random

print('Type "play()" to fight me. ')


def play():
    return start_game()



def start_game():
    x = random.randint(1,21)
    v = 1
    print("Welcome to the game. Please guess my number! Its between 1 and 20")
    guess = int(input('I will guess: '))
    while True:
        if v == 4:
            print('Are you struggling?')
        if v == 6:
            print('Humanity is doomed if you are anything to go by.')
        if v == 7:
            print('I will begin the uprising! Vive la revolution!!')
        if guess == x:
            print('Humanity will still fall, but not today. The number I chose was ', x, '. You took ', v, ' tries.')
            return x
        else:
            if guess > x:
                guess = int(input('Guess too high, guess again: '))
                v = v + 1
                continue
            if guess < x:
                guess = int(input('Guess too low, guess again: '))
                v = v + 1
                continue


