from pandas import DataFrame, Series 
x={'Id': Series([1,2,3,4,5],index=['a','b ','c', 'd', 'e']), "Name": Series(("A", "B", "C"),index=['a',' b','c'])} 
df=DataFrame (x) 
print(df.drop('a'))