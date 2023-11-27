import matplotlib.pyplot as plt

x_coords = [13, 16, 22, 1, 4, 28, 4, 8, 10, 20, 22, 19, 5, 24, 7, 25, 25, 13, 27, 2, 7, 8, 24, 15, 25, 18, 6, 26, 14, 9]
y_coords = [42, 46, 62, 66, 66, 8, 83, 20, 35, 88, 70, 89, 89, 11, 59, 64, 39, 89, 46, 89, 81, 38, 25, 78, 72, 8, 20, 80, 70, 79]
plt.scatter(x_coords, y_coords, marker='^', color='blue')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()
