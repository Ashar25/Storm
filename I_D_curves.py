import numpy as np
import matplotlib.pyplot as plt
import math


x = np.array([60, 120, 180, 240, 300]);
factor = np.array([1 ,0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05]);
print(factor)
percent =np.multiply(factor, 100)
print(percent)
a = 84.4; b = -0.01225; c = 13.8 ; d = 0.0008861;
y = [55, 35, 25, 22, 20];
y_fit = []
plt.figure(figsize= (25,15) , dpi = 300)
# print(x)
legend_properties = {'weight':'bold','size':30}
for i in range (0,11):
    for j in range (0,5):
        pi = factor[i] * a * math.exp(b*x[j]) + factor[i] *  c * math.exp(d*x[j]);
        y_fit.append(pi)
    plt.plot(x,y_fit,linewidth = 6, label = '{}-{} %'.format(i+1,percent[i]))
    y_fit = []
plt.legend(prop=legend_properties, loc = 0)
plt.xlabel('Rainfall Duration(min)', size = 40, weight = 'bold')
plt.ylabel('Rainfall Intensity(mm/hr)', size  = 40, weight = 'bold')
plt.xticks(fontsize = 18 , weight = 'bold')
plt.yticks(fontsize = 18 , weight = 'bold')
plt.title('(d) Intensity-duration (PI-PD) curves',size = 40 , weight = 'bold' )

# plt.annotate('Graph 1',xy=(60, 55), xytext=(3, 4),
#                                         arrowprops=dict(facecolor='blue', shrink=0.02))
plt.savefig(r'E:\Project\Stormbang\Results\pictures\Input_pics\idcurve.jpg',bbox_inches = 'tight',dpi =400)
#plt.show()