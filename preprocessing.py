import pandas as pd
data = {'Name':['sajin','nijas','Aaron','sajin','None','queen'],
                       'Age':[25,None,30,25,28,35],
                       'Salary':[50000,60000,None,50000,70000,80000],
}
#Create a DataFrame 

df= pd.DataFrame(data)
print("Original DataFrame:")
print(df)
#STEP 1 - REMOVE DUPLICATES
df = df.drop_duplicates()
print("------------------------------------")
print("After removing the duplicates values")
print("------------------------------------")
print(df)
#STEP 2 - HANDLE MISSING VALUES
df['Name'].fillna('Unknown',inplace=True)
#REPLACE MISSING NAMES WIITH 'UNKNOWN'
df['Age'].fillna(df['Age'].mean(),inplace=True)
#REPLACE MISSING AGES WITH THE MEAN AGE
df['Salary'].fillna(df['Salary'].median(),inplace=True)
#REPLACE MISSING SALARIES WITH THE MEDIAN SALARY
#STEP3:CONVERT DATA TYPES(IF NEEDED)
df['Age']=df['Age'].astype(int)
#CONVERT AGE TO INTEGER TYPE
print("----------------------")
print("Cleaned DataFrame:")
print("----------------------")
print(df)


'''
Original DataFrame:
    Name   Age   Salary
0  sajin  25.0  50000.0
1  nijas   NaN  60000.0
2  Aaron  30.0      NaN
3  sajin  25.0  50000.0
4   None  28.0  70000.0
5  queen  35.0  80000.0
------------------------------------
After removing the duplicates values
------------------------------------
    Name   Age   Salary
0  sajin  25.0  50000.0
1  nijas   NaN  60000.0
2  Aaron  30.0      NaN
4   None  28.0  70000.0
5  queen  35.0  80000.0
----------------------
Cleaned DataFrame:
----------------------
    Name  Age   Salary
0  sajin   25  50000.0
1  nijas   29  60000.0
2  Aaron   30  65000.0
4   None   28  70000.0
5  queen   35  80000.0
'''