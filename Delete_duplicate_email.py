import pandas as pd  

person.sort_values(['id'], inplace= True)
person.drop_duplicates('email', inplace= True)