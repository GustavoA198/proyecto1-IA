class Posicion:
    def __init__(self, posx, posy):
        self.posx = posx  # vertical
        self.posy = posy  # horizontal

    def existe(self, pos, camino):
        for i in camino:
            x1 = pos.posx
            y1 = pos.posy
            x = i.posx
            y = i.posy

            if (x1 == x and y1 == y):
                return True
        return False
