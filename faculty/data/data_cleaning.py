import numpy as np
import pandas as pd
import json
import sys

with open(sys.argv[1],'r') as file:
    data1 = json.loads(file.read())
#print(data)

df1 = pd.DataFrame(data1)
print(df1)

df1.to_excel('new_data.xlsx')