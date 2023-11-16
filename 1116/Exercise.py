import math

class MyShape:
    #建立物件
    def __init__(self, side, length, width, radius):
        self.side = side
        self.length = length
        self.width = width
        self.radius = radius

    #建立輸出格式
    def __str__(self):
        return f"\nSquare Area = {ms.square_area()} \nRectangle Area = {ms.rectangle_area()} \nCircluar Area = {ms.circular_area()}\n"

    #計算各項面積
    def square_area(self):
        return self.side*self.side
    def rectangle_area(self):
        return self.length*self.width
    def circular_area(self):
        return self.radius*self.radius*math.pi

#輸出
ms = MyShape(5,2,5,10)
print(ms)


