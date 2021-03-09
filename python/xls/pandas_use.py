import pandas as pd


xls = pd.read_excel("C:\\Users\\pc11\\Desktop\\data.xlsx")

for n in xls[1:100]:
    print(n)