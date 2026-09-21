 import matplotlib
matplotlib.use('TkAgg') # отдельное окно для графиков
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#1)создание графика (кривая линия)
# x=np.linspace(0,10,1000)
# plt.plot(x,np.sin(x))
# plt.plot(x,np.cos(x))
# # созадем общий масштаб по х и у
# plt.axis('equal')

# способо настройки цвета линий
# x=np.linspace(0,10,1000)
# plt.plot(x,np.sin(x), color='gold')
# #краткий код цвета rgbcmyk
# # plt.plot(x,np.sin(x-1), color='r')
#
# # шкала оттенков серого цвета, число от 0 до 1
# plt.plot(x,np.sin(x-2), color='0.548')
#
# #16ный код цвета в формате #RRGGBB
# plt.plot(x,np.sin(x-3), color='#FDDA15')
#
# # кортеж RGB с значениямиот 0 до 1
# plt.plot(x,np.sin(x-4), color=(0.9,0.2,0.3))

# способы задания стиля линий
# x=np.linspace(0,10,1000)
# сплошная линия
# plt.plot(x,np.sin(x), color='gold', linestyle='solid')
# # штриховая
# plt.plot(x,np.cos(x+1), color='silver',linestyle='dashed')
# # штрих-пунктир
# plt.plot(x,np.sin(x+2), color='black', linestyle='dashdot')
# #пунктрирная
# plt.plot(x,np.cos(x+3), color='red', linestyle='dotted')


# 2 способ создания линий
# x=np.linspace(0,10,1000)
# сплошная линия
# plt.plot(x,np.sin(x), color='gold', linestyle='-')
# # штриховая
# plt.plot(x,np.cos(x+1), color='silver',linestyle='--')
# # штрих-пунктир
# plt.plot(x,np.sin(x+2), color='black', linestyle='-.')
# #пунктрирная
# plt.plot(x,np.cos(x+3), color='red', linestyle='..')





plt.show()