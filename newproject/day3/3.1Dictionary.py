myDict=dict()
myDict['Russia']= 'Moskow'
myDict['China']= 'Bejiing'
myDict['France']= 'Paris'
# Получение значение по ключю
# print(myDicr['Russia'])
# print(myDict.get('Russia'))
# print(myDict.get('England', 'no country'))
# .keys() возвращает все ключи из словаря
# print(myDict.keys())
# for key in myDict.keys():
#     print(key)
# функ .values() возвращает все знач словаря
# функ items() возвращает пары ключ-знаачение
for k,v in myDict.items():
    print(k,':', v)
