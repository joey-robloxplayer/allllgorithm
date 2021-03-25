import matplotlib.pyplot as plt


fig, ax = plt.subplots()

x = [1.0, 2.0, 3.0, 4.0, 5.0]
ys = [1.144, 2.900, 4.188, 9.161, 16.979]
yb = [0.240, 0.481, 0.940, 1.926, 3.855]
ax.plot(x, ys, label="simple search")
ax.plot(x, yb, label="binary search")
ax.legend()
plt.show()