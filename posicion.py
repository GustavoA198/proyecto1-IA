class Posicion:
    def __init__(self, posx, posy):
        self.posx = posx  # vertical
        self.posy = posy  # horizontal

    def existe(self, camino):
        for i in camino:
            x1 = self.posx
            y1 = self.posy
            x = i.posx
            y = i.posy

            if (x1 == x and y1 == y):
                return False
        return True
