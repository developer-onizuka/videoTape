#!/usr/bin/python3

from videotape import Videotape 

Videotape.location = "Tokyo"

vt = Videotape()
vt.Name = "Bob"
print(vt.Greet())
print(Videotape.location)
print(vt.Forward(100))
print(vt.Backward(10))

print("\n")

vx = Videotape()
vx.Name = "Tom"
print(vx.Greet())
print(Videotape.location)
print(vx.Forward(200))
print(vx.Backward(50))
