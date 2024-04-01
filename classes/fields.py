class Game:
    def __init__(self):
        self.name = ""
        self.year = 0

        self.__developer = "XYZ"

    def show_developer(self):
        print(self.__developer)

game = Game()
game.show_developer()