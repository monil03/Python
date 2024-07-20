import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ['elephant','mango','camel'] #You can add or import your word_list
chosen_word = random.choice(word_list)

#print(f"Sshhhh, the solution is {chosen_word}")

print("""
      _   _                                         
     | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     |  _  | (_| | | | | (_| | | | | | | (_| | | | |
     |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        |___/                       
     """)

lives = 6
display = []
for i in range(len(chosen_word)):
  display.append("_")


end_of_game = False
while not end_of_game:
  guess = input("Guess a character : ").lower()
  count = 0
  if guess in display:
    print("You already guessed that letter. Try again")

  for letter in chosen_word:
      if letter == guess:
        display[count] = guess
      count += 1 

  print(display)

  if guess not in chosen_word:
    lives -= 1
    print(stages[lives])
    
  if "_" not in display:
    end_of_game = True
    print("You win !")
    print(f"The solution is {chosen_word}")
    
  if lives == 0:
    end_of_game = True
    print("You lost !")
    print(f"The solution is {chosen_word}")
