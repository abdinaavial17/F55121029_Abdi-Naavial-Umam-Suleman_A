import matplotlib.pyplot as plt

data = [1, 2, 3, 4, 3, 2, 5, 4, 3, 2, 1, 3, 4, 2, 1]

plt.hist(data, bins=5, edgecolor='black')

plt.title('Histogram data')
plt.xlabel('Nilai')
plt.ylabel('Frekuensi')

plt.show()