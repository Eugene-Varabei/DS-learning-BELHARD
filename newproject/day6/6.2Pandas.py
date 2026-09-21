import pandas as pd
import numpy as np

# пример создание Series ( одномерная структура)
# data=[i for i in range(0,12) if i%2==0]
# series=pd.Series(data)
# print(series)
# labels=['laptop','phone','iphone', 'printer','keyboard','mouse']
# series= pd.Series(data,index=labels)
# print(series)
# # print(series['phone'])
#
# # извлечение из объ сериес всех значений как массив numpy
# # x1=series.values
# # print(x1)
#
# #извлечение из объ сериес всех индексов как массив numpy
# x2=series.index
# print(x2)

# пример создания DataFrame (двумерная структура)
# data={'Name': ["Ivan",'Igor','Nikita','Katya','Elena'],'Age':[25,16,36,22,99],'City': ['Minsk', 'Brest','Vitebsk','Grodno','Gomel']}
# df=pd.DataFrame(data)
# print(df)

# Способы создания Series
#1 из списка
# series=pd.Series([i for i in range(15) if i%3==0])
# print(series)

#2 из двух списков одинаковой длины (1 список хнач, второй индексы)
# series=pd.Series([i for i in range(1,6)], index=['a1'+i for i in 'abcde'])
# print(series)

#3 из словаря, где знач это знач, ключ это индекс
# data={'Name': "Ivan",'Age': 99,'City': 'Minsk'}
# series=pd.Series(data)
# print(series)

#4 Линейное заполнение
# series=pd.Series(np.arange(1,6),index=['a2'+i for i in 'abcde'], name='DATA',dtype=float)
# print(series)


# чтение из csv файла в  Dataframe
# df=pd.read_csv('data.csv',index_col='столбец_1')
# print(df)

# функция head() ыводит 5 первые строки с df
# print(df.head(3))

# функция tail() выводит посление 5 строк с df
# print(df.tail())

# чтекние excel файлов в DF
# df=pd.read_excel('data1.xlsx',index_col='SR.')
# print(df)

# чтение с другого листа (по его имени) Excel in DF (по нумерации листа sheet_name=1)
# df=pd.read_excel('data1.xlsx','Sheet2',index_col='SR.')
# print(df)

# начинатб чтение с выброанной строки с экселя (skiprows)
# df=pd.read_excel('data1.xlsx','Sheet1',skiprows=20,header=None)
# print(df)

# c пропуска указаннойго числа строк с коца
# df=pd.read_excel('data1.xlsx','Sheet1',skipfooter=20)
# print(df)


# запись данных в csv файл
# df=pd.DataFrame({'Name': ["Ivan",'Igor','Nikita','Katya','Elena'],'Age':[25,16,36,22,99],'City': ['Minsk', 'Brest','Vitebsk','Grodno','Gomel']})
# df.to_csv('output.csv',index=False,sep=';')

# запись данных в excel file
# df.to_excel('outs.xlsx',index=False)
# запись данных в excel file
# df.to_excel('outs.xlsx',sheet_name='List2',index=False)

#запись нескольких DF в excel но в разные листы (генерация листов)))))
# with pd.ExcelWriter('outs.xlsx') as writer:
#     for i in range(3):
#         df.to_excel(writer, index=False, sheet_name=f'List{i}')


# №запись несколько датафреймов на разные листы в сущ или готовый эксель файл
# with pd.ExcelWriter('outs.xlsx', mode='a') as writer:
#     df.to_excel(writer, index=False, sheet_name='List3')



# извлечение данных из DFrames
# df=pd.DataFrame({'Bikes': [100,200,300,450],
#                  'E-scooters':[123,234,345,456]})
# print(df)
# обращение к столбцу по имени(получаем сериес)
# print(df['Bikes'])

# фкункиця .loc возвращает эл кот стоит на пересеч указанной строки и столбца
# print(df.loc[1,'Bikes'])

# получение из ДФ названия всех столбов
# print(df.columns)

# получение всех индексов (строк)
# print(df.index)

# обход ДФ двумя циклами for
# for i in df.index:
#     for j in df.columns:
#         print(df.loc[i,j])

# получение  данных из указанной строки
# print(df.loc[1])

#получение конкретного столбца из ДФ
# print(df.loc[:,'Bikes'])
# print(df.loc[2:,'Bikes'])

# доабвление столбца исхдя из имебщихся (вычисл) + - * / // % **
# df['Total']=df['Bikes']+df['E-scooters']
# print(df)

# добавл нового столбца  конкретными жанными
# 1 добавить массив или список
# x=[50,33,64,82]
# df['Motobikes']=x
# print(df)

#2 добавление готового Series
# ser= pd.Series([205,313,524,240,420])
# df['Rollers']=ser
# print(df)


# добавление/обновление новых строк через .loc
# df.loc[4]=[480,565,104,300]
# print(df)

# удаление столбцов из ДФ c созданием нового ДФ
# df2=df.drop(['Motobikes', 'Rollers'], axis=1)

# удаление столбов из текущ ДФ
# df.drop(['Motobikes', 'Rollers'], axis=1, inplace=True)
# print(df)

# Удаление строк из ДФ (inplace=True для удаленре в текущем (экономия памяти)
# df2=df.drop([1,4], axis=0)
# print(df2)



# сортировка DATAFRAMES
# df=pd.DataFrame({'A': [2,1,7,2],
#                  'B': [8,2,6,3],
#                  'C': [7,8,9,2]})
# print(df)
# print()

# df2=df.sort_values(by=['A', "B"])
# print(df2)

# Сортировка по убыванию
# df2=df.sort_values(by=['A','B','C'], ascending= [False, True, False])
# print(df2)

# сортировка по индексам (номера строк)
# df3=df2.sort_index(axis=0, ascending= False)
# print(df3)

# Сортировка по номерам стобцов
# df3=df2.sort_index(axis=1, ascending= False)
# print(df3)


#Пропуски данных
df=pd.DataFrame({'Coal': [27,44,None,3],
                 'Fat': [10,25,18,3],
                'Protein':[3,8,1,None]})

# функция isnull() проверяте на существование пропусков в ДФ и создает маску, кот пропуски помечены знач TRUE
df2= df.isnull()

# Создадим Series по кол-ву пропусков в каждом столбцу
seriesCountNull=df2.sum()
# print(seriesCountNull)

#Получим(*посчитаем) общ кол-во пропусков
# allNull=df2.sum().sum()
# allnull2=seriesCountNull.sum()
# print(allNull)
# print(allnull2)


# замена всех пропусков на 0.0
cnt=df2.sum().sum()
if cnt>0:
    df.fillna(0,inplace=True)

print(df)






