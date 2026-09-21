from Cats import Cats

print(f"all cats = {Cats.getCount()}")
barsik=Cats("Barsik", 5, "Black")
# barsik.name = "Barsik"
# barsik.age = 5
# barsik.color = "Black"
# barsik.printy()
print(barsik)
# barsik.setName("Tommy")
barsik.setAge(6)
print(barsik)

pus=Cats("Pus", 2, 'Orange')
# pus.name= "Pus"
# pus.age = 1
# pus.color = 'Orange'
# pus.printy()
print(pus)    # принт все делает в строку, поэтому при __стр__ автоматически выпишите что записаоно в классе
              # т.к. там переопределен метод
cat3=Cats(color='Gray')
# cat3.printy()
barsik.sound('Miu miu Nigga', 2)
pus.sound(count=1)
cat3.sound()
print(f'all cats now = {Cats.getCount()}')

