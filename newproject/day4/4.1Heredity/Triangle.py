from Rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self, name='',a=1,b=1,c=1):
        super().__init__(name,a,b)
        if a+b>c and a+c>b and b+c >a:
            self.c=c
        else:
            self.a,self.b,self.c=1,1,1

    def per(self):
        return self.a + self.b+ self.c

    def s(self):
        pr=self.per()
        squ=(pr*(pr-self.a)*(pr-self.b)*(pr-self.c))**(0.5)
        return squ

    def __str__(self):
        return super().__str__() + f' and side C={self.c}'