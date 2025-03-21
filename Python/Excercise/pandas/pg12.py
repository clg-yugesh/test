#using dictionary pg 12
import pandas as pd
info = {1: 'rays',2: 'tech'}
a = pd.Series(info)
print(a)

#using scalar value
import pandas as pd
a = pd.Series(4,index=[1,2,3,4,5])
print(a)
