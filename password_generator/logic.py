import string
import random

class Password_generator():
  def __init__(self,no_of_lower,no_of_upper,no_of_symbols):
    self.lower = no_of_lower
    self.upper = no_of_upper
    self.symbols = no_of_symbols
    self.password_list = []
    self.lower_list = []
    self.upper_list = []
    self.symbols_list = []
    self.generate_lower_list()
    self.generate_upper_list()
    self.generate_symbols_list()

  def generate_lower_list(self):
    self.lower_list = [random.choice(string.ascii_lowercase) for lower_letter in range(self.lower)]

  def generate_upper_list(self):
    self.upper_list =  [random.choice(string.ascii_uppercase) for lower_letter in range(self.upper)]

  def generate_symbols_list(self):
    self.symbols_list =  [random.choice(string.punctuation) for lower_letter in range(self.symbols)]

  def join_list_and_display_list(self):
    self.password_list = self.lower_list + self.upper_list + self.symbols_list

    return ''.join(self.password_list)