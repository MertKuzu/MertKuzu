import random

#oyun esnasındayken çıkma tuşu ekle q olsun ama sürekli söylemesin 1 kere söylesin
#scoreboard olacak



moves=['taş', 'kağıt', 'makas']

def game():
    scorePlayer=0
    scoreComputer=0
    while True:

        playerMove=input('Hamlenizi seçin (taş, kağıt, makas): ').lower().strip()
        aiMove=random.choice(moves)
        if playerMove==aiMove:
            print(f"Hamleniz: {playerMove} Bilgisayarın hamlesi: {aiMove} Berabere!")            
        elif playerMove==moves[0] and aiMove==moves[2]:
            scorePlayer+=1
            print(f'Hamleniz: {playerMove} Bilgisayarın hamlesi: {aiMove} Kazandınız!')
            print(f'Skor: {scorePlayer}-{scoreComputer}')
        elif playerMove==moves[0] and aiMove==moves[1]:
            scoreComputer+=1
            print(f'Hamleniz: {playerMove} Bilgisayarın hamlesi: {aiMove} Kaybettiniz!')
            print(f'Skor: {scorePlayer}-{scoreComputer}')
        elif playerMove==moves[2] and aiMove==moves[0]:
            scoreComputer+=1
            print(f'Hamleniz: {playerMove} Bilgisayarın hamlesi: {aiMove} Kaybettiniz!')
            print(f'Skor: {scorePlayer}-{scoreComputer}')
        elif playerMove==moves[2] and aiMove==moves[1]:
            scorePlayer+=1
            print(f'Hamleniz: {playerMove} Bilgisayarın hamlesi: {aiMove} Kazandınız!')
            print(f'Skor: {scorePlayer}-{scoreComputer}')
        elif playerMove==moves[1] and aiMove==moves[0]:
            scorePlayer+=1
            print(f'Hamleniz: {playerMove} Bilgisayarın hamlesi: {aiMove} Kazandınız!')
            print(f'Skor: {scorePlayer}-{scoreComputer}')
        elif playerMove==moves[1] and aiMove==moves[2]:
            scoreComputer+=1
            print(f'Hamleniz: {playerMove} Bilgisayarın hamlesi: {aiMove} kaybettiniz!')
            print(f'Skor: {scorePlayer}-{scoreComputer}')
        else:
            print(f'Hatalı hamle seçimi tekrar deneyin.')



game()