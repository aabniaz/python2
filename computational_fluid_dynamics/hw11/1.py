import numpy as np
import matplotlib.pyplot as plt

def init(xs, ts):
    x = np.arange(0, 1.01, xs)
    t = np.arange(0, 1.01, ts)
    y = np.zeros((len(t), len(x)))
    y_new = np.zeros_like(y)
    y[:, 0] = 1  
    y_new[:, 0] = 1
    return x, t, y, y_new

def maccormac(y, y_new, c, ts, xs, ф):
    for i in range(len(t)-1):
        y_new[i+1, 1:-1] = y[i, 1:-1] - (c * ts * (y[i, 1:-1] - y[i, :-2])) / xs
        y[i+1, 1:-1] = 0.5 * (y[i, 1:-1] + y_new[i+1, 1:-1] - (c * ts * (y_new[i+1, 1:-1] - y_new[i+1, :-2])) / xs)
        if i > 0 and np.max(np.abs(y[i+1, :] - y[i, :])) < ф:
            break
    return y

def plot_result(x, y):
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('u')
    plt.show()

xs = 0.01
ts = 0.01
c = 1
a = 0.00001
x, t, y, y_new = init(xs, ts)
result = maccormac(y, y_new, c, ts, xs, a)
plot_result(x, result[-1])
