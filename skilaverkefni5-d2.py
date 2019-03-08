# Matthías Ólafur
from math import *

class Vigur:

    # Smiður frumstillir x og y hnit vigurs eftir parametrum
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Fall sem skrifar hnit vigurs á skjá
    def prenta(self):
        print("( "+str(self.x), end=", ")
        print(self.y,end=" )\n")

    # Fall sem skilar lengd
    # # sqrt(x^2 + y^2)
    def lengd(self):
        return round(sqrt(self.x**2 + self.y**2),2)

    # Fall sem skilar hallatölu
    # # y / x
    def halli(self):
        if (self.x == 0):
            return
        return round(self.y / self.x, 2)

    # Fall sem skilar þvervigri
    # # snúa um 90° til vinnstri
    # # y fer í x með öfugt formerki og x fer í y
    def þvervigur(self):
        return Vigur(-(self.y),self.x)

    # Fall sem skilar stefnuhorni
    # # atan( y / x )
    def stefnuhorn(self):
        if (self.x == 0 and self.y == 0):
            return 0
        elif (self.x == 0 and self.y > 0):
            return 90
        elif (self.x == 0 and self.y < 0):
            return -90
        grada = round(degrees(atan(self.y/self.x)),2)
        if (self.y >= 0):
            if (self.x < 0):
                grada = 180+grada
        else:
            if (self.x < 0):
                grada = -(180-grada)
        return grada

    # Fall sem tekur vigur sem parameter og skilar horni milli vigra
    # # acos((vigur a(x*y) + vigur b(x*y)) / (lengd vigur a * lengd vigur b))
    # # Lengd vigurs = sqrt(x**2 + y**2)
    def horn(self, v):
        ofan = (self.x * self.y) + (v.x * v.y)
        nedan = (sqrt(self.x**2 + self.y**2) * sqrt(v.x**2 + v.y**2))
        nidurstada = degrees(acos(ofan/nedan))
        return round(nidurstada,2)

    # Fall sem tekur vigur sem parameter og skilar summu vigri
    # x hnit lögð saman og y hnit lögð saman síðan c fundið (langhlið)
    def summa(self, v):
        return Vigur(self.x + v.x, self.y + v.y)

# Keyrsluforrit
v1 = Vigur(1, 3)
v1.prenta()
print("Lengd: ", v1.lengd())
print("Halli: ", v1.halli())
vþ = v1.þvervigur()
print("Þvervigur: ", end=" ")
vþ.prenta()
print("Stefnuhorn: ", v1.stefnuhorn())
v2 = Vigur(-3, 1)
print("Horn milli vigra: ", v2.horn(v1))
v3 = v1.summa(v2)
print("Summa: ", end=" ")
v3.prenta()
