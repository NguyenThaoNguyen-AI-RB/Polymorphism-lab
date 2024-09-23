class Guitar:
    def play(self):
        print('Playing the guitar')
class Piano:
    def play(self):
        print('Playing the piano')
def play_instrument(instruments):
    instruments.play()

guitar = Guitar()
play_instrument(guitar)
piano = Piano()
play_instrument(piano)