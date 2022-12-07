import random
from PIL import Image
import pyautogui as pg

pg.alert('you start a dangrous game --> H A N G M A N ')

im1=Image.open("/Users/tina/projects/coffee to do/Hangman_game/images/1.png") 
im2= Image.open("/Users/tina/projects/coffee to do/Hangman_game/images/2.png")
im3=Image.open("/Users/tina/projects/coffee to do/Hangman_game/images/3.png") 
im4= Image.open("/Users/tina/projects/coffee to do/Hangman_game/images/4.png")
im5=Image.open("/Users/tina/projects/coffee to do/Hangman_game/images/5.png") 
im6= Image.open("/Users/tina/projects/coffee to do/Hangman_game/images/6.png")
im7= Image.open("/Users/tina/projects/coffee to do/Hangman_game/images/7.png")
img_list=[im1,im2,im3,im4,im5,im6,im7]
        

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


def get_random_word(word_list):
    word_index = random.randint(0 , len(word_list) -1)
    return word_list[word_index]

missed_letter = ''
correct_letter = ''
secret_word = get_random_word(words)
game_is_done = False

def display_board(missed_letter , correct_letter, secret_word):
    img_list[len(missed_letter)].show()
    letter =''
    letter += f'{missed_letter} '
    pg.alert(f'missed letter : {letter} ')
    blanks=  '_'  * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letter:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]   
    result= (" ".join(blanks))
    pg.alert(f'secret word : {result}')
    
def get_guess(alreadyguessed):
    while True:
        guess = pg.prompt( 'please enter your guess' )
        guess = guess.lower()
        if len(guess) != 1:
              pg.alert('Please enter a single letter.')
        elif guess in alreadyguessed:
              pg.alert('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
              pg.alert('Please enter a LETTER.')
        else:
             return guess

def play_again():
    answer = pg.prompt('Do you want to play again? (yes or no)\n')
    answer= answer.lower().startswith('y')
    return answer

def win(correct_letter):
    foundall_letter = True
    for i in range(len(secret_word)):
        if secret_word[i] not in correct_letter:
            foundall_letter = False
            break
    if foundall_letter:
        pg.alert(f'yes the secret word is { secret_word } !\nyou won!')
        return True
    return False

def loose(missed_letter):
    if len(missed_letter) == len(img_list) -1 :
        display_board(missed_letter,correct_letter,secret_word)
        pg.alert(f'You have run out of guesses!\nAfter {len(missed_letter)} missed guesses and {len(correct_letter)} correct guesses, the word was { secret_word }')
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
