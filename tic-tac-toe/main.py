from game_processor import *
import os 

hangman = Hangman()


logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


total_lives = hangman.lives

game_is_running = True

print(logo + "\n")

print(f"the hint is : {hangman.hint}\n")

while game_is_running:
  response = hangman.compare_words()
  if hangman.lives_lost == total_lives - 1 :
    game_is_running = False
    print("game over well tried\n")
  if hangman.compare_lists():
    print("You have answered perfectly bravo")
    game_is_running = False










