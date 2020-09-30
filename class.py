class game:
    def __init__(self, name1, name2):
        #print("Enter name of the players.")
        self.name1 = name1
        self.name2 = name2

    def sum(self):
        sum = self.name1 + self.name2
        print(sum)


p1 = game("hello", "world")
p2 = game("my world", "hello")

p1.sum()
p2.sum()
