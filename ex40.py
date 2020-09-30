class Song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        # for line in self.lyrics:
            #print(line)
            print(self.lyrics)       # printing line in this type leads to print lines as a list

    def myex(self):
            i = 0
            while i<5:
                print(self.lyrics)
                i += 1


happy_bday = Song("Happy birthday to you")
sue = Song("I don't want to get sued.")
stop = Song("So I'll stop right there")

bulls_on_parade = Song("They rally around that family")
bulls = Song("With pocket full of shells.")

tatto_ka_saudagar = Song(["Aya tatto ka saudagar",
                            "Bolo meow meow meow"])

i_am_a_programmer = Song(["Jhand zindagi ba phir bhi",
                        "I am so happy happy children day."])
happy_bday.sing_me_a_song()
sue.sing_me_a_song()
stop.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
bulls.sing_me_a_song()

tatto_ka_saudagar.sing_me_a_song()
i_am_a_programmer.sing_me_a_song()

i_am_a_programmer.myex()
