import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

x = np.linspace(-1.5, 2.5, 1000)
y = np.exp(-x/0.294)
z = np.random.normal(0,1,1000)
y1 = gaussian(x, 0, 0.3)

plt.figure()
plt.plot(x, y,linewidth=4,color='darkorange')

plt.figure()
# plt.plot(x,gaussian(x, 0, 0.2),linewidth=3,color='forestgreen')
plt.plot(x,y1,linewidth=4,color='mediumseagreen')


# plt.plot(x,y1,linewidth=4,color='black')

# # case 1
# x2 = np.linspace(-1.5, -0.2, 1000)
# x3 = np.linspace(0.2,1.5, 1000)
# y2= gaussian(x2, 0, 0.3)
# y3= gaussian(x3, 0, 0.3)

# plt.fill_between(x2, 0, y2, facecolor='seagreen')
# plt.fill_between(x3, 0, y3, facecolor='seagreen')

# # case 2
# x4 = np.linspace(0.2, 2.5, 1000)
# y4 = gaussian(x4, 0, 0.3)

# plt.fill_between(x4, 0, y4, facecolor='seagreen')

# # case 3
# x5 = np.linspace(0.5, 2.5, 1000)
# x6 = np.linspace(-1.5,-0.5, 1000)
# y5= gaussian(x5, 0, 0.3)
# y6= gaussian(x6, 0, 0.3)

# plt.fill_between(x5, 0, y5, facecolor='seagreen')
# plt.fill_between(x6, 0, y6, facecolor='seagreen')


plt.show()
