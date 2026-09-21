from Square import Square as Sq
class Rectangle(Sq):
    def __init__(self,name='',a=1,b=2):
        # явно вызовем конструктор родителького класса
        super().__init__(name, a)
        # self.name = name
        # if a<=0:
        #     self.a=1
        # else:
        #     self.a=a
        if b<=0:
            self.b=1
        else:
            self.b=b

    def obs(self):
        val=super().s()+self.s()
        return val
    def s(self):
        return self.a*self.b

    def per(self):
        return (self.a+self.b)*2

    def __str__(self):
        return super().__str__() + f' and side B={self.b}'

