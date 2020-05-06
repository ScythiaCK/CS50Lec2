class CartCoord:
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.coord = "(" + str(x) + ", " + str(y) + ")"

class PolCoord:
    def __init__(self, r, theta):
        self.r = r
        self.theta = theta

coordinates = CartCoord(3,5)
print(coordinates.coord)
print(coordinates.x)
