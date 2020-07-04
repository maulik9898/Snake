from .Axis import Axis
import  copy


class Snake:

    def __init__(self, w, h ,s,direction=Axis(1,0), position=Axis(300, 300),):
        self.width = w
        self.height = h
        self.direction = direction
        self.position = position
        self.size = s
        self.tail = []
        self.total = 0

    def move_snake(self,w,h):
        temp = copy.copy(self.position)
        self.position.x = self.position.x + self.direction.x * self.size
        self.position.y = self.position.y + self.direction.y * self.size

        if self.death(w,h):
            return False

        if len(self.tail) != 0:
            for i in range(0, len(self.tail) - 1):
                self.tail[i] = self.tail[i + 1]

            self.tail[-1] = temp

        return  True

    def eat_food(self):

        self.tail.append(Axis(self.position.x ,self.position.y ))
        self.position.x = self.position.x + self.direction.x * self.size
        self.position.y = self.position.y + self.direction.y * self.size
        self.total = self.total + 1

    def change_direction(self, x, y):
        self.direction.x = x
        self.direction.y = y

    def death(self,width,height):
        if width == self.position.x or self.position.x < 0 :
            return  True
        if height == self.position.y or self.position.y < 0:
            return  True
        for body in self.tail:
            if self.position.x == body.x and self.position.y == body.y:
                return  True
        return False


