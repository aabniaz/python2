import matplotlib.pyplot as plt

countries = ['Germany', 'Austria', 'South Korea', 'US', 'UK', 'India']
percentages = [16.5, 3.4, 9.2, 18.8, 24.6, 27.7]
colors = ['aquamarine', 'purple', 'yellow', 'blue', 'green', 'red']
explode = [0.1 if country == 'US' else 0 for country in countries]
plt.pie(percentages, labels=countries, startangle=45, autopct='%1.1f%%', explode=explode, shadow = True, colors=colors)
plt.axis('equal')
plt.title('Population Density Index')
plt.show()
