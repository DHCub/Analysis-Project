from random import random
from pylab import *

from MonicPoly3RootFinder import *

def GetFR():
    a = 300*random() - 150
    b = 300*random() - 150
    c = 300*random() - 150

    f = lambda x: x**3 + a*x**2 + b*x + c
    r = MonicPoly3Root(a, b, c)
    return (f, r)

def GetAxes(f: callable, x1: float, x2: float, amount: int = 1080):
    inc = (x2 - x1)/amount
    X = []
    Y = []
    while(x1 < x2):
        X.append(x1)
        Y.append(f(x1))
        x1 += inc

    return (X, Y)



# fig, ax = plt.subplots()

# f, r = GetFR()
# X, Y = GetAxes(f, -10, 10)
# plot = ax.plot(X, Y)[0]
# vline = ax.axvline(x=r, linestyle="--")
# grid()

# def update(frame):
#     f, r = GetFR()
#     X, Y = GetAxes(f, -10, 10)
#     plot.set_xdata(X)
#     plot.set_ydata(Y)
#     vline.set_xdata([r])
#     print(f(r))
    

# ani = anim.FuncAnimation(fig=fig, func=update, interval=1)
# plt.show()

