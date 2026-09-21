from Square import Square as Sq
from Rectangle import Rectangle as Rec
from Triangle import Triangle as Tr
first=Sq("abcd", 3)
print(first)
print(f'Square is {first.s()}')
print(f'Perimetr is {first.per()}')

rec= Rec("right",4,5)
print(rec)
print(f'All square "abcd and right" with side A = {rec.obs()}')
print(f'Square is {rec.s()}')
print(f'Perimetr is {rec.per()}')

tri=Tr('trian',1,1,2)
print(tri)
print(f'Square is {tri.s()}')
print(f'Perimetr is {tri.per()}')
