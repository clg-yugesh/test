from pandas import DataFrame, Series 
x={'Id': Series ([1,2,3,4,5]), "Name":Series (["A" , "B", "C", "D", "E"])} 
df = DataFrame (x) 
print (df) 
#Add a Column from DataFrame 
df ['Subject']=Series (["C", "C++", "Java", "python ", "Java", "Julia"]) 
del df ["Id"] # Delete a Column from DataFrame Using del function 
print (df) 
df.pop ("Name") # Delete a Column from DataFrame Using pop function