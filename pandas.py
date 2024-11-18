import pandas as pd
a = [1,7,2]
myvar = pd.Series(a)
print(myvar)

'''
0    1
1    7
2    2
dtype: int64
'''

import pandas as pd
a = [1,7,2]
myvar = pd.Series(a)
print(myvar[0])

#O/P - 1

import pandas as pd
df = pd.DataFrame({'A':[1,2,None,4],'B':[5,None,7,None]})
print(df)
print("\n")
df.fillna(0,inplace=True)
print(df)

'''
# -O/P

     A    B
0  1.0  5.0
1  2.0  NaN
2  NaN  7.0
3  4.0  NaN


     A    B
0  1.0  5.0
1  2.0  0.0
2  0.0  7.0
3  4.0  0.0

'''


import pandas as pd
df =pd.DataFrame({'A':[1,2,None,4],'B':[5,None,7,3]})
print(df)
print("\n")
df.dropna(inplace=True)
print(df)

'''
#-O/P

     A    B
0  1.0  5.0
1  2.0  NaN
2  NaN  7.0
3  4.0  3.0


     A    B
0  1.0  5.0
3  4.0  3.0

'''


import pandas as pd
a = [1,7,2]
myvar = pd.Series(a)
print(myvar[0])
print("\n")
print(myvar)

# - O/P
'''

1


0    1
1    7
2    2
dtype: int64

'''

import pandas as pd
calories = {"day1":420,"day2":380,"day3":390}
myvar= pd.Series(calories)
print(myvar)

'''
#-O/P

day1    420
day2    380
day3    390
dtype: int64


'''

import pandas as pd
calories = {"day1": 420,"day2":380,"day3":390}
myvar = pd.Series(calories,index = ["day1","day2"])
print(myvar)

'''
day1    420
day2    380
dtype: int64
'''


# - Create a DataFrame from two Series:

import pandas as pd
data = {
    "calories":[400,399,300],
    "duration":[50,40,60]
}
myvar = pd.DataFrame(data)
print(myvar)


'''
O/P

   calories  duration
0       400        50
1       399        40
2       300        60

'''

#- over

'''

Locate Row
As you can see from the result above, the DataFrame is like a table with rows and columns.

Pandas use the loc attribute to return one or more specified row(s)

'''

import pandas as pd
data = {
    "calories":[400,399,300],
    "duration":[50,40,60]
}
myvar = pd.DataFrame(data)
print(myvar)
print("\n")
#refer to the row index:
print(myvar.loc[0])


'''

 calories  duration
0       400        50
1       399        40
2       300        60


calories    400
duration     50
Name: 0, dtype: int64

'''


# - OVER 

'''

Locate Row
As you can see from the result above, the DataFrame is like a table with rows and columns.

Pandas use the loc attribute to return one or more specified row(s)

'''

import pandas as pd
data = {
    "calories":[400,399,300],
    "duration":[50,40,60]
}
myvar = pd.DataFrame(data)
print(myvar)
print("\n")
#refer to the row index:
print(myvar.loc[0])
print("\n")
print(myvar.loc[1])

'''
   calories  duration
0       400        50
1       399        40
2       300        60


calories    400
duration     50
Name: 0, dtype: int64


calories    399
duration     40
Name: 1, dtype: int64
'''




import pandas as pd
data = {
    "calories":[20,30,40,50],
    "duration":[1,3,6,7]

}
myvar = pd.DataFrame(data)
print(myvar)
print("\n")
print(myvar.loc[[0,1,2]])


'''
  calories  duration
0        20         1
1        30         3
2        40         6
3        50         7


   calories  duration
0        20         1
1        30         3
2        40         6

'''

import pandas as pd

data1 = {
  "name": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}

data2 = {
  "name": ["Sally", "Peter", "Micky"],
  "age": [77, 44, 22]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

newdf = df1.merge(df2, how='right')
print(newdf)


'''
    name  age
0  Sally   77
1  Peter   44
2  Micky   22
'''