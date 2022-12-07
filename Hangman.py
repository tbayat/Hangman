import random

print('H A N G M A N')

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


def get_random_word(word_list):
    word_index = random.randint(0 , len(word_list) -1)
    return word_list[word_index]

missed_letter = ''
correct_letter = ''
secret_word = get_random_word(words)
game_is_done = False

def display_board(missed_letter , correct_letter, secret_word):
    print(f'{HANGSMAN_PICS[len(missed_letter)]} \n')
    print('missed letter:' , end=' ')
    for letter in missed_letter:
        print(f'\n{letter}' , end = ' \n' )
    blanks= '_' * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letter:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]   
    for letter in blanks:
        print(letter , end = ' ')

def get_guess(alreadyguessed):
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

def play_again():
    answer = input('Do you want to play again? (yes or no)\n').lower().startswith('y')
    return answer

def win(correct_letter):
    foundall_letter = True
    for i in range(len(secret_word)):
        if secret_word[i] not in correct_letter:
            foundall_letter = False
            break
    if foundall_letter:
        print(f'yes the secret word is {secret_word} !you won!')
        return True
    return False

def loose(missed_letter):
    if len(missed_letter) == len(HANGSMAN_PICS) -1 :
        display_board(missed_letter,correct_letter,secret_word)
        print(f'You have run out of guesses!\nAfter {len(missed_letter)}  missed guesses and {len(correct_letter)} correct guesses, the word was {secret_word}')
        return True
    return False



while True:
    display_board(missed_letter,correct_letter,secret_word)
    guess = get_guess(missed_letter + correct_letter)
    if guess in secret_word:
        correct_letter = correct_letter + guess
        game_is_done = win(correct_letter)
    else:
        missed_letter = missed_letter + guess
        game_is_done = loose(missed_letter)
    if game_is_done:
        if play_again():
            missed_letter = ''
            correct_letter = ''
            secret_word = get_random_word(words)
            game_is_done = False
        else:
            break
