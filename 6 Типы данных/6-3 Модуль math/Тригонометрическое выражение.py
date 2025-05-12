from math import pi, pow, sin, cos, tan
x = float(input())
r = x * pi / 180
print(sin(r) + cos(r) + pow(tan(r), 2))