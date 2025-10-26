import math

def unit_price(d, p):
    area = math.pi * (d / 2 / 100) ** 2
    return p / area

d1 = float(input("Đường kính pizza 1: "))
p1 = float(input("Giá pizza 1: "))
d2 = float(input("Đường kính pizza 2: "))
p2 = float(input("Giá pizza 2: "))

if unit_price(d1, p1) < unit_price(d2, p2):
    print("Pizza 1 rẻ hơn.")
else:
    print("Pizza 2 rẻ hơn.")
