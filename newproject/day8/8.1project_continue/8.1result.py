import matplotlib
matplotlib.use('TkAgg') # отдельное окно для графиков
import matplotlib.pyplot as plt
# библиотека для построения 3d графики
from mpl_toolkits import mplot3d
import numpy as np
import pandas as pd
import seaborn as sns

# чтение из файла
df=pd.read_excel('Canada.xlsx','Canada by Citizenship',skiprows=20,skipfooter=1)
# вывекдем на экран название всех столбоц
# print(df.columns)

# удалим ненужные столбцы в тек ДФ
df.drop(['AREA','REG', 'DEV','Coverage'], axis =1, inplace=True)
# print(df)

# переименовать столбцы
df.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)
# print(df)

# добаваить нов стобцец итого (тотал) с суммой по всем годам
df['Total']=df[[i for i in range(1980,2014)]].sum(axis=1)
# print(df)

# преобразуем столбец страна в индекс
df.set_index('Country', inplace=True)
# print(df)

# переменные для хранения номера очередной картинки
numberImage=1
# переменная для хранения адреса сохр изображ (папка должна быть создана)
pathImage='images2/'
# переменная для хранения имени изображения
nameImage='image'
# переменная для хранения
extendImage='png'

# построим список с всеми годамиит (назвы столбцов)
years=[i for i in range(1980,2014)]

#выведем на экран все данные по Швейцарииза все года
# print(df.loc['Switzerland', years])

# построение графика
df.loc['Switzerland', years].plot()

#настройки графика
plt.title('Из Швейцарии в Канаду')
plt.xlabel('Года')
plt.ylabel('Количество')
plt.savefig(f'{pathImage}/{nameImage}{numberImage}.{extendImage}') # сохраняет фотку в папку
numberImage+=1
plt.show()

#  построить график по нескольким странам
newData=df.loc[['India','Pakistan','Bangladesh'], years]
# print(newData)

# транспонирование DF
newData=newData.T

newData.plot()
plt.savefig(f'{pathImage}/{nameImage}{numberImage}.{extendImage}')
numberImage+=1
plt.show()

# Секторные диаграммы
# функция groupby группирует строки ДФ по указанному критерию

cont=df.groupby('Continent').sum()
# print(cont)

cont['Total'].plot(kind='pie', figsize=(8,8), autopct='%1.1f%%', shadow=True) # shadow  это тень,
plt.title('По континентам',  fontname='Times New Roman', fontsize=16, fontweight='bold')
plt.axis('equal')
plt.savefig(f'{pathImage}/{nameImage}{numberImage}.{extendImage}')
numberImage+=1
plt.show()


# настройка секторной диаграммы
colors=['lightblue','gold','lightgreen','pink', 'red','blue','gray']
explode=[0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.3]
cont['Total'].plot(kind='pie', figsize=(14,9), autopct='%1.1f%%', shadow=False,
                   colors=colors, labels=None,
                   pctdistance=1.12, explode=explode) # pctdistance на сколько за сектором будет находистя проценты
plt.title('По континентам',  fontname='Times New Roman',
                                fontsize=16, fontweight='bold')
plt.axis('equal')
plt.legend(labels=cont.index, loc='upper right',
           prop={'family': 'Times New Roman',
            'size': 16,
            'weight': 'bold'})

plt.savefig(f'{pathImage}/{nameImage}{numberImage}.{extendImage}')
numberImage+=1
plt.show()



# диаграмма рассеивания
allyear=pd.DataFrame(df[years].sum(axis=0))
# print(allyear)

allyear.index=map(int,allyear.index)
allyear.reset_index(inplace=True)
allyear.columns=['year','Total']
# print(allyear)

allyear.plot(kind='scatter',x='year', y = 'Total',figsize=(10,6), color='darkblue')
plt.title('Всего за 1980-2013 гг', fontname='Times New Roman',
                                fontsize=16, fontweight='bold')
plt.xlabel('Года')
plt.ylabel('Количество')
plt.savefig(f'{pathImage}/{nameImage}{numberImage}.{extendImage}')
numberImage+=1
plt.show()

# диаграмма с областями

top=df.loc[['India','China','Pakistan', 'France'], years]
top=top.T
color2=['green','blue','yellow','purple']
top.plot(kind='area', stacked=False, figsize=(16,8), color=color2)
plt.xlabel('Года')
plt.ylabel('Количество')
plt.show()

# построение гистограмм
df[2000].plot(kind='hist',figsize=(8,5))
plt.xlabel('Количество иммигранторв')
plt.ylabel('Количество стран')
plt.savefig(f'{pathImage}/{nameImage}{numberImage}.{extendImage}')
numberImage+=1
plt.show()


# столбчатая диаграмма
france=df.loc['France', years]
france.plot(kind='bar',figsize=(10,6),color='lightblue')
plt.xlabel('Года')
plt.ylabel('Количество')
plt.savefig(f'{pathImage}/{nameImage}{numberImage}.{extendImage}')
numberImage+=1
plt.show()


# на столбчатой лиаграмме указать важное место
france.plot(kind='bar',figsize=(10,6))
plt.xlabel('Года')
plt.ylabel('Количество')
plt.annotate('Attention', xy=(19,4300),rotation =23, va='bottom',ha='left')#xy координаты начала текста, rotat- градус написания текста
plt.annotate('',xy=(28,5200),xytext=(17,3800),xycoords='data',arrowprops={'arrowstyle': '->',
                                                                          'connectionstyle': 'arc3',
                                                                          'color': 'black',
                                                                           'lw': 1.5}) # указания на важную точку
# xytext - начало координат стрелкиб, xy- конец координат
plt.savefig(f'{pathImage}/{nameImage}{numberImage}.{extendImage}')
numberImage+=1
plt.show()


# построение диаграммы по горизонт
france.plot(kind='barh',figsize=(12,16),color='steelblue')
plt.gca().invert_yaxis() # перевернет диаграмму
plt.xlabel('Количество')
plt.ylabel('Года')
plt.savefig(f'{pathImage}/{nameImage}{numberImage}.{extendImage}')
numberImage+=1
plt.show()

# на примере горизн столбч диаграммы сделать подпись значений каждогго столбца
france.plot(kind='barh',figsize=(12,16),color='steelblue')
plt.xlabel('Количество')
plt.ylabel('Года')
for ind,val in enumerate(france):
    label= format(int(val), '_') # . это разделитель разрядов
    plt.annotate(label, xy=(val+20,ind-0.05), color='black')

plt.savefig(f'{pathImage}/{nameImage}{numberImage}.{extendImage}')
numberImage+=1
plt.show()


