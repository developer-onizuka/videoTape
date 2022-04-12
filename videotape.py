#!/usr/bin/python3

class Videotape:
    Name = "developer-onizuka"
    Position = 0

    def Greet(self):
        output = "Hello, " +self.Name
        return output

    def Forward(self, arg1):
        self.Position = self.Position + arg1
        print(self.Name)
        return self.Position

    def Backward(self, arg1):
        self.Position = self.Position - arg1
        return self.Position

    def Xward(self):
        self.Position = 0
        self.Forward(100)
        self.Backward(80)
        return self.Position
