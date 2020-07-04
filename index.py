import random
import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Hangman")
pygame.display.update()

#pygame.mixer.init()

pygame.mixer.music.load("theme.wav")
pygame.mixer.music.set_volume(0.01)
pygame.mixer.music.play(-1)


file = open("german.dic", "r")
contents = file.read()
word_list = contents.split("\n")

secret_word = random.choice(word_list)
used_tries = 0
try_limit = 10
underscore = ""

for i in range(len(secret_word)):
    underscore += "_"


myfont = pygame.font.SysFont('Comic Sans MS', 30)

textsurface = myfont.render(underscore, False, (255, 255, 255))

screen.blit(textsurface,(0,0))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()







































"""
while True:
    pygame.display.update()
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")

    if query == 'p':

        # Pausing the music
        pygame.mixer.music.pause()
    elif query == 'r':

        # Resuming the music
        pygame.mixer.music.unpause()
    elif query == 'e':

        # Stop the mixer
        pygame.mixer.music.stop()
        break

def get_input():
    while True:
        current_input = input("Enter guess: ")
        if len(current_input) == len(secret_word) or len(current_input) == 1:
            break
        print("Invalid Input")

    return current_input


file = open("german.dic", "r")
contents = file.read()
word_list = contents.split("\n")
while True:
    print("Choosing 1 of " + str(len(word_list)) + " words...")

    secret_word = random.choice(word_list)
    used_tries = 0
    try_limit = 10
    underscore = ""

    for i in range(len(secret_word)):
        underscore += "_"

    while used_tries < try_limit:
        print("Guesses left: %d" % (try_limit - used_tries))
        print(underscore)
        guess = get_input()
        if guess.lower() == secret_word.lower():
            break
        not_found = True
        if len(guess) == 1:
            for i in range(len(secret_word)):
                if guess.lower() == secret_word[i].lower():
                    not_found = False
                    underscore = underscore[:i] + secret_word[i] + underscore[i + 1:]

        if underscore == secret_word:
            break
        if not_found:
            used_tries += 1

    print(secret_word)
    if used_tries == try_limit:
        print("No guesses anymore, you lose")
    else:
        print("You win!")



    while True:
        answer = input("Wanna play again? (Y/N): ")
        if answer in ('y', 'n'):
            break
        print
        "Invalid input."
    if answer == 'y':
        continue
    else:
        print("Thanks for playing!")

        break
"""