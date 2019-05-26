import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Over_Under Output/ML_Input.csv')
df.dropna(inplace=True)

x = df['2.5'].values
names = ['0.5', '1.5', '3.5', '4.5', '5.5', '6.5', '7.5']

for i in range(len(names)):
    y = df[names[i]].values

    z = np.polyfit(x, y, 3)
    # zz = np.polyfit(x, np.log(y), 1)

    p = np.poly1d(z)
    # p = np.poly1d(zz)

    print(p)
    xp = np.linspace(1.16, 2.82, 100)
    plt.scatter(x, y)
    plt.plot(xp, p(xp), '--')

plt.yscale('log')
plt.show()
