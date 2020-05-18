from openpyxl import *

wb = load_workbook('test.xlsx')
print( wb.sheetnames )
ws = wb.active
print(ws)

g = ws.rows
cells = next(g)
print(cells)

keys = []
for cell in cells:
    keys.append(cell.value)

print(keys)

data = []
for row in g:
    dic = {k:c.value for k , c in zip(keys,row)}
    data.append(dic)
print(data)
    