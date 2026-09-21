#
myList=[1,4,6,8,9,4,6,7,3,6,11]
# 1) myList[0:3] or myList[:5] or myList[2:] or myList[sta:stop:step] or myList[::-1] (star>stop)
# двумерный список ген [[j for j in range(b)] for i in range(a)
s= [[j for j in range(4)] for i in range(4)]
print(*s)
