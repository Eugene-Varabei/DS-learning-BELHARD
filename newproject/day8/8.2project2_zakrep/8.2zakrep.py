import matplotlib
matplotlib.use('TkAgg') # отдельное окно для графиков
import matplotlib.pyplot as plt
# библиотека для построения 3d графики
from mpl_toolkits import mplot3d
import numpy as np
import pandas as pd
import seaborn as sns

df=pd.read_csv('WHR_2019.csv')
df.rename(columns = {'Overall rank':'Место в рейтинге',
                     'Country or region':'Страна или регион',
                     'Score':'Баллы',
                     'GDP per capita':'ВВП на душу населения',
                     'Social support':'Социальная поддержка',
                     'Healthy life expectancy':'Ожидаемая продолжительность здоровой жизни',
                     'Freedom to make life choices':'Свобода жизненных выборов',
                     'Generosity':'Щедрость',
                     'Perceptions of corruption':'Восприятие коррупции'},
          inplace = True)
# print(df.describe())
# print(df.info())


#срез ДФ
df_new=df[['Место в рейтинге',"Ожидаемая продолжительность здоровой жизни"]]
df.loc[:, 'Место в рейтинге':'Социальная поддержка'] # поиск по столбцам
df.iloc[0:100, 0:5] # поиск по индексу
df['Баллы'].tolist()

df['Сумма'] = df['ВВП на душу населения'] + df['Социальная поддержка']#
new_row = {'Место в рейтинге': 160, 'Страна или регион': 'Country', 'Баллы': 10,
           'ВВП на душу населения': 0.5,
           'Социальная поддержка': 1.5,
           'Ожидаемая продолжительность здоровой жизни':105,
           'Свобода жизненных выборов':0,
           'Щедрость': 0.001,
           'Восприятие коррупции':0.99} #

df = df._append(new_row, ignore_index=True)# новый столбец
df = df._append(df.sum(axis=0), ignore_index = True)# новая строка
# print(df)

df = df.drop(['Сумма'], axis = 1) # удаление столбца
df = df.drop(df.shape[0]-1, axis = 0)# удаление строки
# df_copied = df.copy() # копия ДФ
# print(df['Страна или регион'].unique()) # уникальные значения



df['Страна или регион'].value_counts() # кол-во значений
df['Баллы_new'] = round(df['Баллы'])
# print(df.groupby('Баллы_new').count())
# print(df.groupby('Баллы_new').sum()) # сумма по баллам
# print(df.groupby('Баллы_new').mean(numeric_only=True)) #срзнач (в скобка обязательно)
# print(df.groupby('Баллы_new').median(numeric_only=True))
#df_agg = df.groupby('Баллы_new').agg({ 'Баллы_new': ['count','sum', 'mean','median' })


# Сводные таблицы
df['ВВП_new'] = round(df['ВВП на душу населения'])
svod=pd.pivot_table(df,index = ['Баллы_new'], columns=['ВВП_new'], values = 'Социальная поддержка', aggfunc = 'mean')
# print(svod)

# Фильтрация данных
# df.sort_values(by = 'ВВП на душу населения'б=, ascending= False).head() # сортирорка данных
# print(df[df['Ожидаемая продолжительность здоровой жизни'] > 1])
# print(df[df['Страна или регион'].str.startswith('F')])
# print(df[(df['ВВП на душу населения'] > 1) & (df['Социальная поддержка'] > 1.5)])

#Применение функции к столбцам
def m_low(row:str):
    return row.lower()
# df['Страна или регион'] = df['Страна или регион'].apply(m_low)
# print(df['Страна или регион'].apply(m_low))

#очистка данных
df_copied = df.copy() # копия ДФ
# df_copied.drop_duplicates(subset=['ВВП_new', 'Баллы_new'])
df_copied.drop_duplicates(subset = ['ВВП_new', 'Баллы_new'], inplace = True) # если нужно заменить на пустые
df_copied.fillna(0)
df_copied.dropna() # удаляет пустые строки
# print(df_copied)


# переменные для хранения номера очередной картинки
numberImage=1
# переменная для хранения адреса сохр изображ (папка должна быть создана)
pathImage='Graphics/'
# переменная для хранения имени изображения
nameImage='image'
# переменная для хранения
extendImage='png'





# графики
df.plot(x = 'Место в рейтинге', y = 'ВВП на душу населения',color='green')
plt.savefig(f'{pathImage}/{nameImage}{numberImage}.{extendImage}') # сохраняет фотку в папку
numberImage+=1

df.plot(kind='hist',x = 'Место в рейтинге', y = 'ВВП на душу населения', color='purple',figsize=(8,5))
plt.savefig(f'{pathImage}/{nameImage}{numberImage}.{extendImage}') # сохраняет фотку в папку
numberImage+=1
df.plot.scatter(x = 'Место в рейтинге', y = 'ВВП на душу населения',c=df['Место в рейтинге']/100, cmap='rainbow') # при cmap указываать только с
plt.savefig(f'{pathImage}/{nameImage}{numberImage}.{extendImage}') # сохраняет фотку в папку
numberImage+=1
plt.show()
df.to_csv('WHR_2019(1).csv',sep=';')


