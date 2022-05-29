#!/usr/bin/python3

class Videotape:
    location = ""

    def __init__(self):
        self.Name = ""
        self.Position = 0

    def Greet(self):
        output = "Hello, " +self.Name
        return output

    def Forward(self, arg1):
        self.Position = self.Position + arg1
        return self.Position

    def Backward(self, arg1):
        self.Position = self.Position - arg1
        return self.Position

    def Xward(self):
        self.Position = 0
        self.Forward(100)
        self.Backward(80)
        return self.Position
    
    def function(a):
        a = a + 1
        return a

