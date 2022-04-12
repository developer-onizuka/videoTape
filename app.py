#!/usr/bin/python3

from videotape import Videotape 

vt = Videotape()
print(vt.Greet())
print(vt.Name)
print(vt.Position)
print(vt.Forward(100))
print(vt.Backward(10))

print("\n")

vx = Videotape()
print(vx.Greet())
print(vx.Name)
print(vx.Position)
print(vx.Forward(200))
print(vx.Backward(50))
