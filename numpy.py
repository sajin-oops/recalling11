import numpy as np
arr = [20,20,20,20,20]
a = np.mean(arr)
print(a)

'''
20.0
'''


# to find standard deviation
import numpy as np
arr = [20,20,20,20,20]
a = np.std(arr)
print(a)

'''
0.0
'''

#Load Files Into a DataFrame
import pandas as pd
df = pd.read_csv('data.csv')
print(df)
