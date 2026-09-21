import matplotlib.pyplot as plt
import numpy as np
# x=np.arange(0,10)
# y=2*x**2
# plt.plot(x,y)
# plt.show()

a= np.linspace(0,10,11)
b=a**4
x=np.arange(2,10)
y=2*x

fig=plt.figure()
# большие оси
# axes1=fig.add_axes([0.05,0.05,1,1])
# axes1.plot(a,b)
# axes1.set_xlim(0,10)
# axes1.set_ylim(0,10000)
# axes1.set_xlabel('X')
# axes1.set_ylabel('Y')
# axes1.set_title('возведение в степент')
#
# axes2=fig.add_axes([0.2,0.2,0.35,0.35])
# axes2.plot(a,b)
# axes2.set_xlim(1,2)
# axes2.set_ylim(0,50)
# axes2.set_xlabel('A')
# axes2.set_ylabel('B')
# axes2.set_title('умнож на 2')


fig,axes=plt.subplots(nrows=2,ncols=2)
axes[0][1].plot(x*2,y)
axes[1][0].plot(x,y)
axes[0][0].plot(a,b)
axes[1][1].plot(a*1.5,b*a)
plt.show()
