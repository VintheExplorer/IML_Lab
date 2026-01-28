import numpy as np
import pandas as pd

rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))

arr=[]
for i in range(rows):
        row=[]
        for j in range(cols):
            data=int(input(f"Enter the element{i+1},{j+1}: "))
            row.append(data)
        arr.append(row)

np_array=np.array(arr)
print("\nas 2D Numpy array: ")
print(np_array)

np_1D=np_array.flatten()
print("\nas 1D Array using Numpy: ")
print(np_1D)

data2=pd.DataFrame(np_array)
print("\nas Pandas dataframe: ")
print(data2)

pd_1D=data2.values.flatten()
print("\nas 1D array using Pandas: ")
print(pd_1D)


