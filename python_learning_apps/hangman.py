import random

hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


words = ('istanbul','ankara','izmir','adana','kütahya','kastamonu','kocaeli','tekirdağ','edirne','balıkesir','çanakkale',
'bolu','bursa','aydın','muğla','antalya','mersin','trabzon','tokat','sivas','kars','artvin','ağrı','muş','kahramanmaraş',
'gaziantep','şanlıurfa','ordu','rize','nevşehir')


class Hangman:
  def __init__(self,words):
    self.random_words=random.choice(words)      #rastgele kelime seçiyor
    self.wrong_letter=''
    self.correct_letter=''
    self.game_is_done=False
    
  def hangman_display(self):
    print(hangmanpics[len(self.wrong_letter)])    #yukardaki görseli yanlış yaptıkça bir sonrakine geçiriyor

    print('Yanlış Tahminler:', end=' ')

    for letter in self.wrong_letter:
      print(letter, end=' ')
    print('\n')

    blanks='_'*len(self.random_words)       #harfleri gizliyor 

    for i in range(len(self.random_words)):
      if self.random_words[i] in self.correct_letter:                     #doğru tahmin edilen harfi yerine yerleştiriyor
        blanks = blanks[:i] + self.random_words[i] + blanks[i+1:]

    for letter in blanks:                #her gizli kelimenin arasına 1 er boşluk koyuyor ki kör olmayalım :d
      print(letter, end=' ')

  def word(self, word):
    if word == self.random_words:
      print('Tebrikler bildiniz!!!')               #kontrol kısmı 
      self.check_win()

      if self.check_win() == True:
        self.game_is_done = True  

    else:
      print('Tekrar deneyiniz.')


  def guess(self,guessed):
    while True:
      guess = input('Bir harf giriniz: ').lower().strip()

      if len(guess) > 1:
        self.word(guess)                         #kullanıcıdan harf alma yeri 1 den fazla almamayı engelleme
      elif guess in guessed:
        print('Bu harfi zaten denediniz. Lütfen başka harf girin.')
      else:
        return guess

  def check_win(self):
    
    for i in range(len(self.random_words)):
      if self.random_words[i] not in self.correct_letter:
        return False

    print("Kelime {0}'idi. Tebrikler bildiniz.".format(self.random_words))
    return True


  def check_lost(self):

    if len(self.wrong_letter) == len(hangmanpics) - 1 :
      self.hangman_display()

      wrong=len(self.wrong_letter)
      correct = len(self.correct_letter)
      word = self.random_words

      print('Tahmin hakkınız kalmadı.')
      print("Yanlış tahminleriniz: {0}, Doğru tahminleriniz: {1}, Doğru kelime: {2}".format(wrong,correct,word))
      return True

    return False


  def run(self):
    print("H-A-N-G-M-A-N".center(50,'*'))
    print('Gizli kelimelerimiz şehir isimlerinden oluşmaktadır. Bir tahminde bulunun.')

    while not self.game_is_done:
      self.hangman_display()


      guessed_letter=self.wrong_letter+self.correct_letter
      guess=self.guess(guessed_letter)

      if guess in self.random_words:
        self.correct_letter += guess
        self.game_is_done = self.check_win()

      else:
        self.wrong_letter+=guess
        self.game_is_done = self.check_lost()



def playagain():
  while True:
    again=input('Tekrar oynamak ister misiniz? (e/h)')
    if again == 'e':
      return True
    elif again == 'h':
      return False
    else:
      continue


  

def main():
  
  game = Hangman(words)

  while True:
    game.run()

    if playagain():
      game = Hangman(words)

    else:
      break


main()