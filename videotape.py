#!/usr/bin/python3

class Videotape:
    Name = "developer-onizuka"
    Position = 0

    def Greed(self):
        output = "Hello, " +self.Name
        return output

    def Forward(self, arg1):
        self.Position = self.Position + arg1
        return self.Position

    def Backward(self, arg1):
        self.Position = self.Position - arg1
        return self.Position
