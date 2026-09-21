from newproject import mylibr as lib

#help(mylibr)

size=int(input('Write size: '))
a,b = int(input('write start: ')), int(input('write stop: '))
mylst=lib.inlst2(size,a,b)
print(mylst)