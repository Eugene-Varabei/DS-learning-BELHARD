class Cats:
    __count=0 # создание статического поля (общего для всех об)
    def __init__(self, name='Unknown', age:int=0, color='Unknown') -> str:   # конструктор
        self.__name= name   #self.name=''
        if age<0:
            self.__age =1
        elif 0<age<50:
            self.__age= age
        else:
            self.__age = 1
        #self.age = 0
        self.__color= color    #self.color = ''
        Cats.__count +=1

    # статич свойства
    @staticmethod
    def getCount():
        return Cats.__count


    # свойства (1можно посмотроеть содержимое этого поля изза get)
    def getName(self):
        return self.__name
    def setName(self, name):
        password= input('Write password: ')
        if password == "123456":
            self.__name = name
        else:
            print('No, you cannot')

    def getAge(self):
        return self.__age
    def setAge(self, age):
        if age-self.__age==1:
            self.__age=age


    def getColor(self):
        return self.__color


    #переопределение родительских методов
    def __str__(self):
        return f'Cat {self.__name} is {self.__age} y.o. and it is {self.__color}.'

    # def printy(self):
    #     print(f'Cat {self.__name} is {self.__age} y.o. and it is {self.__color}.')

    #метода (функции)
    def sound(self, word='Miu', count=1):
        print(f'Cat {self.__name} said: ', end='')
        for i in range(count):
            print(word, end=' ')
        print()