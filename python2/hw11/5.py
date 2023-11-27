import matplotlib.pyplot as plt

pie_data = [10.2, 10.2, 10.7, 17.7, 30.3, 21.0] 
pie_labels = ['Germany', 'Greece', 'Iceland', 'Ireland', 'Italy', 'Other']
bar_data = [3.6, 3.8, 4.1, 4.2, 5.3]
bar_labels = ['Austria', 'Belgium', 'Denmark', 'Finland', 'France']
bar_colors = ['DarkOliveGreen', 'LightSeaGreen', 'MediumSeaGreen', 'Olive', 'PeachPuff']
fig, ax = plt.subplots()
ax.pie(pie_data, labels=pie_labels, autopct='%1.1f%%', startangle=90, colors=['Khaki', 'SandyBrown', 'Tomato', 'PaleVioletRed', 'MediumVioletRed', 'Aquamarine'])
ax.axis('equal') 
ax.set_title('Country Distribution')
bottom = 1
for height, label, color in zip(bar_data, bar_labels, bar_colors):
    ax.text(height, bottom, f'{height:.1f}%', va='center', color=color)
ax.legend(loc='upper right', labels=bar_labels)
ax.set_yticks([])  
ax.set_title('Country Percentages (Bar Chart)')
plt.show()
