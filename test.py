import xlwings as xw
import pandas as pd

df = pd.read_excel(r'C:\Users\n429310\Documents\squash.xlsx', sheetname="Blad1")

participants = len(df)+1
print ("Number of participants: %s" %participants)

print (df)
