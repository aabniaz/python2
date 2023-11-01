import matplotlib.pyplot as plt

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создание графика
plt.plot(x, y)

# Добавление заголовка и подписей осей
plt.title('Пример графика')
plt.xlabel('X')
plt.ylabel('Y')

# Сохранение графика в файл
plt.savefig('plot.png')

# Вместо plt.show(), сохраняя график в файл, выше используется plt.savefig()

print("График сохранен в файл plot.png")
