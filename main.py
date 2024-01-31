import random
import os
import pathlib
import pygame


# Function to play a specific song
def play_song(song_path):
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()


# Function to display the current state of the word
def display_word(word, guessed_letters):
    displayed_word = ''.join([letter if letter in guessed_letters else '-' for letter in word])
    return displayed_word


# Set up the directory path
input_directory = pathlib.Path("/Users/macos/Desktop/songs")

# Initialize Pygame
pygame.init()

# Hangman game variables
word_list = [file.stem.upper() for file in input_directory.iterdir() if
             file.is_file() and file.suffix.lower() in ['.mp3', '.wav']]
word_to_guess = random.choice(word_list)
guessed_letters = set()

# Play the corresponding song at the beginning
song_path = input_directory / (word_to_guess + ".mp3")  # Assuming song files have the same name as the word
play_song(str(song_path))

# Main game loop
total_chances = 7
while total_chances > 0:
    print(display_word(word_to_guess, guessed_letters))

    # Get a letter guess from the user
    letter = input("Guess a letter: ").upper()

    if letter in guessed_letters:
        print("You already guessed that letter. Try again.")
    elif letter in word_to_guess:
        guessed_letters.add(letter)
        print("Correct!")
    else:
        total_chances -= 1
        print("Incorrect guess. Chances remaining:", total_chances)

    # Check if the player has guessed the entire word
    if set(word_to_guess) <= guessed_letters:
        print("Congratulations! You guessed the word:", word_to_guess)
        break

# If the player runs out of chances
else:
    print("Game over. You ran out of chances. The correct word was:", word_to_guess)

    

# Optionally, you can add code here to play the full song after the game ends
# pygame.mixer.music.play()
