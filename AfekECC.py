class ECC:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def add_ec(self, point1_x, point1_y, point2_x, point2_y):
        incline = (point1_y - point2_y) % self.p
        incline = (incline * pow(point1_x - point2_x, self.p - 2, self.p)) % self.p
        x = (-point1_x - point2_x + incline**2) % self.p
        y = (incline * (point1_x - x) + point1_y) % self.p
        return (x + self.p) % self.p, (y + self.p) % self.p

    def mul_skalar(self, point1_x, point1_y, k):
        s = "{0:b}".format(k)
        x = point1_x
        y = point1_y
        for i in range(1, len(s)):
            x, y = self.add_ec(x, y, x, y)
            if s[i] == "1":
                x, y = self.add_ec(x, y, point1_x, point1_y)
        return x, y
