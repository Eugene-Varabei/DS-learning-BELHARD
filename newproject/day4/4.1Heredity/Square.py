class Square:
    def __init__(self, name='', a=0):
        self.name=name
        if a<=0:
            self.a =1
        else:
            self.a =a

    def s(self):
        return self.a*self.a

    def per(self):
        return 4*self.a

    def __str__(self):
        return f'Figure {self.name} with side A={self.a}'