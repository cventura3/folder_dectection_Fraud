#read excel file using pandas
import pandas as pd
import numpy as np
from pandas import ExcelWriter
from pandas import ExcelFile

# xldr needed to read excel file. xldr is already installed, matplotlib is installed
from matplotlib import pyplot as plt


# read excel file
df = pd.read_excel(r"C:\Users\Jazmi\OneDrive\Documents\coding\iris_dataset.xlsx", sheet_name='Sheet1')


# print all the columns of the data print(df.columns)
print("Columns heading:")
print(df.columns)
print(df)

# get one specific column using  print(df['sepal_width']). Get entire columns

sepal_length = df['sepal_length']
sepal_width = df['sepal_width']
petal_length = df['petal_length']
petal_width = df['petal_width']

# create array
np_sepal_length = np.array(sepal_length)

#np_sepal_width = np.array(sepal_width)

# double the size
np_sepal_length = np_sepal_length * 2






print(np_sepal_length)
#np_sepal_width = np_sepal_width * 5


plt.scatter(sepal_length, sepal_width, label='Sepal', color='green', alpha=0.8,
            s=np_sepal_length
            )

#plt.scatter(petal_length, petal_width, label='Petal', color='pink', alpha=0.8)

plt.xlabel('Length')
plt.ylabel('Width')
plt.title('Iris Data set')
plt.legend()
plt.show()

print(df)













