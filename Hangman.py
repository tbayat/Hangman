import random

HANGSMAN_PICS = ['''
   +---+
       |
       |
       |
     =====''' , '''
    +---+
    o   |
        |
        |
      =====''', '''
    +---+
    o   |
    |   |
        |                   
      =====''' , '''
    +---+
    o   |
    |\  |
        |
      =====''' , '''
    +---+
    o   |
   /|\  |
        |
      =====''' , '''
    +---+
    o   |
   /|\  |
     \  |
      =====''' , '''
     +---+
     o   |
    /|\  |
    / \  |
       =====''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


def getrandom_word(wordlist):
    wordindex = random.randint(0 , len(wordlist) -1)
    return wordlist[wordindex]

print('H A N G M A N')
missedletter = ''
correctletter = ''
secretword = getrandom_word(words)
gameisdone = False

def display_board(missedletter , correctletter, secretword):
    print(f'{HANGSMAN_PICS[len(missedletter)]} \n')
    print('missed letter:' , end=' ')
    for letter in missedletter:
        print(f'\n{letter}' , end = ' \n' )
        

    blanks= '_' * len(secretword)
    for i in range(len(secretword)):
        if secretword[i] in correctletter:
            blanks = blanks[:i] + secretword[i] + blanks[i+1:]   
    for letter in blanks:
        print(letter , end = ' ')

def getguess(alreadyguessed):
    while True:
        guess = input('\nplease guess a letter:').lower()
        if len(guess) != 1:
              print('\nPlease enter a single letter.')
        elif guess in alreadyguessed:
              print('\nYou have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
              print('\nPlease enter a LETTER.')
        else:
             return guess

def playagain():
    answer = input('Do you want to play again? (yes or no)\n').lower().startswith('y')
    return answer

def win(correctletter):
    global gameisdone
    foundall_letter = True
    for i in range(len(secretword)):
        if secretword[i] not in correctletter:
            foundall_letter = False
            break
    if foundall_letter:
        print("yes the secret word is " +secretword + " !you won!")
        gameisdone = True
    return gameisdone

def loose(missedletter):
    global gameisdone
    if len(missedletter) == len(HANGSMAN_PICS) -1 :
            display_board(missedletter,correctletter,secretword)
            print('You have run out of guesses!\nAfter ' + str(len(missedletter)) + ' missed guesses and ' + str(len(correctletter)) + ' correct guesses, the word was "' + secretword + '"')
            gameisdone = True
    return gameisdone



while True:
    display_board(missedletter,correctletter,secretword)
    guess = getguess(missedletter + correctletter)
    if guess in secretword:
        correctletter = correctletter + guess
        gameisdone = win(correctletter)
    else:
        missedletter = missedletter + guess
        gameisdone = loose(missedletter)
    if gameisdone:
        if playagain():
            missedletter = ''
            correctletter = ''
            secretword = getrandom_word(words)
            gameisdone = False
        else:
            break
