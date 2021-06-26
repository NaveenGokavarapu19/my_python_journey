import requests 


class WordRetriever():
  def __init__(self):
    self.url = "https://random-words-api.vercel.app/word"
    self.word = ''
    self.request = requests.get(url = self.url)




  def retrieve_data(self):
    data = self.request.json()
    return data[0]['word'],data[0]['definition']
 











