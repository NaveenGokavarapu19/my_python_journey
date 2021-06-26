import data_handler

word_retriever = data_handler.WordRetriever()

word,hint = word_retriever.retrieve_data()

HANGMAN_PICS = ['''
     +---+
           |
           |
           |
          ===''', '''
       +---+
       O   |
           |
           |
          ===''', '''
       +---+
       O   |
       |   |
           |
          ===''', '''
       +---+
       O   |
      /|   |
           |
          ===''', '''
       +---+
       O   |
      /|\  |
           |
          ===''', '''
       +---+
       O   |
      /|\  |
      /    |
          ===''', '''
       +---+
       O   |
      /|\  |
      / \  |
          ===''']




class Hangman():
  def __init__(self):
    self.to_display_list = []
    self.lives_lost = 0
    self.lives = len(HANGMAN_PICS)
    self.index = 0
    self.word = word.lower()
    self.word_list = list(word.lower())
    self.hint = hint
    self.make_list()


  def make_list(self):
    self.to_display_list = ['-' for _ in range(len(self.word)) ]
    print(self.word)


  def compare_words(self):
    print(hint)
    self.guess = input("Please enter a letter: \n")


    if self.guess in self.to_display_list:
      print("Please enter a different letter ")
    elif self.guess in self.word_list:
      for i in range(len(self.to_display_list)):
        letter = self.word_list[i]
        if letter == self.guess:
          self.index = i
          self.replace_list()

    else:
      print("Oops looks like who have entered a wrong letter\n")
      self.increase_lives_lost()
      self.display_hangman()
    print(self.to_display_list)





  def replace_list(self):
    self.to_display_list[self.index] = self.guess
 

  def display_hangman(self):
    print(HANGMAN_PICS[self.lives_lost])


  def increase_lives_lost(self):
    self.lives_lost +=1
    return self.lives

  def compare_lists(self):
    if list(self.word) == self.to_display_list:
      return True



