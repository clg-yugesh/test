from pandas import DataFrame, Series 
x={'Id': Series ([1,2,3,4,5], index=['a', 'b', 'c ','d', 'e']), "Name": Series(["A", "B", "C"],index=['a', 'b',' c'])} 
df=DataFrame (x) 
#by row label 
print(df.loc['a']) 
#by using row integer row location 
print(df.iloc[4]) 
#by using slice operator : 
print(df [0:3])